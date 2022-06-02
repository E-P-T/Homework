# Task 7.11
# Implement a generator which will geterate Fibonacci numbers endlessly.

from time import sleep


def endless_fib_generator():
    """
    Yield Fibonacci numbers endlessly.
    """
    # Yield init values
    prev1 = 1
    prev2 = 1
    yield prev1
    yield prev2

    # Yield next value
    while True:
        current = prev1 + prev2
        prev1, prev2 = prev2, current
        yield current


def main():
    """
    Entry point function.
    """
    gen = endless_fib_generator()
    while True:
        print(next(gen))
        sleep(0.1)


if __name__ == '__main__':
    main()
