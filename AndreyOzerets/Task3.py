# Task 7.3
from contextlib import ContextDecorator
from time import sleep, time


class ExecutionTimeToLogFile(ContextDecorator):
    """Decorator with context manager

    Support for writing execution time to log-file.
    """

    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def __enter__(self):
        print('Starting')
        self._start = time()
        return self

    def __exit__(self, *exc):
        _stop = str(time() - self._start)
        with open(self._file, 'w') as f:
            f.write(f'Execution time is {_stop}')
        print('Finishing')


@ExecutionTimeToLogFile('log-file.txt')
def fun():
    """Something very important"""

    for _ in range(50):
        sleep(0.01)


if __name__ == '__main__':
    fun()
