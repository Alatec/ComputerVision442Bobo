# import the necessary packages
#Arynn Collins and Andrew Johnson
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import BoboGo as bg
#import BoboFace as bf
import BoboFollow as bf 
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
    return np.exp(-(480-y)/0.01)*x

def calcTurnTime(x):
    return 0.02*((x-320)/160)**2 + 0.25
    #return 0.25
def calcTurnAmount(x):
    return 200*((x-320)/160)**2 + 800


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))


# allow the camera to warmup
time.sleep(0.5)
cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

face_cascade = cv2.CascadeClassifier('facefile.xml')

#bg.start()
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)

    for face in faces:
        cv2.rectangle(image, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (255, 0, 0), 2)
        print("y = " + face[1] + "   x = " + face[0])
        bf.findFace(face[1], face[0])
    cv2.imshow("Frame", image)

    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        bg.stop()
        break
