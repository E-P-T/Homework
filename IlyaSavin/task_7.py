#! /usr/bin/env python
# TODO: Implement your custom collection called MyNumberCollection.
# It should be able to contain only numbers. It should NOT inherit any other
# collections. If user tries to add a string or any non numerical object there,
# exception TypeError should be raised. Method init sholud be able to take
# either start,end,step arguments, where start - first number of collection,
# end - last number of collection or some ordered iterable collection
# (see the example). Implement following functionality:
# appending new element to the end of collection
# concatenating collections together using + when element is addressed by
# index(using []), user should get square of the addressed element.
# when iterated using cycle for, elements should be given normally
# user should be able to print whole collection as if it was list. Example:
# col1 = MyNumberCollection(0, 5, 2)
# print(col1)
# >>> [0, 2, 4, 5]
# col2 = MyNumberCollection((1,2,3,4,5))
# print(col2)
# >>> [1, 2, 3, 4, 5]
# col3 = MyNumberCollection((1,2,3,"4",5))
# >>> TypeError: MyNumberCollection supports only numbers!
# col1.append(7)
# print(col1)
# >>> [0, 2, 4, 5, 7]
# col2.append("string")
# >>> TypeError: 'string' - object is not a number!
# print(col1 + col2)
# >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
# print(col1)
# >>> [0, 2, 4, 5, 7]
# print(col2)
# >>> [1, 2, 3, 4, 5]
# print(col2[4])
# >>> 25
# for item in col1:
#     print(item)
# >>> 0 2 4 5 7


"""
task_7.py: Implemented custom collection called MyNumberCollection and some
test statements.
"""


from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction


NUMERIC = int | float | complex | Decimal | Fraction


class MyNumberCollection:
    """
    MyNumberCollection: Custom collection, which contains only number and
    defines serveral methods for working with numbers.
    """
    def __init__(self, start=0, end=10, step=1):
        if not isinstance(start, Iterable):
            if not all(isinstance(x, NUMERIC) for x in (start, end, step)):
                raise TypeError('MyNumberCollection supports only numbers!')
            self.collection = [i for i in range(start, end, step)] + [end]
        else:
            if not all(isinstance(x, NUMERIC) for x in start):
                raise TypeError('MyNumberCollection supports only numbers!')
            self.collection = list(start)

    def append(self, number):
        if not isinstance(number, NUMERIC):
            raise TypeError(repr(number) + ' object is not a number!')
        self.collection.append(number)

    def __add__(self, collection):
        return MyNumberCollection(self.collection + list(collection))

    def __getitem__(self, index):
        return self.collection[index] ** 2

    def __iter__(self):
        yield from self.collection

    def __str__(self):
        return str(self.collection)


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)  # Result: [0, 2, 4, 5]
    col2 = MyNumberCollection((1, 2, 3.5, 4+2j, 5))
    print(col2)  # Result: [1, 2, 3.5, (4+2j), 5]
    # col3 = MyNumberCollection((1, 2, 3, "4", 5))
    # Result: TypeError: MyNumberCollection supports only numbers!
    col1.append(7)
    print(col1)  # Result: [0, 2, 4, 5, 7]
    # col2.append("string")
    # Result: TypeError: 'string' - object is not a number!
    print(col1 + col2)  # Result: [0, 2, 4, 5, 7, 1, 2, 3.5, (4+2j), 5]
    print(col1)  # Result: [0, 2, 4, 5, 7]
    print(col2)  # Result: [1, 2, 3.5, (4+2j), 5]
    print(col2[4])  # Result: 25
    for item in col1:
        print(item, end=' ')
    # Result: 0 2 4 5 7
    print()
