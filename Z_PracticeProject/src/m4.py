"""
The  **** PRACTICE **** Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m3

import tkinter
from tkinter import ttk
import new_create

# ----------------------------------------------------------------------
# TODO: Do the following in STAGES, using ITERATIVE ENHANCEMENT.
#       That means that for each stage, you implement it, TEST it,
#       COMMIT your work WITH A SHORT, REASONABLE MESSAGE,
#       and then and only then continue to the next stage.
#
# Your ultimate goal for your part of this Practice Project is to have
# a correctly function button:
#   -- Spin N seconds
# plus two entry boxes in which the user can enter:
#   -- speed at which the robot is to spin
#   -- seconds the robot is to spin
#
# Use the following ITERATIVE ENHANCEMENT PLAN, where each stage
# augments the preceding stages:
#
#   Stage 1: Frame appears with the button and Entry boxes on it.
#
#   Stage 2: Button prints a message, as a stub.
#              -- A STUB is placeholder code that lets you do some
#                 testing even before you have finished the real code.
#
#   Stage 3: Button prints the values of the two entry boxes,
#              again as a stub.
#
#   Stage 4: Button works correctly.
#              That is, pressing it causes a robot to spin at the speed
#              in the first entry box, for the number of seconds
#              in the second entry box.
#
#   NOTES:
#     You will have to decide where in your code it is best to construct
#     the robot, and where it is best to do a robot shutdown.
#     Keep in mind that:
#       -- You will eventually use your teammate's connect and
#          disconnect buttons to construct the robot.
#       -- That same robot will eventually be used throughout the code.
#
#     TEST using the SIMULATOR for now.
#
# Do ALL your work in THIS file.  Do not touch m0!
# You will INTEGRATE work in the NEXT session, using m0 to do so.
# ----------------------------------------------------------------------


class DataContainer4():
    """ A container for the data shared across the application. """

    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m4:')
    print('-------------------------------')


def my_frame(root, data):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type data: DataContainer4
    """

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
