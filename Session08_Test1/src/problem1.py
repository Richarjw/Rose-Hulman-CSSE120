"""
Test 1, problem 1.

Authors: David Mutchler, Michael Wollowski, Mark Hays, their colleagues,
         and Jack Richard.  September 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the   problem1   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')
    problem1()


def problem1():
    """
    Prompts the user for and inputs:
      -- A string
      -- A floating point number
      -- Another string
    in that order (via three separate inputs).

    Then prints, in this order, on a SINGLE line,
    separated by spaces:
      -- The SECOND of the two strings
      -- The cosine of the floating point number
      -- The FIRST of the two strings
      -- The FIRST of the two strings AGAIN

    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
        Enter a string: I went skiing!
        Enter a floating point number: 3.0
        Enter another string: Mickey Mouse
        Mickey Mouse -0.9899924966004454 I went skiing! I went skiing!
    """
    # TODO: Implement and test this function.
    #       The testing code is already written for you (above).
    string = input('Enter a string:')
    number = float(input('Enter a floating point number:'))
    string2 = input('Enter another string:')
    print(string2, math.cos(number), string, string)
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
