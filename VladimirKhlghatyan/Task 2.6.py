# Task 2.6
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```


def convert_tuple_to_int(tpl):
    num = 0
    for item in tpl:
        num = num * 10 + item
    return num
