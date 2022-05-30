# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}


import string
alphabet = string.ascii_lowercase


def test_1_1(*args):
    result_1 = []
    for i in alphabet:
        character_appear_in_all_strings = True
        for j in list(*args):
            if i not in j:
                character_appear_in_all_strings = False
        if character_appear_in_all_strings:
            result_1.append(i)
    return set(result_1)


def test_1_2(*args):
    result_2 = []
    characters = ''.join(list(*args))
    for i in characters:
        if characters.count(i) == 1:
            result_2.append(i)
    return set(result_2)


def test_1_3(*args):
    result_3 = []
    for a in alphabet:
        count_a = 0
        for s in list(*args):
            if a in s:
                count_a += 1
        if count_a == 2:
            result_3.append(a)
    return set(result_3)


def test_1_4(*args):
    result_4 = []
    for a in alphabet:
        count_a = 0
        for s in list(*args):
            if a in s:
                count_a += 1
        if count_a == 0:
            result_4.append(a)
    return str(result_4)


strings = ("hello", "world", "python")
print(test_1_1(strings))
print(test_1_2(strings))
print(test_1_3(strings))
print(test_1_4(strings))
