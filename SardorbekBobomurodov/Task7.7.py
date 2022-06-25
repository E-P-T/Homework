# TODO Implement your custom collection called MyNumberCollection.
#  It should be able to contain only numbers. It should NOT inherit any other collections.

from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction

CHECK_FORMAT = int | float | complex | Decimal | Fraction


class MyNumberCollection:
    def __init__(self, start=0, end=10, step=1):
        if not isinstance(start, Iterable):
            if not all(isinstance(x, CHECK_FORMAT) for x in (start, end, step)):
                raise TypeError("Wrong Format!")
            self.collection = [x for x in range(start, end, step)] + [end]
        else:
            if not all(isinstance(x, CHECK_FORMAT) for x in (start, end, step)):
                raise TypeError("Wrong Format!")
            self.collection = list(start)

    def append(self, num):
        if not isinstance(num, CHECK_FORMAT):
            raise TypeError("Wrong Format")
        self.collection.append(num)

    def __add__(self, other):
        return MyNumberCollection(self.collection + other)

    def __getitem__(self, item):
        return self.collection[item] ** 2

    def __iter__(self):
        yield from self.collection

    def __str__(self):
        return str(self.collection)


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1[2])
    for item in col1:
        print(item, end=' ')
    print()

