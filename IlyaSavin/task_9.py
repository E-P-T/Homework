#! /usr/bin/env python
# TODO: Implement a bunch of functions which receive a
# changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters
# >>> python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j',
# 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}


"""
task_9.py: implemented a bunch of functions which receive a changable number
of string and return next parameters. Also it contains some speed tests.
And ofcourse it contains several implementation for each function.
"""


import timeit
from string import ascii_lowercase as ascii
from numpy import average as avg


def test_1_1(*strings):
    """
    test_1_1: short implementation of option 1 with comprehension and built-in
    functions.
    """
    return {sym for sym in ascii if all(sym in string for string in strings)}


def test_1_2(*strings):
    """
    test_1_2: short implementation of option 2 with comprehension and built-in
    functions.
    """
    return {sym for sym in ascii if any(sym in string for string in strings)}


def test_1_3(*strings):
    """
    test_1_3: short implementation of option 3 with comprehension and built-in
    functions.
    """
    return {
        sym for sym in ascii
        if list(sym in string for string in strings).count(True) >= 2
    }


def test_1_4(*strings):
    """
    test_1_4: short implementation of option 4 with comprehension and built-in
    functions.
    """
    return {
        sym for sym in ascii
        if not any(sym in string for string in strings)
    }


def test_1_1_2(*strings):
    """
    test_1_1_2: long implementation of option 1 with own logic and loops
    """
    syms = set()
    for sym in ascii:
        for string in strings:
            if sym not in string:
                break
        else:
            syms.add(sym)
    return syms


def test_1_2_2(*strings):
    """
    test_1_2_2: long implementation of option 2 with own logic and loops
    """
    syms = set()
    for sym in ascii:
        for string in strings:
            if sym in string:
                syms.add(sym)
                break
    return syms


def test_1_3_2(*strings):
    """
    test_1_3_2: long implementation of option 3 with own logic and loops
    """
    syms = set()
    for sym in ascii:
        count = 0
        for string in strings:
            if sym in string:
                count += 1
                if count == 2:
                    syms.add(sym)
                    break
    return syms


def test_1_4_2(*strings):
    """
    test_1_4_2: long implementation of option 4 with own logic and loops
    """
    syms = set()
    for sym in ascii:
        for string in strings:
            if sym in string:
                break
        else:
            syms.add(sym)
    return syms


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]

    print(test_1_1(*test_strings))
    # Result: {'o'}
    print(test_1_2(*test_strings))
    # Result: {'o', 'd', 'y', 'e', 'l', 'p', 't', 'h', 'n', 'r', 'w'}
    print(test_1_3(*test_strings))
    # Result: {'o', 'l', 'h'}
    print(test_1_4(*test_strings))
    # Result: {'s', 'a', 'g', 'u', 'm', 'x', 'f',
    # 'c', 'i', 'z', 'v', 'k', 'q', 'b', 'j'}

    print(test_1_1_2(*test_strings))
    # Result: {'o'}
    print(test_1_2_2(*test_strings))
    # Result: {'o', 'd', 'y', 'e', 'l', 'p', 't', 'h', 'n', 'r', 'w'}
    print(test_1_3_2(*test_strings))
    # Result: {'o', 'l', 'h'}
    print(test_1_4_2(*test_strings))
    # Result: {'s', 'a', 'g', 'u', 'm', 'x', 'f',
    # 'c', 'i', 'z', 'v', 'k', 'q', 'b', 'j'}

    result = timeit.repeat(
        stmt="test_1_1(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.00890382840007078

    result = timeit.repeat(
        stmt="test_1_2(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.009633217800001148

    result = timeit.repeat(
        stmt="test_1_3(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.01200047940001241

    result = timeit.repeat(
        stmt="test_1_4(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.009639995799989264

    result = timeit.repeat(
        stmt="test_1_1_2(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0016742077999879258

    result = timeit.repeat(
        stmt="test_1_2_2(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.002906245999929524

    result = timeit.repeat(
        stmt="test_1_3_2(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0033433137999963948

    result = timeit.repeat(
        stmt="test_1_4_2(*test_strings)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0030913654000869427

    # As we can see own implementation faster than built-in functions.
    # I suppose it because it contains a lot of functions and that's why
    # loop implementation is faster.
