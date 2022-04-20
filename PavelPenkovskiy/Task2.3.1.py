""" Task 2.3.1
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
in sorted form.
Examples:
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
"""


def unique_words(words):
    return sorted(set(words))


print(unique_words(['red', 'white', 'black', 'red', 'green', 'black']))
