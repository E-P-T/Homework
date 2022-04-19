# Task 2.2
'''Write a Python program to count the number of characters to count the number of characters
(character frequency) in a string (ignore case of letters).
Examples:
Input: 'Oh, it is python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}'''


def count_the_number(s):
    frequency = {}
    s_lower = s.lower()
    for c in s_lower:
        frequency[c] = frequency.get(c, 0) + 1
    return frequency


print(count_the_number("Oh, it is python"))
