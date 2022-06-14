#! /usr/bin/env python
# TODO: Implement an iterator class EvenRange, which accepts start and end
# of the interval as an init arguments and gives only even numbers during
# iteration. If user tries to iterate after it gave all possible numbers
# Out of numbers! should be printed.
# Note: Do not use function range() at all Example:
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


"""
task_9.py: Implemented an iterator class EvenRange, which accepts start and end
of the interval as an init arguments and gives only even numbers during
iteration and some test statements.
"""


class EvenRange:
    """
    EvenRange: class, which accepts start and end of the interval as an init
    arguments and gives only even numbers during iteration.
    """
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current % 2 != 0:
            self.current += 1
        else:
            self.current += 2

        if self.current < self.end:
            return self.current
        else:
            print('Out of numbers')
            raise StopIteration


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    # print(next(er1))
    # print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
