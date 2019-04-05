import BoboGo as bg
import cv2

# defines the y,x values of the center bounding area
centerLeft = 300
centerRight = 340
centerTop = 220
centerBot = 260

amount = 100


def findFace(y, x):
    ret = False
    if x <= centerLeft:
        bg.lookLeft(amount)
        ret = True
    elif x >= centerRight:
        bg.lookRight(amount)
        ret = True
        print("Look at me, Bobo baby")

    if y <= centerTop:
        bg.lookUp(amount)
        ret = True
    elif y >= centerBot:
        bg.lookDown(amount)
        ret = True
        print("Stay put, Bobo baby")


    return ret

def getThirds(image):
    cv2.line(image, (centerLeft, 0), (centerLeft, 639), (0, 255, 0), 2)
    cv2.line(image, (centerRight, 0), (centerRight, 639), (0, 255, 0), 2)
    cv2.line(image, (0, centerTop), (479, centerTop), (0, 255, 0), 2)
    cv2.line(image, (0, centerBot), (479, centerBot), (0, 255, 0), 2)
    return image
