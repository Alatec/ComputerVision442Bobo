# !/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent

gamepad = InputDevice('/dev/input/event4')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        print(event)
        print("-----------------------")
        print(keyevent)
        print("+++++++++++++++++++++++")
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.keycode[0] == 'BTN_A':
                print("Back")
            elif keyevent.keycode[1] == 'BTN_Y':
                print("Forward")
            elif keyevent.keycode[2] == 'BTN_B':
                print("Right")
            elif keyevent.keycode[3] == 'BTN_X':
                print("Left")