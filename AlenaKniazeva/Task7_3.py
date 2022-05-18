"""
Implement decorator with context manager support for writing execution time to log-file.
"""

from contextlib import contextmanager
from time import time


@contextmanager
def execut_time():
    start = time()
    yield
    end = time() - start
    print("The execution time is: {}".format(round(end,7)))

def main():
    with execut_time():
        s = [x for x in range(1000000)]

if __name__ == '__main__':
    main()