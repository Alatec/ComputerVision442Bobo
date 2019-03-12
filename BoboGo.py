import maestro
import time
MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3
zeroed = 6000
amount = 400

bobo = maestro.Controller()

def goLeft(delay):
    bobo.setTarget(TURN, zeroed - amount)
    time.sleep(delay)

def goRight(delay):
    bobo.setTarget(TURN, zeroed + amount)
    time.sleep(delay)


def goForward(delay):
    bobo.setTarget(MOTORS, zeroed + amount)
    time.sleep(delay)


def goBackward(delay):
    bobo.setTarget(MOTORS, zeroed - amount)
    time.sleep(delay)