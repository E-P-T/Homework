#! /usr/bin/env python
# TODO: Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 7.5 for
# validating input, handle all exceptions and print user friendly output.


"""
task_6.py: Created console program for proving Goldbach's conjecture
and some test statements.
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


def gen_primes(number):
    """
    primes: Returns list of primes before number.
    """
    if isinstance(number, bool | float | complex):
        raise NotIntegerException('number must be integer')
    elif not isinstance(number, int):
        raise NotANumberException('number must be integer')

    return [i for i in range(2, number) if all(i % j for j in range(2, i))]


def goldbach(number):
    """
    goldbach: return list of all combinations of primes, which in sum give
    number.
    """
    if is_even(number) and number >= 4:
        primes = gen_primes(number)
        return [(x, y) for x in primes for y in primes if x + y == number]
    else:
        raise ValueError('Not even number')


if __name__ == '__main__':
    while ((number := input('>>> ')) != 'q'):
        print(goldbach(int(number)))
