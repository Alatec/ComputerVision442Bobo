import BoboGo as bg

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

