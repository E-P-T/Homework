# Task 7.7 Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It
# should NOT inherit any other collections. If user tries to add a string or any non numerical object there,
# exception `TypeError` should be raised. Method init sholud be able to take either `start,end,step` arguments,
# where `start` - first number of collection, `end` - last number of collection or some ordered iterable collection (
# see the example). Implement following functionality: * appending new element to the end of collection *
# concatenating collections together using `+` * when element is addressed by index(using `[]`), user should get
# square of the addressed element. * when iterated using cycle `for`, elements should be given normally * user should
# be able to print whole collection as if it was list.
from decimal import Decimal
from fractions import Fraction
from collections.abc import Iterable


class MyNumberCollection:
    """custom collection that is able to contain only numbers.
    Method init takes either start,end,step` arguments, where `start` - first number of collection, `end` - last number
    of collection, or some ordered iterable collection.
    Implemented functionality:
    * appending new element to the end of collection
    * concatenating collections together using `+`
    * when element is addressed by index(using `[]`), user gets square of the addressed element.
    * when iterated using cycle `for`, elements are given normally
    * user is able to print whole collection as if it was list."""

    @staticmethod
    def check_value(value: int) -> bool:
        return isinstance(value, (int, float, Decimal, complex, Fraction))

    def __init__(self, start=None, end=None, step=1):
        self.data = []
        if isinstance(start, Iterable):
            if all(map(MyNumberCollection.check_value, start)):
                self.data.extend(start)
            else:
                raise TypeError('MyNumberCollection supports only numbers!')
        elif all(map(MyNumberCollection.check_value, (start, end, step))):
            self.data.extend(range(start, end + 1, step))
            if end not in self.data:
                self.data.append(end)

    def __str__(self):
        return f'{self.data}'

    def append(self, number):
        if MyNumberCollection.check_value(number):
            self.data.append(number)
        else:
            raise TypeError('MyNumberCollection supports only numbers!')

    def __add__(self, other):
        self.result = self.data.copy()
        if isinstance(other, MyNumberCollection):
            self.result.extend(other.data)
            return self.result
        elif isinstance(other, Iterable):
            if all(map(MyNumberCollection.check_value, other)):
                self.result.extend(other)
                return self.result
            else:
                raise TypeError('MyNumberCollection supports concatenation only for collections of numbers!')
        else:
            raise TypeError('MyNumberCollection supports concatenation only for collections of numbers!')

    __radd__ = __add__

    def __getitem__(self, index):
        return self.data[index] ** 2

    def __iter__(self):
        self.index = - 1
        return self

    def __next__(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return self.data[self.index]
        else:
            raise StopIteration


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    # >>> [0, 2, 4, 5]
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # >>> [1, 2, 3, 4, 5]
    try:
        col3 = MyNumberCollection((1, 2, 3, "4", 5))
    except TypeError as message:
        print(message)
    col1.append(7)
    print(col1)
    # >>> [0, 2, 4, 5, 7]
    try:
        col2.append("string")
    except TypeError as message:
        print(message)
    print(col1 + col2)
    # >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
    print(col1 + [1, 4, 5, 8, 9])
    # >>> [0, 2, 4, 5, 7, 1, 4, 5, 8, 9]
    try:
        print(col1 + "[1, 4, 5, 8, 9]")
    except TypeError as message:
        print(message)
    print(col1)
    # >>> [0, 2, 4, 5, 7]
    print(col2)
    # >>> [1, 2, 3, 4, 5]
    print(col2[4])
    # >>> 25
    for item in col1:
        print(item, end=" ")
    # >>> 0 2 4 5 7
