#! /usr/bin/env python
# TODO: Implement a function, that receives changeable number of dictionaries
# (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values ​​should be summarized in case of identical keys
# >>> python
# def combine_dicts(*args):
#     ...
# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}
# print(combine_dicts(dict_1, dict_2))
# >>> {'a': 300, 'b': 200, 'c': 300}
# print(combine_dicts(dict_1, dict_2, dict_3))
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}


"""
task_11.py: implemented 2 functions which combine dicts and some speed tests
for these functions.
"""


import timeit
from numpy import average as avg


def combine_dicts(*args):
    """
    combine_dicts: combines dicts with loop for and dict methods.
    """
    result = {}
    for dict in args:
        for key in dict:
            result[key] = result.get(key, 0) + dict[key]
    return result


def combine_dicts2(*args):
    """
    combine_dicts2: combines dicts with dict comprehension
    """
    result = {}
    {result.__setitem__(key, result.get(key, 0) +
     dict[key]) for dict in args for key in dict}
    return result


if __name__ == "__main__":
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    # Result: {'a': 300, 'b': 200, 'c': 300}
    print(combine_dicts(dict_1, dict_2, dict_3))
    # Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}

    print(combine_dicts2(dict_1, dict_2))
    # Result: {'a': 300, 'b': 200, 'c': 300}
    print(combine_dicts2(dict_1, dict_2, dict_3))
    # Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}

    result = timeit.repeat(
        stmt="combine_dicts(dict_1, dict_2, dict_3)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0008159936005540658

    result = timeit.repeat(
        stmt="combine_dicts2(dict_1, dict_2, dict_3)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.001815845400415128

    # The first function is better for obvious reasons
    # The second function is awful but I need 2 or more functions to
    # train timeit module :)
