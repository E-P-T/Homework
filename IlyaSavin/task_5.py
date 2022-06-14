#! /usr/bin/env python
# TODO: Implement function for check that number is even, at least 3.
# Throw different exceptions for this errors. Custom exceptions must be derived
# from custom base exception(not Base Exception class).


"""
task_5.py: Implemented function for check that number is even, at least 3.
Throwed different exceptions for this errors. Also contains some test
statements.
"""


class MyException(Exception):
    pass


class NotIntegerException(MyException):
    pass


class NotANumberException(MyException):
    pass


def is_even(number):
    """
    is_even: Returns True if number is even otherwise returns False.
    """
    if isinstance(number, bool | float | complex):
        raise NotIntegerException('number must be integer')
    elif not isinstance(number, int):
        raise NotANumberException('number must be integer')
    return number % 2 == 0


if __name__ == '__main__':
    print(is_even(3))  # Result: False
    print(is_even(0))  # Result: True
    print(is_even(4))  # Result: True
    print(is_even(11))  # Result: False
    # print(is_even(11.5))  # Result: NotIntegerException
    # print(is_even(2+3j))  # Result: NotIntegerException
    # print(is_even(True))  # Result: NotIntegerException
    # print(is_even('12'))  # Result: NotANumberException
    # print(is_even([1, 2, 3]))  # Result: NotANumberException
