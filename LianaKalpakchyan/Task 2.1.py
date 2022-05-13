#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.1 Write a Python program to calculate the length of a string without using the len function.')

start = True

while start:
    some_str = input('Type something to know its length: ')

    if some_str.strip() != str():
        len_str = 0

        for char in some_str:
            len_str += 1

        print(f'The length of the "{some_str}" is {len_str}')
        start = False
    else:
        print('Please, make sure to type something')