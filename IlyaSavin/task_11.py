#! /usr/bin/env python
# TODO: Implement a generator which will geterate Fibonacci numbers endlessly.
# Example: 1 1 2 3 5 8 13 ...


"""
task_11.py: Implemented a generator which will geterate Fibonacci numbers
endlessly and some test statements.
"""


import time


def endless_fib_generator():
    """
    endless_fib_generator: Generator which will geterate Fibonacci numbers
    endlessly.
    """
    first, second = -1, 0
    while True:
        yield abs(first + second)
        first, second = second, first + second


if __name__ == '__main__':
    gen = endless_fib_generator()
    while True:
        print(next(gen))
        time.sleep(1)
