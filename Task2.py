# Task 7.2
from contextlib import contextmanager


@contextmanager
def my_open(file, mode='r'):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()
