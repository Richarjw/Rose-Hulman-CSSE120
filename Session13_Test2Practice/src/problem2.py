"""
PRACTICE Test 2, problem 2.

Authors: David Mutchler, Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Jack Richard.  September 2013.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
from test.datetimetester import Oddballs


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()
    test_problem2c()
    test_problem2d()


# ----------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Students: Use this  is_prime  function in some of the problems below.
#           It is ALREADY DONE - no need to modify or add to it.
# ----------------------------------------------------------------------
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is an integer.
      (For integers < 2, this function returns False.)
    """
    if n < 2:
        return False

    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def test_problem2a():
    """ Tests the    problem2a    function. """

    # Some tests.
    tests = [st.SimpleTestCase(problem2a,
                               [(12, 33, 18, 9, 13, 3, 9, 20, 19, 20)],
                               19 + 3),
             st.SimpleTestCase(problem2a,
                               [(3, 12, 10, 8, 8, 9, 8, 11)],
                               10 + 8),
             st.SimpleTestCase(problem2a,
                               [(-9999999999, 8888888888)],
                               - 9999999999 + 8888888888),
             st.SimpleTestCase(problem2a,
                               [(8888888888, -9999999999)],
                               8888888888 + -9999999999),
             st.SimpleTestCase(problem2a,
                               [(-77, 20000, -33, 40000, -55, 60000, -11)],
                               - 11 + 20000),
             st.SimpleTestCase(problem2a,
                               [(9, 11, 13, 15, 17, 19, 22)], 33),
             st.SimpleTestCase(problem2a,
                               [(1, 2, 3, 4, 5, 6, 7, 8, 9)], 11),
             ]

    st.SimpleTestCase.run_tests('problem2a', tests)

    # ------------------------------------------------------------------
    # TODO: Add at least 2 more tests to the above list of tests.
    #       Try to choose tests that might expose errors in your code!
    # CONSIDER: Ask an assistant to CHECK your tests to confirm
    #           that they are adequate tests!
    # ------------------------------------------------------------------


def problem2a(sequence):
    """
    For the given sequence of numbers, returns the sum of:
      -- the largest of the numbers at EVEN INDICES, plus
      -- the smallest of the numbers at ODD INDICES.

    For example, if the sequence is:
       12, 33, 18, 9, 13, 3, 9, 20, 19, 20
    then the largest of the numbers at EVEN indices is the largest of
       12      18     13     9      19
    which is 19,

    and the smallest of the numbers at ODD integers is the smallest of
           33      9      3     20      20
    which is 3,

    so the answer in this example would be 19 + 3 = 22.

    Preconditionss:
      :type sequence (list, str, tuple)
    and the length of the sequence is at least 2
    and the sequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #       Some tests are already written for you (above),
    #       but you are required to write ADDITIONAL tests (above).
    # ------------------------------------------------------------------
    even = 0
    odd = 10000000000000000
    for k in range(0, len(sequence), 2):
        if sequence[k] > even:
            even = sequence[k]
    for k in range(1, len(sequence), 2):
        if sequence[k] < odd:
            odd = sequence[k]
    sum = even + odd
    return sum

def test_problem2b():
    """ Tests the    problem2b    function. """

    # Some tests.
    tests = [st.SimpleTestCase(problem2b,
                               [[12, 33, 18, 'hello', 9, 13, 3, 9]],
                               True),
             st.SimpleTestCase(problem2b,
                               [[12, 12, 33, 'hello', 5, 33, 5, 9]],
                               False),
             st.SimpleTestCase(problem2b,
                               [(77, 112, 33, 'hello', 0, 43, 5, 77)],
                               True),
             st.SimpleTestCase(problem2b,
                               [[1, 1, 1, 1, 1, 1, 2]],
                               False),
             st.SimpleTestCase(problem2b,
                               [['aa', 'a']],
                               False),
             st.SimpleTestCase(problem2b,
                               ['aaa'],
                               True),
             st.SimpleTestCase(problem2b,
                               [['aa', 'a', 'b', 'a', 'b', 'a']],
                               True),
             st.SimpleTestCase(problem2b,
                               [[9]],
                               False),
             st.SimpleTestCase(problem2b,
                               [(12, 33, 8, 'hello', 99, 'hello')],
                               True),
             st.SimpleTestCase(problem2b,
                               [['hello there', 'he', 'lo', 'hello']],
                               False),
             st.SimpleTestCase(problem2b,
                               [((8,), '8', (4 + 4, 4 + 4), [8, 8], 7, 8)],
                               False),
             st.SimpleTestCase(problem2b,
                               [[(8,), '8', [4 + 4, 4 + 4],
                                 (8, 8), 7, [8, 8]]],
                               True),
             st.SimpleTestCase(problem2b,
                               [[(8,), '8', [4 + 4, 4 + 4],
                                 [8, 8], 7, (8, 8)]],
                               False),
             st.SimpleTestCase(problem2b,
                               [(8, 8, 8, 8, 8, 9)], False),
             st.SimpleTestCase(problem2b,
                               [(1, 2, 3, 4, 5, 6, 7, 1)], True)
             ]

    st.SimpleTestCase.run_tests('problem2b', tests)

    # ------------------------------------------------------------------
    # TODO: Add at least 2 more tests to the above list of tests.
    #       Try to choose tests that might expose errors in your code!
    # CONSIDER: Ask an assistant to CHECK your tests to confirm
    #           that they are adequate tests!
    # ------------------------------------------------------------------


def problem2b(sequence):
    """
    Returns True if the last element of the sequence appears again
    somewhere else in the sequence.  Otherwise returns False.

    For example, given:
      Sequence [12, 33, 18, 'hello', 9, 13, 3, 9] - returns True
      Sequence [12, 12, 33, 'hello', 5, 33, 5, 9] - returns False
      Sequence [77, 112, 33, 'hello', 0, 43, 5, 77] - returns True
      Sequence [9] - returns False
      Sequence [12, 33, 8, 'hello', 99, 'hello'] - returns True
      Sequence ['hello there', 'he', 'lo', 'hello'] - returns False

    Preconditions:
      :type: sequence: (list, tuple, str)
    and the given sequence is non-empty.
    """
    last = sequence[len(sequence) - 1]
    for k in range(len(sequence) - 1):
        if last == sequence[k]:
            return True
    return False

    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #       Some tests are already written for you (above),
    #       but you are required to write ADDITIONAL tests (above).
    #
    # IMPLEMENTATION REQUIREMENT:  You are NOT allowed to use the
    #    'count' or 'index' methods for sequences in this problem
    #    (because here we want you to demonstrate your ability
    #    to use explicit looping here).
    # ------------------------------------------------------------------


def test_problem2c():
    """ Tests the    problem2c    function. """

    # Some tests.
    tests = [st.SimpleTestCase(problem2c,
                               [(9, 33, 8, 8, 0, 4, 4, 8)],
                               [2, 5]),
             st.SimpleTestCase(problem2c,
                               [(9, 9, 9, 9, 0, 9, 9, 9)],
                               [0, 1, 2, 5, 6]),
             st.SimpleTestCase(problem2c,
                               [(4, 5, 4, 5, 4, 5, 4)],
                               []),
             st.SimpleTestCase(problem2c,
                               ['abbabbb'],
                               [1, 4, 5]),
             ]

    st.SimpleTestCase.run_tests('problem2c', tests)

    # ------------------------------------------------------------------
    # TODO: Add at least 2 more tests to the above list of tests.
    #       Try to choose tests that might expose errors in your code!
    # CONSIDER: Ask an assistant to CHECK your tests to confirm
    #           that they are adequate tests!
    # ------------------------------------------------------------------


def problem2c(sequence):
    """
    Returns a list containing all the places (indices) where an item
    appears twice in a row.

    For example:
      Given sequence (9, 33, 8, 8, 0, 4, 4, 8)
         -- returns [2, 5]
              since 8 appears twice in a row starting at index 2
              and 4 appears twice in a row starting at index 5
      Given sequence (9, 9, 9, 9, 0, 9, 9, 9)
         -- returns [0, 1, 2, 5, 6]
      Given sequence (4, 5, 4, 5, 4, 5, 4)
         -- returns []
      Given sequence 'abbabbb'
         -- returns [1, 4, 5]

    Preconditions:
      :type: sequence: (list, tuple, str)
    and the given sequence is non-empty.    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #       Some tests are already written for you (above),
    #       but you are required to write ADDITIONAL tests (above).
    # ------------------------------------------------------------------
    list = []
    for k in range(1, len(sequence)):
        if sequence[k - 1] == sequence[k]:
            list.append(k - 1)
    return list

def test_problem2d():
    """ Tests the    problem2d    function. """

    # Some tests.
    tests = [st.SimpleTestCase(problem2d,
                               [(6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5)],
                               17 + 3 + 7 + 13),
             st.SimpleTestCase(problem2d,
                               [(7, 7, 7, 7, 7, 4, 4, 8, 5, 5, 6)],
                               0),
             st.SimpleTestCase(problem2d,
                               [(2, 3, 5, 7, 5, 3, 2)],
                               2 + 3 + 5 + 7 + 5 + 3),
             ]

    st.SimpleTestCase.run_tests('problem2d', tests)

    # ------------------------------------------------------------------
    # TODO: Add at least 2 more tests to the above list of tests.
    #       Try to choose tests that might expose errors in your code!
    # CONSIDER: Ask an assistant to CHECK your tests to confirm
    #           that they are adequate tests!
    # ------------------------------------------------------------------


def problem2d(sequence):
    """
    Returns the sum of all the items in the given sequence such that
    the item is a prime number and its immediate successor is a
    DIFFERENT prime number.

    For example:
      Given sequence (6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5)
         -- returns 17 + 3 + 7 + 13, which is 40
      Given sequence (7, 7, 7, 7, 7, 4, 4, 8, 5, 5, 6)
         -- returns 0
      Given sequence (2, 3, 5, 7, 5, 3, 2)
         -- returns 2 + 3 + 5 + 7 + 5 + 3, which is 25

    Preconditions:
      :type: sequence: (list, tuple, str)
    and the given sequence is non-empty.    """
    sum = 0
    for k in range(1, len(sequence)):
        if is_prime(sequence[k - 1]) and sequence[k - 1] != sequence[k] and is_prime(sequence[k]):
            sum = sum + sequence[k - 1]
    return sum
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #       Some tests are already written for you (above),
    #       but you are required to write ADDITIONAL tests (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the   is_prime   function define above,
    #    as appropriate.
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
