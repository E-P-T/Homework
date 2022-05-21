"""Implement decorator with context manager support for writing execution time to log-file.
 See contextlib module."""
import time
from contextlib import contextmanager


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@contextmanager
def executing_time():
    print("Start program!")
    start = time.time()
    yield
    end = time.time()
    print("Program ended!")
    print(f"Program is executed in {round(end - start, 5)} seconds")


if __name__ == '__main__':
    with executing_time() as exc:
        a = fibonacci(20)
        print(a)
