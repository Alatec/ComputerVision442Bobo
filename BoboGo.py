import maestro
import time
MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3
zeroed = 6000
Tamount = 900
Famount = 1400

bobo = maestro.Controller()

def goLeft(delay):
    bobo.setTarget(TURN, zeroed - Tamount)
    time.sleep(delay)

def goRight(delay):
    bobo.setTarget(TURN, zeroed + Tamount)
    time.sleep(delay)


def goForward(delay):
    bobo.setTarget(MOTORS, zeroed - Famount)
    time.sleep(delay)


def goBackward(delay):
    bobo.setTarget(MOTORS, zeroed - Famount)
    time.sleep(delay)

def stop():
    for i in range(3):
        bobo.setTarget(i, 6000)
