### Task 2.4
### Write a Python program to sort a dictionary by key.

def sorting_new_dictionary(x:dict, reverse=False):
    """
    The function takes a dictionary as an argument and returns a dictionary, in which all the pairs key:value of the
    original dictionary are sorted by key
    :param x: dictionary
    :param reverse: if reverse is set as False, the sorting is made from lower to higher values,
    if reverse is set to True the sorting will be made reversed, from higher to lower values
    :return: a sorted dictionary
    # >>> sorting_new_dictionary({'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1})
    # {'h': 2, 'i': 2, 'n': 1, 'o': 2, 'p': 1, 's': 1, 't': 2, 'y': 1}
    # >>> sorting_new_dictionary({'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}, reverse=True)
    # {'y': 1, 't': 2, 's': 1, 'p': 1, 'o': 2, 'n': 1, 'i': 2, 'h': 2}
    # >>> sorting_new_dictionary({})
    # {}
    # >>> sorting_new_dictionary(5)
    # Traceback (most recent call last):
    # ...
    # AssertionError: Incorrect input. Must input a dictionary type


    """
    assert isinstance(x, dict), 'Incorrect input. Must input a dictionary type'
    result = {}
    for key in sorted(x, reverse=reverse):
        value = x.pop(key)
        result[key] = value
    return result


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
    

