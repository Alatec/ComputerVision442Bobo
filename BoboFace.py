import numpy as np
import cv2
import time

class BoboFace:
    def __init__(self):
        print("Hello")
        self.face = np.zeros((480,800, 3), np.uint8)
        self.color = (255,255,255)
        self.eyeSize = 75

    def eye(self, eye, isOpen):
        if eye == "L" and isOpen:
            cv2.rectangle(self.face, (110, 150), (110 + self.eyeSize, 150 + self.eyeSize), self.color, thickness=cv2.FILLED)
        elif eye == "L" and not isOpen:
            cv2.rectangle(self.face, (110, 150), (110 + self.eyeSize, 150 + self.eyeSize//4), self.color, thickness=cv2.FILLED)
        elif eye == "R" and isOpen:
            cv2.rectangle(self.face, (690 - self.eyeSize, 150), (690, 150 + self.eyeSize), self.color, thickness=cv2.FILLED)
        elif eye == "R" and not isOpen:
            cv2.rectangle(self.face, (690 - self.eyeSize, 150), (690, 150 + self.eyeSize//4), self.color, thickness=cv2.FILLED)

    def drawFace(self):
        return self.face

    def reset(self):
        self.face = np.zeros((480, 800, 3), np.uint8)

cv2.namedWindow("Bobo", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Bobo",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
boboFace = BoboFace()
#while True:
boboFace.reset()
boboFace.eye("L", True)
boboFace.eye("R", True)
cv2.imshow("Bobo", boboFace.drawFace())
cv2.waitKey(0)
boboFace.reset()
boboFace.eye("L", False)
boboFace.eye("R", False)
cv2.imshow("Bobo", boboFace.drawFace())
cv2.waitKey(0)



