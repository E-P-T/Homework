# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives
# only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
# _Note: Do not use function `range()` at all_

class EvenRange:
    """An iterator class which accepts start and end of the interval and gives only even numbers during iteration.
    """
    def __init__(self, start: int, end: int):
        self.end = end
        self.index = start - 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index % 2:
            self.index += 1
        if self.index + 2 < self.end:
            self.index += 2
            return self.index
        else:
            print('"Out of numbers!"')
            raise StopIteration


if __name__ == '__main__':
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=' ')
    # # >>> 4 6 8 10 12 "Out of numbers!"
    er1 = EvenRange(7, 11)
    print(next(er1))
    # >>> 8
    print(next(er1))
    # >>> 10
    print(next(er1))
    # >>> "Out of numbers!"


