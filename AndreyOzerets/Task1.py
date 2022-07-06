# Task 7.1
import sys
import traceback


class MyOpen:
    def __init__(self, file, mode='r') -> None:
        self._file = file
        self._mode = mode
        self._file_obj = None

    def __enter__(self):
        self._file_obj = open(self._file, self._mode)
        return self._file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file_obj.close()


def _print_ex():
    """Print traceback"""
    *_, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)


if __name__ == '__main__':
    try:
        with MyOpen('d.txt', 'r') as mo:
            mo.write('OK')
    except FileNotFoundError as e:
        _print_ex()
        print(f'\n*** Is the filename correct?: {e}', end='\n\n')
        raise SystemExit
    except ValueError as e:
        _print_ex()
        print(f'\n*** Is the mode correct?: {e}', end='\n\n')
        raise SystemExit
