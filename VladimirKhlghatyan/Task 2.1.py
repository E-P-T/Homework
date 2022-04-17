# Task 2.1
# Write a Python program to calculate the length of a string without using the `len` function.


def str_len(string):
    length = 0
    for _ in string:
        length += 1
    return length
