#! /usr/bin/env python
# TODO: Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse


"""
task_3.py: implemened two functions like str.split.
The first is iterable implementation. The second is recursion implementation.
Also contains some speed tests for these fucntions.
"""

import timeit
from numpy import average as avg


def split_iterable(string, sep=' ', maxsplit=-1):
    """
    split_iterable: iterable implementation of str.split.
    maxsplit is how much blocks need to be in the result list.
    """
    result = []
    pos = None

    while maxsplit != 0:
        pos = string.find(sep)
        if pos == -1:
            break
        result.append(string[:pos])
        string = string[pos + len(sep):]
        maxsplit -= 1

    result.append(string)
    return result


def split_recursion(string, sep=' ', maxsplit=-1):
    """
    split_recursion: recursion implementation of str.split.
    maxsplit is how much blocks need to be in the result list.
    """
    if maxsplit == 0:
        return [string]

    pos = string.find(sep)

    if pos == -1:
        return [string]

    return [string[:pos]] + \
        split_recursion(string[pos + len(sep):], sep=sep, maxsplit=maxsplit - 1)


if __name__ == '__main__':
    print(split_iterable('hello world how are you doing', maxsplit=3))
    # Result: ['hello', 'world', 'how', 'are you doing']
    print(split_recursion('hello world how are you doing', maxsplit=3))
    # Result: ['hello', 'world', 'how', 'are you doing']
    print(split_iterable('hello world how are you doing'))
    # Result: ['hello', 'world', 'how', 'are', 'you', 'doing']
    print(split_recursion('hello world how are you doing'))
    # Result: ['hello', 'world', 'how', 'are', 'you', 'doing']
    print(split_iterable('hello___world how___are you_doing', sep='___'))
    # Result: ['hello', 'world how', 'are you_doing']
    print(split_recursion('hello___world how___are you_doing', sep='___'))
    # Result: ['hello', 'world how', 'are you_doing']

    result = timeit.repeat(
        stmt="split_iterable('hello world how are you doing', maxsplit=3)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.001036395601113327

    result = timeit.repeat(
        stmt="split_recursion('hello world how are you doing', maxsplit=3)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0013307645989698359

    # As we can see iterable implementation is better with performance but
    # for me recursion implementation easier to read.
