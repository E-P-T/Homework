# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) chazacters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
from string import ascii_lowercase


def test_1_1(*strings: str) -> set:
    """
    The function takes a changeable number of strings and returns characters that appear in all strings
    :param strings: a changeable number of strings
    :return: a set
    :raises AssertionError if not oll of the arguments are strings
    """
    assert all(map(lambda x: isinstance(x, str), strings)), 'Incorrect input. all arguments must be strings'
    result = set(strings[0])
    for string in strings[1:]:
        result &= set(string)
    return result


def test_1_2(*strings: str) -> set:
    """
    The function takes a changeable number of strings and returns characters that appear in at least one string
    :param strings: a changeable number of strings
    :return: a set
    :raises AssertionError if not oll of the arguments are strings
    """
    assert all(map(lambda x: isinstance(x, str), strings)), 'Incorrect input. all arguments must be strings'
    return {j for i in strings for j in i}


def test_1_3(*strings: str) -> set:
    """
    The function takes a changeable number of strings and returns characters that appear at least in two strings
    :param strings: a changeable number of strings
    :return: a set
    :raises AssertionError if not oll of the arguments are strings
    """
    assert all(map(lambda x: isinstance(x, str), strings)), 'Incorrect input. all arguments must be strings'
    result = set()
    used = set()
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and (j, i) not in used:
                result |= set(string1) & set(string2)
                used.add((i, j))
    return result


def test_1_4(*strings: str) -> set:
    """
    The function takes a changeable number of strings and returns characters of alphabet, that were not used
    in any string
    :param strings: a changeable number of strings
    :return: a set
    :raises AssertionError if not oll of the arguments are strings
    """
    assert all(map(lambda x: isinstance(x, str), strings)), 'Incorrect input. all arguments must be strings'
    return set(ascii_lowercase) - {j for i in strings for j in i}


test_strings = ["hello", "world", "python", ]

print(test_1_1(*test_strings))
# {'o'}

print(test_1_2(*test_strings))
# {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}  # order may change

print(test_1_3(*test_strings))
# {'h', 'l', 'o'}  # order may change

print(test_1_4(*test_strings))
# {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}  # order may change
