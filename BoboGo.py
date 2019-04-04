import maestro
import time
MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3
zeroed = 6000
Tamount = 900
Famount = 800
up = 6000
down = 6000
right = 6000
left = 6000

bobo = maestro.Controller()
def start():
    bobo.setTarget(4, 6000)
    time.sleep(0.3)
    bobo.setTarget(4, 1510)

def goLeft(delay, amount):
    bobo.setTarget(TURN, zeroed - int(amount))
    time.sleep(delay)

def goRight(delay, amount):
    bobo.setTarget(TURN, zeroed + int(amount))
    time.sleep(delay)

def goForward(delay):
    bobo.setTarget(MOTORS, zeroed - Famount)
    time.sleep(delay)

def goBackward(delay):
    bobo.setTarget(MOTORS, zeroed + Famount)
    time.sleep(delay)

def lookUp(amount):
    up += amount
	bobo.setTarget(HEADTILT, up)

def lookDown(amount):
    down += amount
	bobo.setTarget(HEADTILT, down)

def lookRight(amount):
    right += amount
	bobo.setTarget(HEADTURN, right)

def lookLeft(amount):
    left += amount
	bobo.setTarger(HEADTURN, left)

def stop():
    for i in range(3):
        bobo.setTarget(i, 6000)
