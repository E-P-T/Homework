def combine_dicts(*dictionaries) -> dict:
    """ Function that takes a variable number of dictionaries in arguments.
        Combines them into one and returns the combined dictionary.
    """
    combined_dict = {
        letter: number
        for dictionary in dictionaries
        for letter, number in dictionary.items()
    }

    return combined_dict


if __name__ == "__main__":
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2, dict_3))