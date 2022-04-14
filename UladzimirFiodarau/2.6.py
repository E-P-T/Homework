### Task 2.6
### Write a Python program to convert a given tuple of positive integers into an integer.
### Examples:
### Input: (1, 2, 3, 4)
### Output: 1234

def convert_tuple_to_integer(tup:tuple):
    """
    The function takes a tuple of positive integers as an argument and returns an integer with digits,
    originated from the taken tuple in the same order (tuple index 0 = the highest register,
    index 1 - second highest and so on)
    :param tup:a tuple of positive integers
    :return: an integer
    """
    assert isinstance(tup, tuple) and all(map(lambda x: isinstance(x, int) and x > 0, tup)), \
        'Incorrect input. Must be a tuple of positive integers'
    # result = ''.join([str(i) for i in tup])
    return int(''.join([str(i) for i in tup]))

