### Task 2.5
### Write a Python program to print all unique values of all dictionaries in a list.
### Examples:
### ```
### Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
### Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

def get_dict_values(l:list):
    """
    The function gets a list of dictionaries and processes it to get all values from pairs key:value of those dictionaries.
    The function then returns a set of all unique values of the previously mentioned dictionaries.

    :param l: a list of dictionaries
    :return: a set of unique values in all dictionaries that were contained in processed list
    """

    assert isinstance(l, list) and all(map(lambda x: isinstance(x, dict), l)), 'Incorrect input. Must be a list of dictionaries'
    result = {value for dicts in l for value in dicts.values()}
    return result



