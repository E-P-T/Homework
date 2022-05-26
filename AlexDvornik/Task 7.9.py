"""
Task 7.9
Implement an iterator class EvenRange, which accepts start and end of the interval
as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
Note: Do not use function `range()` at all
"""


class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if self.start % 2 == 0:
            self.n = self.start + 2
        else:
            self.n = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.end:
            result = self.n
            self.n += 2
        else:
            print("Out of numbers!")
            raise StopIteration
        return result

er1 = EvenRange(5, 11)
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    print(number, end=' ')
