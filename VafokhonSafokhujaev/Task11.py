
def combine_dicts(*args: dict) -> dict:
    accumulated = {}

    for el in args:
        for key, val in el.items():
            if key in accumulated:
                accumulated[key] += val
            else:
                accumulated[key] = val

    return accumulated


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
