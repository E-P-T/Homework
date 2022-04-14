### Task 2.2
### Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
### Examples:
### Input: 'Oh, it is python'
### Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}


def frequency_counter(x:str) -> dict:
    """
    The function takes a string as an argument and returns a dictionary, where keys are characters
    of the string, and corresponding values show how many times the character is represented in processed
    string, case of letters is ignored, keys in resulting dictionary are all stored in lower case

    :param x: a string
    :return: a dictionary of character frequencies in the processed string
    >>> frequency_counter('')
    {}
    >>> frequency_counter('Oh, it is python')
    {'o': 2, 'h': 2, ',': 1, ' ': 3, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
    >>> frequency_counter('ABBA is a beast')
    {'a': 4, 'b': 3, ' ': 3, 'i': 1, 's': 2, 'e': 1, 't': 1}
    >>> frequency_counter(23424)
    Traceback (most recent call last):
    ...
    AssertionError: Incorrect input, must be a string type
    """

    assert isinstance(x, str), 'Incorrect input, must be a string type'
    frequency_dict = {}
    for character in x.lower():
        frequency_dict[character] = frequency_dict.get(character, 0) + 1
    return frequency_dict


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# print(frequency_counter('Oh, it is python'))
# print(frequency_counter(''))
