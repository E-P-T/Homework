"""Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives
only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
_Note: Do not use function `range()` at all_"""


class EvenRange:
    def __init__(self, start, end):
        self.end = end
        if start % 2 == 0:
            self.start = start
        else:
            self.start = start + 1
        self._range = []
        i = self.start
        while i <= self.end:
            self._range.append(i)
            i += 2

    def __iter__(self):
        for i in self._range:
            yield i

    def __next__(self):
        res = self.start
        self.start += 2
        if res <= self.end:
            return res
        else:
            return "Out of numbers!"


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    print(next(er1))
    print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
