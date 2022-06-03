def combine_dicts(*args) -> dict:
    new_dict = {}
    for dictionary in args:
        for key in dict(dictionary).keys():
            if key in new_dict:
                new_dict[key] += int(dictionary[key])
            else:
                new_dict[key] = dictionary[key]
    return new_dict


if __name__ == "__main__":
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2, dict_3))
