### Task 7.9
# TODO: Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and
#  gives only even numbers during iteration. If user tries to iterate after it gave all possible numbers
#  `Out of numbers!` should be printed.   _Note: Do not use function `range()` at all_

class EvenRange:
    def __init__(self, start, end):
        i = start
        self.current_index = 0
        self._data = []
        while i <= end:
            if not i % 2:
                self._data.append(i)
            i += 1

    def __iter__(self):
        for item in self._data:
            yield item
        yield '"Out of numbers!"'

    def __next__(self):
        if self.current_index < len(self._data):
            x = self._data[self.current_index]
            self.current_index += 1
            return print(x)
        else:
            print('"Out of numbers!"')


er1 = EvenRange(7, 11)
next(er1)
# >>> 8
next(er1)
# >>> 10
next(er1)
# >>> "Out of numbers!"
next(er1)
# >>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number, end=' ')
# >>> 4 6 8 10 12 "Out of numbers!"
