# Task 7.4

from contextlib import ContextDecorator
from time import time


class SupressDecorator(ContextDecorator):
    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def __enter__(self):
        print('Starting')
        self._start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _stop = str(time() - self._start)
        message = f'Execution time is {_stop}'
        if exc_type:
            with open(self._file, 'w') as f:
                f.write(message)
        else:
            print(message)

        print('Finishing')
        return True
