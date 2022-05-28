#! /usr/bin/env python
# TODO: Write a function that check whether a string is a palindrome or not.
# Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from [here]
# (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).


"""
task_2.py: implemented 6 different ways to check whether string a palindrome or
not. Also contains some speed tests for these functions.
"""


import timeit
from numpy import average as avg


def is_palindrome_indeces(string) -> bool:
    """
    is_palindrome_indeces: check wheter string a palindrome or not with slices.
    """
    return string == string[::-1]


def is_palindrome_loopfor(string):
    """
    is_palindrome_loopfor: check wheter string a palindrome or not with
    loop for.
    """
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False

    return True


def is_palindrome_loopwhile(string):
    """
    is_palindrome_loopwhile: check wheter string a palindrome or not with
    loop while.
    """
    i = 0

    while i < len(string) // 2:
        if string[i] != string[-(i + 1)]:
            return False
        i += 1

    return True


def is_palindrome_recursion(string):
    """
    is_palindrome_recursion: check wheter string a palindrome or not with
    recursion.
    """
    def rev(string):
        return string[-1] + rev(string[:-1]) if string else ''

    if string == rev(string):
        return True

    return False


def is_palindrome_genexpr(string) -> bool:
    """
    is_palindrome_genexpr: check wheter string a palindrome or not with
    generator expression.
    """
    return string == ''.join(string[-(i + 1)] for i in range(len(string)))


def is_palindrome_listcomp(string) -> bool:
    """
    is_palindrome_listcomp: check wheter string a palindrome or not with
    list comprehension.
    """
    return string == ''.join([string[-(i + 1)] for i in range(len(string))])


if __name__ == '__main__':
    print(is_palindrome_indeces('qwertyytrewq'))  # Result: True
    print(is_palindrome_loopfor('qwertyytrewq'))  # Result: True
    print(is_palindrome_loopwhile('qwertyytrewq'))  # Result: True
    print(is_palindrome_recursion('qwertyytrewq'))  # Result: True
    print(is_palindrome_genexpr('qwertyytrewq'))  # Result: True
    print(is_palindrome_listcomp('qwertyytrewq'))  # Result: True

    print(is_palindrome_indeces('qwerty'))  # Result: False
    print(is_palindrome_loopfor('qwerty'))  # Result: False
    print(is_palindrome_loopwhile('qwerty'))  # Result: False
    print(is_palindrome_recursion('qwerty'))  # Result: False
    print(is_palindrome_genexpr('qwerty'))  # Result: False
    print(is_palindrome_listcomp('qwerty'))  # Result: False

    result = timeit.repeat(
        stmt="is_palindrome_indeces('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.00014375739920069464

    result = timeit.repeat(
        stmt="is_palindrome_loopfor('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0006004619994200766

    result = timeit.repeat(
        stmt="is_palindrome_loopwhile('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0008355476005817763

    result = timeit.repeat(
        stmt="is_palindrome_recursion('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0022450227996159812

    result = timeit.repeat(
        stmt="is_palindrome_genexpr('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0022450227996159812

    result = timeit.repeat(
        stmt="is_palindrome_listcomp('qwertyytrewq')",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.001127898799313698

    # The best way to do this task is to use slices and common loops.
    # The other ways fairly slow in comparison with slices and loops.
