""" Task 2.6
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
Input: (1, 2, 3, 4)
Output: 1234
"""


def tuple_to_integer(t):
    t = list(t)
    t = [str(i) for i in t]
    return int(''.join(t))


print(tuple_to_integer((1, 2, 3, 4)))
