'''
Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters

test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
{'o'}
print(test_1_2(*strings))
{'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
{'h', 'l', 'o'}
print(test_1_4(*strings))
{'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
'''
import string
from collections import Counter
from itertools import chain


def test_1_1(*strings):
    return set.intersection(*map(set, *strings))


def test_1_2(*strings):
    set_of_char = set()
    for word in strings[0]:
        for char in word:
            if char not in set_of_char:
                set_of_char.add(char)
    return set_of_char


def test_1_3(*strings):
    counter = Counter(chain.from_iterable(set(*strings)))
    return {char for char, count in counter.items() if count >= 2}


def test_1_4(*strings):
    alphabet = string.ascii_lowercase
    set_of_chars = set(''.join(*strings))
    return set(alphabet).difference(set_of_chars)


bunch_of_functions = [test_1_1,
                      test_1_2,
                      test_1_3,
                      test_1_4,
                      ]

for func in bunch_of_functions:
    test_strings = ["hello", "world", "python", ]
    print(func(test_strings))
