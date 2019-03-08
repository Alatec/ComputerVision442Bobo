# !/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent

gamepad = InputDevice('/dev/input/event4')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.keycode[0] == 'BTN_A':
                print("X")
            elif keyevent.keycode[1] == 'BTN_Y':
                print("Triangle")
            elif keyevent.keycode[0] == 'BTN_B':
                print("Circle")
            elif keyevent.keycode[1] == 'BTN_X':
                print("Square")