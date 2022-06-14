#! /usr/bin/env python
# TODO: Implement a generator which will generate odd numbers endlessly.
# Example: 1 3 5 7 ... 128736187263 128736187265 ...


"""
task_10.py: Implemented a generator which will generate odd numbers endlessly
and some test statements.
"""


import time


def endless_generator():
    """
    endless_generator: Generator which will generate odd numbers endlessly.
    """
    i = 1
    while True:
        yield i
        i += 2


if __name__ == '__main__':
    gen = endless_generator()
    while True:
        print(next(gen))
        time.sleep(1)
