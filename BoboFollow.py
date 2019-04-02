import BoboGo as bg

# defines the y,x values of the center bounding area
centerLeft = 200
centerRight = 280
centerTop = 280
centerBot = 360

amount = 200
delay = 0.2


def findFace(y, x):
    if x >= centerLeft and x <= centerRight:
        if y <= centerTop:
            bg.lookUp(delay, amount)
        elif y >= centerBot:
            bg.lookDown(delay, amount)
        else:
            print("Stay put, Bobo baby")
            #move forward/backwards
    elif x <= centerLeft:
        bg.lookLeft(delay, amount)
        if y <= centerTop:
            bg.lookUp(delay, amount)
        elif y >= centerBot:
            bg.lookDown(delay, amount)
        else:
            print("Look at me, Bobo baby")
            #turn body to face direction
    elif x >= centerRight:
        bg.lookRight(delay, amount)
        if y <= centerTop:
            bg.lookUp(delay, amount)
        elif y >= centerBot:
            bg.lookDown(delay, amount)
        else:
            print("Look at me, Bobo baby")
            #turn body to face direction

    else:
        print("rip")

