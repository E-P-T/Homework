"""
Task 7.5
Implement function for check that number is even, at least 3. Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""
from exceptions import *


def is_even(number: int):
    try:
        if isinstance(number, int):
            print(bool(number % 2 == 0))
        else:
            if isinstance(number, float):
                raise WrongTypeOfArgumentFloat
            else:
                raise WrongTypeOfArgument
    except CustomException as ex:
        print(ex)


if __name__ == '__main__':
    a = '2'
    b = 3
    c = 0.2
    is_even(b)

