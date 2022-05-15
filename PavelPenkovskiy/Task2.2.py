""" Task 2.2 Write a Python program to count the number of characters (character frequency) in a string
(ignore case of letters).
Examples:
Input: 'Oh, it is python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
"""


def number_of_characters(string):
    result = dict()
    characters = set(string.lower())
    for c in characters:
        result[c] = string.lower().count(c)
    return result


print(number_of_characters('Oh, it is python'))
