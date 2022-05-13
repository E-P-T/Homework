#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.2 Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).')
# You can use this: Oh, it is python

start = True

while start:
    some_str = input('Type something to know the count of every character: ')

    if some_str.strip() != str():
        char_count = {}

        for char in some_str:
            char = char.lower()
            if char not in char_count:
                char_count[char] = 0

            char_count[char] += 1

        print(f'Output: {char_count}')
        start = False
    else:
        print('Please, make sure to type something')