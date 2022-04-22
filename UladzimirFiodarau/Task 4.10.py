# Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary, where the key is a number
# and the value is the square of that number.
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def generate_squares(num: int) -> dict[int]:
    """
    The function takes an integer as an argument and returns a dictionary, where keys belong to a sequence of numbers
    from 1 to input integer (included) and values are squares of number in corresponding key.
    :param num: integer
    :return: dictionary
    :raises AssertionError if input is not an integer
    """
    assert isinstance(num, int), 'Incorrect input. first argument must be an integer'
    return {i: i ** 2 for i in range(1, num + 1)}


print(generate_squares(5))
