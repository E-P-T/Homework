#! /usr/bin/env python
# TODO: Implement a function which receives a string and replaces
# all `"` symbols with `'` and vise versa.


"""
task_1.py: implemented function which replaces all `"` symbols
with `'` and vise versa. Also contants speed tests for this function.
There is a conclustion about performance and style in the end of the module.
"""


import timeit
from numpy import average as avg


def replace_quotes(string):
    return string.replace('\'', '!$@%').replace('"', '\'').replace('!$@%', '"')


def replace_quotes2(string):
    list1 = string.split('"')
    string1 = ''.join([x + '!$@%' for x in list1[:-1]] + [list1[-1]])
    list2 = string1.split('\'')
    string2 = ''.join([x + '"' for x in list2[:-1]] + [list2[-1]])
    list3 = string2.split('!$@%')
    string3 = ''.join([x + '\'' for x in list3[:-1]] + [list3[-1]])
    return string3


if __name__ == '__main__':
    string1 = '''Hello "world". I've tired of this world'''
    string2 = 'Test only "double quotes"'
    string3 = "Test only 'single quotes'"

    result = replace_quotes(string1)
    print(result)  # Result: Hello 'world'. I"ve tired of this world
    result = replace_quotes(string2)
    print(result)  # Result: Test only 'double quotes'
    result = replace_quotes(string3)
    print(result)  # Result: Test only "single quotes"

    result = replace_quotes2(string1)
    print(result)  # Result: Hello 'world'. I"ve tired of this world
    result = replace_quotes2(string2)
    print(result)  # Result: Test only 'double quotes'
    result = replace_quotes2(string3)
    print(result)  # Result: Test only "single quotes"

    time_result = timeit.repeat(
        stmt="replace_quotes(string1)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(time_result))  # Result: 0.00033086959992942864

    time_result = timeit.repeat(
        stmt="replace_quotes2(string1)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(time_result))  # Result: 0.001963284600242332

    # The best way to write this function is to use built-in functions
    # instead of writing your own features because built-in functions work
    # with speed of language C
