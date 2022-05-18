"""
Implement your custom collection called MyNumberCollection. It should be able to contain
only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError`
should be raised. Method init sholud be able to take either 
`start,end,step` arguments, where `start` - first number of collection,
`end` - last number of collection or some ordered iterable 
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
"""

from collections.abc import Iterable

class MyNumberCollection:
    def __init__(self, start, stop = None, step = None):
        try:
            if isinstance(start, Iterable):
                for i in start:
                    if not isinstance(i, int):
                        raise TypeError
                self.list = list(start)
                self.ind = 0 # a start index for an iterator implementation
            elif isinstance(start, int) & isinstance(stop, int) & isinstance(step, int):
                self.list = [i for i in range(start, stop, step)]
                self.list.append(stop)
                self.ind = 0 # a start index for an iterator implementation
            else:
                raise TypeError
        except TypeError:
            print("TypeError: MyNumberCollection supports only numbers!")

    def __str__(self):
        return str(self.list)

    def append (self, elem):
        try:
            if isinstance(elem, int):
                self.list.append(elem)
            else:
                raise TypeError
        except TypeError:
            print("TypeError: {} - object is not a number!".format(elem))

    def __add__(self, coll):
        result = [i for i in self.list] + [i for i in coll]
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < len(self.list):
            result = self.list[self.ind]
            self.ind += 1
            return result
        else:
            raise StopIteration
    
    def __getitem__(self, num):
        return self.list[num] ** 2

if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1,2,3,4,5))
    print(col2)
    col3 = MyNumberCollection((1,2,3,"4",5))
    col1.append(7)
    print(col1)
    col2.append("string")
    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item, end=' ')
