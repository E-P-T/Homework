# Task 2.4. Write a Python program to sort a dictionary by key.


from collections import OrderedDict


def sort_dict_by_key(dictionary):
    result = OrderedDict()
    list_keys = list(dictionary.keys())
    list_keys.sort()
    for i in list_keys:
        result[i] = dictionary[i]
    return result


print(sort_dict_by_key({'a': 1, 'c': 3, 'b': 2}))
