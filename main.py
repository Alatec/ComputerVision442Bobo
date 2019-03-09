# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)
cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #hsv = cv2.medianBlur(hsv, 5)
    orange = cv2.inRange(hsv, (80, 77, 61), (89, 131, 133))



    orange = cv2.medianBlur(orange, 5)
    contours, ret = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.empty_like(orange)

    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 100:
            cv2.drawContours(mask, contours, i, (255, 255, 255), thickness=cv2.FILLED)

    mask = cv2.erode(mask, (5, 5))
    mask = cv2.dilate(mask, (5, 5))
    # mask = cv2.Canny(mask, 100, 170)
    contours, ret = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # print(len(contours))
    center = np.zeros(2, np.uint8)
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 100:
            M = cv2.moments(contours[i])
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.drawContours(image, contours, i, (255, 255, 255), thickness=cv2.FILLED)
            center[0] += cX
            center[1] += cY
    center = center/len(contours)
    cv2.circle(image, (center[0], center[1]), 4, (255, 50, 200))

    # show the frame

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            break
