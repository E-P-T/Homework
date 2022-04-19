# Task 2.1
''' Write a Python program to calculate the length of a string without using the `len` function.'''

s = "Hello World"
length = 0
for _ in s:
    length += 1
print(length)
