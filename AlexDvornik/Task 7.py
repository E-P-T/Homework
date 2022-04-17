"""
Task 2.7
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
Input: (1, 2, 3, 4)
Output: 1234
"""

sample_tuple = tuple(i for i in range(1, int(input()) + 1))
print(int(''.join(map(str, sample_tuple))))
