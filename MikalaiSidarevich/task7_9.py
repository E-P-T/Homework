# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval
# as an init arguments and gives only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
# Note: Do not use function range() at all.

class EvenRange:
    """Iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
    """

    def __init__(self, start, end):
        """
        Initialize even number generator with range boundaries `start` and `end`.
        """
        self.start = start
        self.end = end
        self.gen = self.generator(start, end)

    def generator(self, start, end):
        """
        Yield even number from range [`start`, `end`].
        Yield odd number when out of range is reached.
        """
        value = start
        while True:
            if value <= end:
                if value % 2 == 0:
                    yield value
                value += 1
            else:
                yield 1

    def __iter__(self):
        self.gen = self.generator(self.start, self.end)
        return self

    def __next__(self):
        value = next(self.gen)
        return '"Out of numbers!"' if value % 2 else value


def main():
    """
    Entry point function.
    """
    er1 = EvenRange(7, 10)
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=' ')
        # There are no StopIteration, so break it manually
        if isinstance(number, str):
            break
    print()


if __name__ == '__main__':
    main()
