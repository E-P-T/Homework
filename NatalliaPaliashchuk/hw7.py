# Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.
class My_context_manager:
    def __init__(self, path, mode='r'):
        self.path, self.mode = path, mode
        
    def __enter__(self):
        try:
            self.file = open(self.path, self.mode)
            return self.file
        except Exception as err:
            self.__exit__(err.__class__, err.args[1], err.__traceback__)
        
        
    def __exit__(self, exception, value, trace):
        if value is None:
            self.file.close()
        else:
            raise Exception(f'{exception}, {value}, {trace}')
# Task 7.2
# Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.
from contextlib import contextmanager


@contextmanage
def my_open(path, mode='r'):
    try:
        file = open(path, mode)
        yield file 
    except Exception as err:
        pass
    finally:
        if file is not None:
            file.close()
# Task 7.3
# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
from contextlib import contextmanager
from time import time
from logging import info


@contextmanager
def timer():
    first = time()
    yield 
    second = time()
    diff = second - first
    info(diff)
# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.
from logging import info

def supr_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            info('OK')
            return result
        except Exception:
            pass
    return wrapper
# Task 7.5
# Implement function for check that number is even, at least 3. Throw different exceptions for this errors. Custom exceptions must be derived from custom base exception(not Base Exception class).
class Error(Exception): pass
    

class ArgError(Error): pass
    

def iseven(num):
    try:
        if num % 2 == 0:
            return True
        else:
            return False
    except Exception:
        raise ArgError('Bad arg')
        
# Task 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.
while True:
    ent = input()
    if 'q'== ent: break
    try:
        ent = int(ent)
    except ValueError:
        print('Enter the correct even number')
        continue
    if not iseven(ent) or ent < 4:
        print('Enter the correct even number')
        continue
    prime = []
    for i in range(2, ent):
        cnt = 0
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            prime.append(i)
    for i, val in enumerate(prime):
        for j in prime[i:]:
            if val + j == ent:
                print(val, j)
# Task 7.7
# Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections. If user tries to add a string or any non numerical object there, exception TypeError should be raised. Method init sholud be able to take either start,end,step arguments, where start - first number of collection, end - last number of collection or some ordered iterable collection (see the example). Implement following functionality:

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
class MyNumberCollection:
    def __init__(self, start, end=None, step=None):
        if end is None and step is None:
            if isinstance(start, (list, tuple)):
                if not all(isinstance(i, int) for i in start):
                    raise TypeError('MyNumberCollection supports only numbers!')
                else:
                    self.coll = list(start)
            elif isinstance(start, int):
                self.coll = [start]
            else: raise TypeError('MyNumberCollection supports only numbers!')
        else:
            if not isinstance(start, int) or  not isinstance(end, int) or not isinstance(step, int):
                raise TypeError('MyNumberCollection supports only numbers!')
            self.coll = list(range(start, end, step)) + [end]
                  
    def __iter__(self):
        self.len = len(self.coll)
        self.n = -1
        return self
    
    def __next__(self):
        if self.n < self.len - 1:
            self.n += 1
            return self.coll[self.n]
        else: raise StopIteration
        
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('MyNumberCollection supports only numbers!')
        self.coll.append(value)
        
    def __add__(self, coll):
        if not isinstance(coll, MyNumberCollection):
            raise TypeError('MyNumberCollection supports adding to MyNumberCollection!')
        return self.coll + coll.coll
    
    __radd__ = __add__
    
    def __getitem__(self, indx):
        return self.coll[indx] ** 2
    
    def __str__(self):
        return str(self.coll)
# Task 7.8
# Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through. Example:

# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25
class MySquareIterator:
    def __init__(self, coll):
        if not isinstance(coll, (list, tuple)):
            raise TypeError('Argument should be a tuple')
        self._coll = coll
    
    def __iter__(self):
        self._start = 0
        self._stop = len(self._coll)
        return self
    
    def __next__(self):
        if self._start < self._stop:
            self._start += 1
            return self._coll[self._start - 1] ** 2
        else: raise StopIteration
# Task 7.9
# Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration. If user tries to iterate after it gave all possible numbers Out of numbers! should be printed.
# Note: Do not use function range() at all Example:

# er1 = EvenRange(7,11)
# next(er1)
# >>> 8
# next(er1)
# >>> 10
# next(er1)
# >>> "Out of numbers!"
# next(er1)
# >>> "Out of numbers!"
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)
# >>> 4 6 8 10 12 "Out of numbers!"
class EvenRange:
    def __init__(self, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError
        self.start, self.end = start, end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.end:          
            if self.start % 2 != 0:
                self.start = self.start + 1
            self.start = self.start + 2
            return self.start - 2
        else:
            raise StopIteration('Out of numbers!') 
# Task 7.10
# Implement a generator which will generate odd numbers endlessly. Example:

# gen = endless_generator()
# while True:
#     print(next(gen))
# >>> 1 3 5 7 ... 128736187263 128736187265 ...
def endless_generator():
    i = -1
    while True:
        i += 2
        yield i 
# Task 7.11
# Implement a generator which will geterate Fibonacci numbers endlessly. Example:

# gen = endless_fib_generator()
# while True:
#     print(next(gen))
# >>> 1 1 2 3 5 8 13 ...
def endless_fib_generator():
    i, j = 1, 1
    yield i
    while True:
        yield i
        i, j = j + i, i