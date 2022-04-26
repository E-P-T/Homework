# Task 4.11

def combine_dicts(*args):
    combined = {}
    for i in args:
        for k in i.keys():
            if k in combined.keys():
                combined[k] += i[k]
            else:
                combined[k] = i[k]
    return combined


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2,))

print(combine_dicts(dict_1, dict_2, dict_3))
