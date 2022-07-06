# Task 7.11


def endless_fib_generator() -> Generator[int, None, None]:
    """Infinite fibonacci numbers.

    :yield: Fibonacci number at each iteration.
    :rtype: Generator[int, None, None]
    """

    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second
