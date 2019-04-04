import BoboGo as bg

# defines the y,x values of the center bounding area
centerLeft = 200
centerRight = 280
centerTop = 300
centerBot = 340

amount = 100


def findFace(y, x):
    if x >= centerLeft and x <= centerRight:
        if y <= centerTop:
            bg.lookUp(amount)
        elif y >= centerBot:
            bg.lookDown(amount)
        else:
            print("Stay put, Bobo baby")
            #move forward/backwards
    elif x <= centerLeft:
        bg.lookLeft(amount)
        if y <= centerTop:
            bg.lookUp(amount)
        elif y >= centerBot:
            bg.lookDown(amount)
        else:
            print("Look at me, Bobo baby")
            #turn body to face direction
    elif x >= centerRight:
        bg.lookRight(amount)
        if y <= centerTop:
            bg.lookUp(amount)
        elif y >= centerBot:
            bg.lookDown(amount)
        else:
            print("Look at me, Bobo baby")
            #turn body to face direction

    else:
        print("rip")

