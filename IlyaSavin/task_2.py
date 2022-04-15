# TASK2.2 FROM LECTION 2
"""
This module contains some functions to counter the symbols in a string.
All functions construct dictionary symbol -> number of symbols in a string.
Module also contains speed tests for these functions.
"""


import timeit
from numpy import average as avg
from collections import Counter


def count_string_characters(string) -> dict:
    counter = {}
    string = string.lower()
    while string:
        symbol = string[0]
        counter[symbol] = string.count(symbol)
        string = string.replace(symbol, '')
    return counter


def count_string_characters2(string) -> dict:
    counter = {}
    string = ''.join(sorted(string.lower()))
    while string:
        symbol = string[0]
        count = string.count(symbol)
        counter[symbol] = count
        string = string[count:]
    return counter


def count_string_characters3(string) -> dict:
    return dict(Counter(string.lower()))


def count_string_characters4(string) -> dict:
    string = string.lower()
    counter = {symbol: 0 for symbol in string}
    for symbol in string:
        counter[symbol] += 1
    return counter


if __name__ == '__main__':
    d1 = count_string_characters('Oh, it is python')
    d2 = count_string_characters2('Oh, it is python')
    d3 = count_string_characters3('Oh, it is python')
    d4 = count_string_characters4('Oh, it is python')
    print(d1 == d2 == d3 == d4)  # Result: True
    print(d1, d2, d3, d4, sep='\n')  # Result: as in answer in the Task2.2

    result = timeit.repeat(
        stmt='count_string_characters("Oh, it is python")',
        setup='import task_2',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00204353

    result = timeit.repeat(
        stmt='count_string_characters2("Oh, it is python")',
        setup='import task_2',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00235497

    result = timeit.repeat(
        stmt='count_string_characters3("Oh, it is python")',
        setup='import task_2',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00130545

    result = timeit.repeat(
        stmt='count_string_characters4("Oh, it is python")',
        setup='import task_2',
        number=1000,
        repeat=100,
        globals=globals()
    )
    print(f'{avg(result):.8f}')  # Average time: 0.00145297

    # ------------------------Results----------------------------------------
    # The best way to count the symbols in a string is to use class Counter
    # But the forth function is also good
