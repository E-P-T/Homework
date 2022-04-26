# Task 4.9

import re
import string


def all_chars(*s):
    result = ''
    for i in s:
        result += i
    return set(re.sub('[^a-zA-Z_]', '', result).lower())


def test_1_1(*s):
    result = list(all_chars(s[0]))
    for char in all_chars(s[0]):
        for i in s:
            if char not in all_chars(i):
                result.remove(char)
                break
    return set(result)


def test_1_2(*s):
    return all_chars(*s)


def test_1_3(*s):
    result = []
    for i in s:
        others = list(s)
        others.remove(i)
        [result.append(i) for i in all_chars(i) if i in all_chars(*others)]
        return set(result)


def test_1_4(*s):
    result = list(string.ascii_lowercase)
    for i in all_chars(*s):
        result.remove(i)
    return set(result)


strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
print(test_1_2(*strings))
print(test_1_3(*strings))
print(test_1_4(*strings))
