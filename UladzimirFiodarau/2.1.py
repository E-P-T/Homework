### Task 2.1
### Write a Python program to calculate the length of a string without using the `len` function.

def calculate_string_length(x:str):
    """
    this function takes a string as an argument and calculates its length in symbols
    :param x: x is the inputed string
    :return: an integer, that shows length of string x in symbols
    # >>> calculate_string_length('asdf')
    # 4
    # >>> calculate_string_length('')
    # 0
    # >>> calculate_string_length('aaaaa')
    # 5
    # >>> calculate_string_length(5)
    # Traceback (most recent call last):
    # ...
    # AssertionError: Incorrect input, must be a string type


    """
    assert isinstance(x, str), 'Incorrect input, must be a string type'
    count = 0
    for _ in x:
        count += 1
    return count

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

