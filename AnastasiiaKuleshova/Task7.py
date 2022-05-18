# Task 7.7
# Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
# It should NOT inherit any other collections. If user tries to add a string or any non numerical object there,
# exception TypeError should be raised. Method init sholud be able to take either start,end,step arguments,
# where start - first number of collection, end - last number of collection or some ordered iterable collection
# (see the example). Implement following functionality:
#
# appending new element to the end of collection
# concatenating collections together using +
# when element is addressed by index(using []), user should get square of the addressed element.
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
from typing import Iterable


class MyNumberCollection(object):

    def __init__(self, *params):
        self.my_collection = []
        self.pos = 0

        if len(params) == 3:
            self.const_three_params(params[0], params[1], params[2])
        if len(params) == 1:
            self.const_tuple(params[0])

    def const_three_params(self, start, end, step):
        self.__validate_input(start, end, step)
        for i in range(start, end, step):
            self.my_collection.append(i)

    def const_tuple(self, input_tuple):
        self.__validate_input(*input_tuple)
        for i in input_tuple:
            self.my_collection.append(i)

    def append(self, appendable):
        if isinstance(appendable, Iterable):
            self.__validate_input(*appendable)
            self.my_collection += appendable
        else:
            self.__validate_input(appendable)
            self.my_collection.append(appendable)

    @staticmethod
    def __validate_input(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError(i, ' object is not a number')

    def __str__(self):
        return str(self.my_collection)

    def __add__(self, other):
        if not isinstance(other, MyNumberCollection):
            raise NotImplementedError
        return self.my_collection + other.my_collection

    def __iter__(self):
        return iter(self.my_collection)

    def __next__(self):
        if self.pos < len(self.my_collection):
            to_be_returned = self.pos
            self.pos += 1
            return self.my_collection[to_be_returned]
        raise StopIteration

    def __getitem__(self, item):
        return self.my_collection[item]


col1 = MyNumberCollection(0, 5, 'as')
col2 = MyNumberCollection((1, 2, 3, 4, 5))

col1.append(7)


print(col1)