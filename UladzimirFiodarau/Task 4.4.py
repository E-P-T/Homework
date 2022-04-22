# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes must be ignored.


def split_by_index(string: str, indexes: list[int]) -> list[str]:
    """
    The function takes a string and a list of integers, and splits the string into list of substrings using given
    integers as delimiters
    :param string: taken string
    :param indexes: taken list of indexes
    :return: list of substrings
    :raises AssertionError if first argument is not a string or second argument is not a list of integers
    """
    assert isinstance(string, str), 'Incorrect input. first argument must be a string'
    assert isinstance(indexes, list) and all(map(lambda x: isinstance(x, int), indexes)), 'Incorrect input. ' \
                                                                                          'second argument must be a list of integers'
    result = []
    if indexes:
        if string[:indexes[0]]:
            result.append(string[:indexes[0]])
        for i, index in enumerate(indexes):
            if i < len(indexes) - 1 and string[index:indexes[i + 1]]:
                result.append(string[index:indexes[i + 1]])
        if string[indexes[-1]:]:
            result.append(string[indexes[-1]:])
    else:
        if string:
            result.append(string)
    return result


print(split_by_index("no luck", [42]))
# ["no luck"]

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# ["python", "is", "cool", ",", "isn't", "it?"]

print(split_by_index("pythoniscool,isn'tit?", []))
# ["pythoniscool,isn'tit?"]

print(split_by_index("", [6, 8, 12, 13, 18]))
# []

print(split_by_index("", []))
# []
