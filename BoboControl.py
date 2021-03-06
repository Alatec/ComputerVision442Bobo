# !/usr/bin/python
from evdev import InputDevice, categorize, ecodes, KeyEvent

import maestro

MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3

bobo = maestro.Controller()

gamepad = InputDevice('/dev/input/event3')

bobo = maestro.Controller()
body = 6000
headTurn = 6000
headTilt = 6000
motors = 6000
turn = 6000
amount = 1200

turn = 6000
bobo.setTarget(TURN, turn)
motors = 6000
bobo.setTarget(MOTORS, motors)
bobo.setTarget(BODY, 6000)
bobo.setTarget(HEADTILT, 6000)
bobo.setTarget(HEADTURN, 6000)
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.keycode[0] == 'BTN_A':
                print("X")
                motors -= amount
                if (motors < 1510):
                    motors = 1510
                print(motors)
                bobo.setTarget(MOTORS, motors)
            elif keyevent.keycode[1] == 'BTN_Y':
                print("Square")
                turn -= amount
                if (turn < 2110):
                    turn = 2110
                print(turn)
                bobo.setTarget(TURN, turn)

            elif keyevent.keycode[0] == 'BTN_B':
                print("Circle")
                turn += amount
                if (turn > 7400):
                    turn = 7400
                print(turn)
                bobo.setTarget(TURN, turn)
            elif keyevent.keycode[1] == 'BTN_X':
                print("Triangle")
                motors += amount
                if (motors > 7900):
                    motors = 7900
                print(motors)
                bobo.setTarget(MOTORS, motors)
            else:
                turn = 6000
                bobo.setTarget(TURN, turn)
                motors = 6000
                bobo.setTarget(MOTORS, motors)
