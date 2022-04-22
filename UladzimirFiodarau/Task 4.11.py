# Task 4.11
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines
# them into one dictionary. Dict values should be summarized in case of identical keys


def combine_dicts(*args: dict) -> dict:
    """
    # Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and
    combines them into one dictionary. New dictionary values are summarized in case of identical keys.
    :param args:
    :return:
    """
    assert all(map(lambda x: isinstance(x, dict), args)), 'Incorrect input. all arguments must be dicts'
    result = {}
    for dictionary in args:
        for key in dictionary:
            result[key] = result.get(key, 0) + dictionary[key]
    return result


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
# >>> {'a': 300, 'b': 200, 'c': 300}

print(combine_dicts(dict_1, dict_2, dict_3))
# {'a': 600, 'b': 200, 'c': 300, 'd': 100}

print(combine_dicts())
# {}

print(combine_dicts("dict3"))
# AssertionError: Incorrect input. all arguments must be dicts
