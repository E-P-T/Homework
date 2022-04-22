"""Implement a bunch of functions which receive a changeable number of strings and return next parameters:

1) characters that appear in all strings

2) characters that appear in at least one string

3) characters that appear at least in two strings

4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters
"""
import string
from itertools import combinations


def chars_in_all(*args):
    set_lst = [set(i) for i in args]
    out_set = set_lst[0]
    for i in range(1, len(set_lst)):
        out_set &= set_lst[i]
    return out_set


def at_least_one(*args):
    set_lst = [set(i) for i in args]
    out_set = set_lst[0]
    for i in range(1, len(set_lst)):
        out_set |= set_lst[i]
    return out_set


def at_least_two(*args):
    set_lst = [set(i) for i in args]
    out_set = set()
    for a, b in combinations(set_lst, 2):
        out_set |= a & b
    return out_set


def not_used_char(*args):
    used_char = at_least_one(*args)
    all_chars = set(string.ascii_lowercase)
    return all_chars - used_char


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]
    print(chars_in_all(*test_strings))
    print(at_least_one(*test_strings))
    print(at_least_two(*test_strings))
    print(not_used_char(*test_strings))
