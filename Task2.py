# Task 7.2
from contextlib import contextmanager
import sys
import traceback


@contextmanager
def my_open(file, mode='r'):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()


def _print_ex():
    """Print traceback"""
    *_, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)


if __name__ == '__main__':

    try:
        with my_open('a.txt', 'w') as mo:
            mo.write('OK')
    except FileNotFoundError as e:
        _print_ex()
        print(f'\n*** Is the filename correct?: {e}', end='\n\n')
        raise SystemExit
    except ValueError as e:
        _print_ex()
        print(f'\n*** Is the mode correct?: {e}', end='\n\n')
        raise SystemExit
