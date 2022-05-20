# ### Task 7.7
# TODO:Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should
#  NOT inherit any other collections. If user tries to add a string or any non numerical object there, exception
#  `TypeError` should be raised. Method init should be able to take either `start,end,step` arguments, where `start` -
#  first number of collection, `end` - last number of collection or some ordered iterable collection (see the example).
### Implement following functionality:
# TODO:* appending new element to the end of collection
# TODO:* concatenating collections together using `+`
# TODO:* when element is addressed by index(using `[]`), user should get square of the addressed element.
# TODO:* when iterated using cycle `for`, elements should be given normally
# TODO:* user should be able to print whole collection as if it was list.
from typing import Iterable


class MyNumberCollection:
    def __init__(self, *args):
        try:
            if isinstance(args, Iterable):
                if len(args) == 1:
                    for _ in args[0]:
                        if not isinstance(_, int):
                            raise TypeError
                else:
                    for _ in args:
                        if not isinstance(_, int):
                            raise TypeError("Bad arguments")
        except TypeError:
            print('TypeError: MyNumberCollection supports only numbers!')
        else:
            if len(args) == 1:
                self._data = args[0]
            else:
                self._data = [n for n in range(args[0], args[1], args[2])]
                self._data.append(args[1])

    def __iter__(self):
        for elem in self._data:
            yield elem

    def __getitem__(self, item):
        return self._data[item] ** 2

    def __repr__(self):
        return str(list(self))

    def append(self, new_item):
        try:
            if not isinstance(new_item, int):
                raise TypeError(f"TypeError: '{new_item}' - object is not a number!")
            else:
                self._data.append(new_item)
        except TypeError as e:
            print(e)

    def __add__(self, other):
        return self._data + list(other)

# a = MyNumberCollection(0, 14, 2)
#
# print(a)
# print(a[6])
# for item in a:
#     print(item)

# Example:
# ```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
# >>> [0, 2, 4, 5]
col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)
# >>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
# >>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
# >>> [0, 2, 4, 5, 7]
col2.append("string")
# >>> TypeError: 'string' - object is not a number!
print(col1 + col2)
# >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
# >>> [0, 2, 4, 5, 7]
print(col2)
# >>> [1, 2, 3, 4, 5]
print(col2[4])
# >>> 25
for item in col1:
    print(item, end=' ')
# >>> 0 2 4 5 7
# ```
