from collections.abc import Iterable

class CollectionTypeError(TypeError):
    def __init__(self, msg = 'MyNumberCollection supports only numbers!'):
        self.msg = msg
        
    def __str__(self):
        return self.msg
        
class CollectionConcatenationException(Exception):
    def __init__(self, msg = 'MyNumberCollection supports concatenation only for collections of numbers!'):
        self.msg = msg
        
    def __str__(self):
        return self.msg

def isNumber(value):
    if not isinstance(value, (int, float)):
        return False
    return True

class MyNumberCollection:
    def __init__(self, start = None, end = None, step = 1):
        self.collection = []
        if isinstance(start, Iterable):
            if all(map(isNumber, start)):
                self.collection.extend(start)
            else:
                raise CollectionTypeError
        elif all(map(isNumber, (start, end, step))):
            self.collection.extend(range(start, end + 1, step))
            
            if end not in self.collection:
                self.collection.append(end)

    def __str__(self):
        return '{collection}'.format(collection = self.collection)

    def append(self, number):
        if isNumber(number):
            self.collection.append(number)
        else:
            raise CollectionTypeError

    def __add__(self, other):
        result = self.collection.copy()
        if isinstance(other, MyNumberCollection):
            result.extend(other.collection)
            return MyNumberCollection(result)
        elif isinstance(other, Iterable):
            if all(map(isNumber, other)):
                result.extend(other)
                return MyNumberCollection(result)
            else:
                raise CollectionConcatenationException
        else:       
            raise CollectionConcatenationException
    
    __radd__ = __add__

    def __getitem__(self, index):
        return self.collection[index] ** 2

    def __iter__(self):
        self.index = - 1
        return self

    def __next__(self):
        if self.index < len(self.collection) - 1:
            self.index += 1
            return self.collection[self.index]
        else:
            raise StopIteration


col1 = MyNumberCollection(0, 5, 2)
print(col1)

col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2)

try:
    col3 = MyNumberCollection((1, 2, 3, "4", 5))
except CollectionTypeError as msg:
    print(msg)

col1.append(7)
print(col1)

try:
    col2.append("string")
except CollectionTypeError as msg:
    print(msg)

print(col1 + col2)
print(col1 + [1, 4, 5, 8, 9])

try:
    print(col1 + "[1, 4, 5, 8, 9]")
except CollectionConcatenationException as msg:
    print(msg)

print(col2[4])
