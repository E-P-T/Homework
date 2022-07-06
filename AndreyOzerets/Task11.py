# Task 7.11


from typing import Generator
from time import sleep


def endless_fib_generator() -> Generator[int, None, None]:
    """Infinite fibonacci numbers.

    :yield: Fibonacci number at each iteration.
    :rtype: Generator[int, None, None]
    """

    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second


def main():
    gen = endless_fib_generator(5)
    while True:
        print(next(gen))
        sleep(.3)


if __name__ == '__main__':
    main()
