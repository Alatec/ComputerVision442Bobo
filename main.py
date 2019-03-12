# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import BoboGo as bg

import maestro

MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3

bobo = maestro.Controller()
body = 6000
headTurn = 6000
headTilt = 6000
motors = 6000
turn = 6000
amount = 400

def calcWeight(x, y):
    return np.exp(-(640-y)/200)*x

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

    orange = cv2.inRange(hsv, (10, 63, 103), (25, 255, 255))
    orange = cv2.medianBlur(orange, 5)
    #contours, ret = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #canny = cv2.Canny(orange, 100, 170)
    contours, ret = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # show the frame

    weightedX = 0
    weightTotal = 0.01
    for i in range(len(contours)):

        if cv2.contourArea(contours[i]) > 100:
            M = cv2.moments(contours[i])
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #cv2.circle(image, (cX, cY), 7, (255, 70, 180), -1)
            weight = np.exp(-(640-cY)/200)
            weightTotal += weight
            weightedX += weight*cX

    avgX = weightedX/weightTotal

    cv2.circle(image, (int(avgX), 320), 17, (255, 70, 180), -1)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    if(avgX < 260):
        bg.goRight(0.25)
        bg.stop()
    elif (avgX > 380):
        bg.goLeft(0.25)
        bg.stop()
    else:
        bg.goForward(0.5)
        bg.stop()

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            break
