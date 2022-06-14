#! /usr/bin/env python
# TODO: Implement decorator for suppressing exceptions.
# If exception not occure write log to console.


"""
task_4.py: Implemented decorator for suppressing exceptions and test statements
"""


from contextlib import ContextDecorator


class Suppress(ContextDecorator):
    """
    Suppress: Decorator for suppressing exceptions.
    """
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exception, value, trace):
        if exception in self.exceptions:
            print(value)
            return True
        elif exception is None:
            print('No exceptions was occured.')


@Suppress(ZeroDivisionError, AttributeError)
def test():
    first = 1 + 1
    second = 1 / 0
    third = [1, 2, 3].deleteall()


if __name__ == '__main__':
    test()
