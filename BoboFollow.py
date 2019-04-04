import BoboGo as bg
import cv2

# defines the y,x values of the center bounding area
centerLeft = 200
centerRight = 280
centerTop = 300
centerBot = 340

amount = 100


def findFace(y, x):

            #turn body to face direction

    if x <= centerLeft:
        bg.lookLeft(amount)
    elif x >= centerRight:
        bg.lookRight(amount)
        print("Look at me, Bobo baby")

    if y <= centerTop:
        bg.lookUp(amount)
    elif y >= centerBot:
        bg.lookDown(amount)
        print("Stay put, Bobo baby")

    else:
        print("rip")

def getThirds(image):
    cv2.line(image, (centerLeft, 0), (centerLeft, 639), (0, 255, 0), 2)
    cv2.line(image, (centerRight, 0), (centerRight, 639), (0, 255, 0), 2)
    cv2.line(image, (0, centerTop), (479, centerTop), (0, 255, 0), 2)
    cv2.line(image, (0, centerBot), (479, centerBot), (0, 255, 0), 2)
    return image