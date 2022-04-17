# Task 2.4
# Write a Python program to sort a dictionary by key.


def sort_dict_by_key(dictionary):
    sorted_keys = sorted(dictionary.keys())
    sorted_dictionary = dict()
    for item in sorted_keys:
        sorted_dictionary[item] = dictionary[item]
    return sorted_dictionary
