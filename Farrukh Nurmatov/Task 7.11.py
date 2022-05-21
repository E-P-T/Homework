"""Implement a generator which will geterate [Fibonacci numbers] endlessly."""
import time


def endless_fib_generator():
    a, b = 0, 1
    while True:
        time.sleep(1)
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    gen = endless_fib_generator()
    while True:
        print(next(gen))
