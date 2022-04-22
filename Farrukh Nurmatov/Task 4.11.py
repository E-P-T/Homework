"""Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
 and combines them into one dictionary. Dict values should be summarized in case of identical keys"""


def combine_dicts(*args):
    out_dict = dict()
    for arg in args:
        for k, v in arg.items():
            if k in out_dict.keys():
                out_dict[k] += v
            else:
                out_dict[k] = v
    return out_dict


if __name__ == '__main__':

    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))