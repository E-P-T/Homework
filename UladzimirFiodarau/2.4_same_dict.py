### Task 2.4
### Write a Python program to sort a dictionary by key.

def sorting_same_dictionary(x:dict, reverse=False):
    """
    The function takes a dictionary as an argument and sorts its pairs key:value of the by key
    :param x: dictionary
    :param reverse: if reverse is set as False, the sorting is made from lower to higher values,
    if reverse is set to True the sorting will be made reversed, from higher to lower values
    :return: None
    """
    assert isinstance(x, dict), 'Incorrect input. Must input a dictionary type'
    for key in sorted(x, reverse=reverse):
        value = x.pop(key)
        x[key] = value



dictionary = {'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# dictionary = [1, 3, 2]
# sorting_same_dictionary(dictionary, reverse=True)
sorting_same_dictionary(dictionary)
print(dictionary)