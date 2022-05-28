#! /usr/bin/env python
# TODO: Implement a function get_pairs(lst: List) -> List[Tuple] which returns
# a list of tuples containing pairs of elements. Pairs should be formed as in
# the example. If there is only one element in the list return `None` instead.
# Example:
# >>> python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
# >>> get_pairs([1])
# None


"""
task_8.py: implemented function, which takes a list of elements and returns a
new list with pairs of elements. Also contains some speed tests.
"""


import timeit
from numpy import average as avg


def get_pairs(L: list) -> list[tuple]:
    """
    get_pairs: returns new list with pairs with list comprehension.
    """
    return [(x, L[i + 1]) for i, x in enumerate(L[:-1])] if len(L) > 1 else None


def get_pairs2(L: list) -> list[tuple]:
    """
    get_pairs2: returns new list with pairs with loop for.
    """
    if len(L) <= 1:
        return None

    result = []

    for i, x in enumerate(L[:-1]):
        result.append((x, L[i + 1]))

    return result


def get_pairs3(L: list) -> list[tuple]:
    """
    get_pairs3: returns new list with pairs with recursion.
    """
    if len(L) <= 1:
        return None

    def recur(L):
        return [(L[0], L[1])] + recur(L[1:]) if len(L) > 1 else []

    return recur(L)


if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    # Result: [(1, 2), (2, 3), (3, 8), (8, 9)]
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    # Result: [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    print(get_pairs([1]))
    # Result: None

    print(get_pairs2([1, 2, 3, 8, 9]))
    # Result: [(1, 2), (2, 3), (3, 8), (8, 9)]
    print(get_pairs2(['need', 'to', 'sleep', 'more']))
    # Result: [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    print(get_pairs2([1]))
    # Result: None

    print(get_pairs3([1, 2, 3, 8, 9]))
    # Result: [(1, 2), (2, 3), (3, 8), (8, 9)]
    print(get_pairs3(['need', 'to', 'sleep', 'more']))
    # Result: [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    print(get_pairs3([1]))
    # Result: None

    result = timeit.repeat(
        stmt="get_pairs([1, 2, 3, 8, 9])",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0007633056002305239

    result = timeit.repeat(
        stmt="get_pairs2([1, 2, 3, 8, 9])",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0006805298000472249

    result = timeit.repeat(
        stmt="get_pairs3([1, 2, 3, 8, 9])",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0012972673999684047
