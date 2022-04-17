# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
#
# 1) characters that appear in all strings
#
# 2) characters that appear in at least one string
#
# 3) characters that appear at least in two strings
#
# 4) characters of alphabet, that were not used in any string
#
# Note: use `string.ascii_lowercase` for list of alphabet letters
#
# ```python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
# ```


def test_1_1(*strings):
    lst = list()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        flag = 1
        for string in strings:
            if char not in string:
                flag = 0
        if flag == 1:
            lst.append(char)
    return lst


def test_1_2(*strings):
    lst = list()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        flag = 0
        for string in strings:
            if char in string:
                flag = 1
        if flag == 1:
            lst.append(char)
    return lst


def test_1_3(*strings):
    lst = list()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        flag = 0
        for string in strings:
            if char in string:
                flag += 1
        if flag >= 2:
            lst.append(char)
    return lst


def test_1_4(*strings):
    lst = list()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        flag = 0
        for string in strings:
            if char in string:
                flag = 1
        if flag == 0:
            lst.append(char)
    return lst
