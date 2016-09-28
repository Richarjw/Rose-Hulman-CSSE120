"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Jack Richard-Joe J- Ryan C (all of them).

The primary author of this module is: Jack Richard.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m4
import random
import tkinter
from tkinter import ttk
import new_create
# from m1 import DataContainer
import time


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m3:')
    print('-------------------------------')
    initial_frame()

def initial_frame(initial_frame):
#     root = tkinter.Tk()
#
#     initial_frame = ttk.Frame(root, padding=(30, 20), relief='raised')
#     initial_frame.grid()

    playNotes_button = ttk.Button(initial_frame, text='Play Notes')
    playNotes_button.grid()
    playNotes_button['command'] = lambda: notes_frame()

    moveSensors_button = ttk.Button(initial_frame, text='Move until Sensors')
    moveSensors_button.grid()
    moveSensors_button['command'] = lambda: moveSensors_frame()

    conversation_button = ttk.Button(initial_frame, text='Conversation')
    conversation_button.grid()
    conversation_button['command'] = lambda: conversation_frame()

#     root.mainloop()

def notes_frame():
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
    """
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=(30, 20), relief='raised')
    main_frame.grid()

    n_entry = ttk.Entry(main_frame, width=3)
    n_entry.grid(row=1, column=1)

    note_label = ttk.Label(main_frame, text='Press a button to complete a task')
    note_label.grid()

    note_button = ttk.Button(main_frame, text='Play n Notes')
    note_button.grid()
    note_button['command'] = lambda:  playNotes(int(n_entry.get()))

    root.mainloop()

def playNotes(n):
    # CurrentRobot = m1.Robot.Robot
#     port = 'sim'
#     robot = new_create.Create(port)
    for k in range(n):
        m0.Robot.Robot.playNote(random.randint(31, 127), 50)
        time.sleep(2)

def moveSensors_frame():
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    speed_label = ttk.Label(main_frame, text='Enter the speed:')
    speed_label.grid()

    speed_entry = ttk.Entry(main_frame, width=10)
    speed_entry.grid()

    stop_button = ttk.Button(main_frame, text='stop')
    stop_button.grid()
    stop_button['command'] = lambda: follow_stop()

    run_button = ttk.Button(main_frame, text='Run Robot')
    run_button.grid()
    run_button['command'] = lambda: moveSensors(root, int(speed_entry.get()))

    root.mainloop()

def moveSensors(root, speed):
#     port = 'sim'
#     robot = new_create.Create(port)
#     cliff_front_left = new_create.Sensors.cliff_front_left_signal
#     cliff_front_right = new_create.Sensors.cliff_front_right_signal
    m0.Robot.follow = True
    while m0.Robot.follow:
        m0.Robot.Robot.driveDirect(speed, speed)
        left_sensor = m0.Robot.Robot.getSensor('CLIFF_FRONT_LEFT_SIGNAL')
        right_sensor = m0.Robot.Robot.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')
        bumps = m0.Robot.Robot.getSensor('BUMPS_AND_WHEEL_DROPS')
        if left_sensor < 20 or right_sensor < 20:
            m0.Robot.Robot.stop()
            break
        if bumps == [0, 0, 0, 1, 1] or bumps == [0, 0, 0, 0, 1] or bumps == [0, 0, 0, 1, 0]:
            m0.Robot.Robot.stop()
            m0.Robot.Robot.driveDirect(-1 * speed, -1 * speed)
            time.sleep(.5)
            m0.Robot.Robot.driveDirect(-speed, speed)
            time.sleep(1)
            m0.Robot.Robot.stop()
        root.update()
    m0.Robot.Robot.stop()
def follow_stop():

    m0.Robot.follow = False

def conversation_frame():
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    led_entry = ttk.Entry(main_frame, width=10)
    led_entry.grid()

    led_label = ttk.Label(main_frame, text='Enter an integer between 0 and 7')
    led_label.grid()

    run_button = ttk.Button(main_frame, text='Begin Conversation')
    run_button.grid()
    run_button['command'] = lambda: talk(int(led_entry.get()))

def talk(entry):
#     port = 'sim'
#     robot = new_create.Create(port)
    if entry == 0:
        print('Press Spot')
    elif entry == 1:
        print('Press Clean')
    elif entry == 2:
        print('Press Max')
    elif entry == 3:
        print('Press Forward')
    elif entry == 4:
        print('Press Left')
    elif entry == 5:
        print('Press Right')
    elif entry == 6:
        print('Press Red Button')
    elif entry == 7:
        print('Press P')
    else:
        print('Invalid Entry')
    listen()
def listen():
    IR_BYTE = new_create.Sensors.ir_byte
    while True:
        ir_read = m0.Robot.Robot.getSensor('IR_BYTE')
        if ir_read == 130:
            m0.Robot.Robot.setLEDs(0, 255, 0, 0)
            break
        if ir_read == 131:
            m0.Robot.Robot.setLEDs(0, 0, 1, 0)
            break
        if ir_read == 129:
            m0.Robot.Robot.setLEDs(0, 0, 0, 1)
            break
        if ir_read == 137:
            m0.Robot.Robot.setLEDs(0, 255, 1, 0)
            break
        if ir_read == 132:
            m0.Robot.Robot.setLEDs(0, 255, 0, 1)
            break
        if ir_read == 136:
            m0.Robot.Robot.setLEDs(0, 0, 1, 1)
            break
        if ir_read == 133:
            m0.Robot.Robot.setLEDs(0, 255, 1, 1)
            break
        if ir_read == 138:
            m0.Robot.Robot.setLEDs(0, 0, 0, 0)
            break




# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
