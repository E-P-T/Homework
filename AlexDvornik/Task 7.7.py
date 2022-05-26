"""
Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
It should NOT inherit any other collections. If user tries to add a string or any nonnumerical object there, exception
`TypeError` should be raised. Method init should be able to take either `start,end,step` arguments, where `start` -
first number of collection, `end` - last number of collection or some ordered iterable collection (see the example).

Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
"""

from collections.abc import Iterable


class MyNumberCollection:
    def __init__(self, start, end=None, step=1):
        try:
            if isinstance(start, int) and isinstance(end, int):
                self.arg = [i for i in range(start, end, step)]
                self.arg.append(end)
            elif isinstance(start, Iterable):
                for item in start:
                    if isinstance(item, str):
                        raise TypeError
                self.arg = list(start)
            else:
                raise TypeError
        except TypeError:
            print(f"Type Error: MyNumberCollection supports only numbers!")

    def __str__(self):
        return f"{self.arg}"

    def append(self, item):
        try:
            if isinstance(item, int) or isinstance(item, float):
                self.arg.append(item)
            else:
                raise TypeError
        except TypeError:
            print(f"TypeError: {item} - object is not a number!")

    def __add__(self, other):
        return [*self.arg, *other]

    def __getitem__(self, item):
        return self.arg[item]


col1 = MyNumberCollection(0, 5)
print(col1)
col1.append(2)
print(col1)
print(col1[2])

col2 = MyNumberCollection((1, 2, 3, 4))
print(col1 + col2)

for i in col2:
    print(i, end=' ')

