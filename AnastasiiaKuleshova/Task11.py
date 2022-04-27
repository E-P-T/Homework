# Task 4.11
# Implement a function, that receives changeable number of dictionaries
# (keys - letters, values - numbers) and combines them into one dictionary.
# Dict values ​​should be summarized in case of identical keys
#
# def combine_dicts(*args):
#     ...
#
# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}
#
# print(combine_dicts(dict_1, dict_2)
# >>> {'a': 300, 'b': 200, 'c': 300}
#
#
# print(combine_dicts(dict_1, dict_2, dict_3)
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}


def combine_dicts1(*args):
    all_keys = set()
    dict = {}
    for dict_ in args:
        all_keys |= dict_.keys()
    all_keys = sorted(all_keys)
    for key in all_keys:
        dict[key] = 0
        for dict_ in args:
            if key in dict_:
                dict[key] += dict_[key]
    return dict


print(combine_dicts1({'a': 100, 'b': 200},
                     {'a': 200, 'c': 300},
                     {'a': 300, 'd': 100},
                     {'a': 100, 'f': 300}))
