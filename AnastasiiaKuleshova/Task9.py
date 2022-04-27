# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# characters that appear in all strings
# characters that appear in at least one string
# characters that appear at least in two strings
# characters of alphabet, that were not used in any string
# Note: use string.ascii_lowercase for list of alphabet letters
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


def test_1(strings: [str]):
    result = set(strings[0])
    for i in range(1, len(strings)):
        result = result & set(strings[i])
    print(list(result))


def test_2(strings: [str]):
    result = set(strings[0])
    for i in range(1, len(strings)):
        result = result | set(strings[i])
    print(list(result))


def test_3(strings: [str]):
    result = set()
    for i in range(0, len(strings)):
        for j in range(i + 1, len(strings)):
            result |= (set(strings[i]) & set(strings[j]))
    return result


def test_4(strings: [str]):
    alphabet = set(string.ascii_lowercase)
    result = set()
    for i in range(0, len(strings)):
        result = set(strings[i]) | result
    result = alphabet - result
    return result


print(test_3(["hello", "world", "python"]))
