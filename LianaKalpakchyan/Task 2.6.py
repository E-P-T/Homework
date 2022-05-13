#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.6 Write a Python program to convert a given tuple of positive integers into an integer.')

some_tuple = (1, 2, 3, 4)

some_str = ''

for i in some_tuple:
    some_str += str(i)

integer = int(some_str)

print(f'The result is : {integer}')
