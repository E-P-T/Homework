#! /usr/bin/env python
# TODO: Implement a function get_longest_word(s: str) -> str which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words
# in the string with a same length return the word that occures first.
# Example:
# >>> python
# >>> get_longest_word('Python is simple and effective!')
# 'effective!'
# >>> get_longest_word('Any pythonista like namespaces a lot.')
# 'pythonista'


"""
task_6.py: implemented functions, which return the longest word in a string.
Also contains some speed tests for these functions.
"""


import timeit
from numpy import average as avg


def get_longest_word(string):
    """
    get_longest_word: returns the longest word in a string.
    """
    words = string.split()
    lengths = [len(word) for word in words]
    return words[lengths.index(max(lengths))]


def get_longest_word2(string):
    """
    get_longest_word2: returns the longest word in a string.
    """
    words = string.split()
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


if __name__ == '__main__':
    print(get_longest_word('Python is simple and effective!'))
    # Result: effective!
    print(get_longest_word('Any pythonista like namespaces a lot.'))
    # Result: pythonista

    result = timeit.repeat(
        stmt="get_longest_word('Python is simple and effective!')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0007932090000394964

    result = timeit.repeat(
        stmt="get_longest_word2('Python is simple and effective!')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0008469418001368467

    # As usual built-in instruments is better then own implementation.
