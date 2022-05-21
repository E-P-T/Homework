"""Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised. Method init sholud be able to take either
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection or some ordered iterable
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list."""
from collections.abc import Iterable


class MyNumberCollection:
    def __init__(self, start, end=None, step=None):
        try:
            self.collection = []
            if isinstance(start, Iterable):
                for char in start:
                    if isinstance(char, int):
                        self.collection.append(char)
                    else:
                        raise TypeError
            elif all([isinstance(start, int), isinstance(end, int), isinstance(step, int)]):
                for i in range(start, end, step):
                    self.collection.append(i)
                self.collection.append(end)
        except TypeError:
            print("TypeError: MyNumberCollection supports only numbers!")

    def __str__(self):
        return str(self.collection)

    def __add__(self, other):
        return self.collection + other.collection

    def append(self, char):
        try:
            if isinstance(char, int):
                self.collection.append(char)
            else:
                raise TypeError
        except TypeError:
            print(f"TypeError: '{char}' - object is not a number!")

    def __getitem__(self, item):
        return self.collection[item] ** 2

    def __iter__(self):
        for c in range(len(self.collection)):
            yield self.collection[c]


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    col3 = MyNumberCollection((1, 2, 3, "4", 5))
    print(col1 + col2)
    print(col1)
    print(col2)
    col2.append("string")
    print(col2[3])
    for it in col2:
        print(it, end=" ")

