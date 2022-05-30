# Task 4.11
# Implement a function, that receives changeable number of dictionaries
# (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values should be summarized in case of identical keys

# ```python
# def combine_dicts(*args):

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2)
# >>> {'a': 300, 'b': 200, 'c': 300}

# print(combine_dicts(dict_1, dict_2, dict_3)
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}


def combine_values(*args):

    result = dict()

    for dictionary in args:
        for k in dictionary.keys():
            if k not in result.keys():
                result[k] = 0
            result[k] = result[k] + dictionary[k]
    return result


print(combine_values({'a': 100, 'b': 200}, {'a': 100, 'b': 200}))
