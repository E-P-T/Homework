# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval as an
# init arguments and gives only even numbers during iteration. If user tries to iterate after it
# gave all possible numbers Out of numbers! should be printed.
# Note: Do not use function range() at all Example:
#
# er1 = EvenRange(7,11)
# next(er1)
# >>> 8
# next(er1)
# >>> 10
# next(er1)
# >>> "Out of numbers!"
# next(er1)
# >>> "Out of numbers!"
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)
# >>> 4 6 8 10 12 "Out of numbers!"

class EvenRange:

    def __init__(self, start, stop):
        try:
            if isinstance(start, int) and isinstance(stop, int):
                if start % 2 == 0:
                    self.current = start
                else:
                    self.current = start + 1
                self.last_num = stop
            else:
                raise TypeError
        except TypeError:
            print("input must be integers")

    def __iter__(self):
        return self

    def __next__(self):

        try:

            if self.current <= self.last_num:
                to_be_returned = self.current
                self.current += 2
                return to_be_returned
            raise StopIteration

        except StopIteration:
            print("out of numbers")
            raise StopIteration


er1 = EvenRange(7, 11)
for number in er1:
    print(number)
