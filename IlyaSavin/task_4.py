#! /usr/bin/env python
# TODO: ### Task 4.4
# Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# >>> python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("no luck", [42])
# ["no luck"]


"""
task_4.py: implemened two functions that split string by indeces.
The first is iterable implementation. The second is recursion implementation.
Also contains some speed tests for these fucntions.
"""


import timeit
from numpy import average as avg


def split_by_index(string, indeces=None):
    """
    split_by_index: iterable implementation of split_by_index
    """
    indeces = [index for index in indeces if index < len(string)]
    result = []
    pos = 0

    while indeces:
        result.append(string[pos:(pos := indeces.pop(0))])
    result.append(string[pos:])

    return result


def split_by_index_rec(string, indeces):
    """
    split_by_index: recursion implementation of split_by_index
    """
    indeces = [index for index in indeces if index < len(string)]

    def rec(string, indeces):
        if not string:
            return []

        if not indeces:
            return [string]

        pos = indeces.pop(0)
        indeces = [ind - pos for ind in indeces]

        return [string[0:pos]] + rec(string[pos:], indeces)

    return rec(string, indeces)


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    # Result: ['python', 'is', 'cool', ',', "isn't", 'it?']
    print(split_by_index("no luck", [42]))
    # Result: ['no luck']
    print(split_by_index_rec("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    # Result: ['python', 'is', 'cool', ',', "isn't", 'it?']
    print(split_by_index_rec("no luck", [42]))
    # Result: ['no luck']

    result = timeit.repeat(
        stmt="""split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])""",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0014431534000323154

    result = timeit.repeat(
        stmt="""split_by_index_rec("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])""",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.003600776800158201

    # As we can see iterable implementation is better with performance.
