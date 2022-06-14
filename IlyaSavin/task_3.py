#! /usr/bin/env python
# TODO: Implement decorator with context manager support for writing execution
#  time to log-file. See contextlib module.


"""
task_3.py: Implemented decorator with context manager support for writing
execution time to log-file. See contextlib module and some test statements.
"""


import sys
import time
from contextlib import ContextDecorator


timer = time.clock if sys.platform[:3] == 'win' else time.time


class ExecuteTime(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, exception, value, trace):
        self.end = timer() - self.start
        with open(self.filename, 'a+') as logfile:
            logfile.write('Time of performing: %s\n' % self.end)


@ExecuteTime('task3_logfile.txt')
def test():
    for i in range(10000):
        a = 2 ** 100
        b = [1, 2, 3, 4]
        c = [x ** 2 for x in b]


if __name__ == '__main__':
    test()
