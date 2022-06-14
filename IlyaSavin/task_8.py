#! /usr/bin/env python
# TODO: Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through. Example:
# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25


"""
task_8.py: Implemented your custom iterator class called MySquareIterator
which gives squares of elements of collection it iterates through and some test
statements.
"""


class MySquareIterator:
    """
    MySquareIterator: Class, which gives squares of elements of collection
    it iterates through.
    """
    def __init__(self, collection):
        self.collection = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.collection) ** 2


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=' ')
    print()
