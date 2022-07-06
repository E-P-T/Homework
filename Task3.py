# Task 7.3
from contextlib import ContextDecorator


class ExecutionTimeToLogFile(ContextDecorator):
    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def __enter__(self):
        print('Starting')
        self._start = time()
        return self
