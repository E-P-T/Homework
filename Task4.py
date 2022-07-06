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
