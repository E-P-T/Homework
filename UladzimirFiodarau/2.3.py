### Task 2.3
### Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
### Examples:
### Input: ['red', 'white', 'black', 'red', 'green', 'black']
### Output: ['black', 'green', 'red', 'white', 'red']

def sort_unique_words(s, reverse=False):
    """
    The function takes a sequence (list, or tuple, or set) of words (strings) as an argument and returns a sorted in
    lexicographical order list of unique words in processed collection

    :param s: can be a list, tuple or a set
    :param reverse: if reverse is set as False, the sorting is made from lower to higher values,
    if reverse is set to True the sorting will be made reversed, from higher to lower values
    :return: a sorted list of unique words
    :raises AssertionError: if any item in collection is not string type

    >>> sort_unique_words(['red', 'white', 'black', 'red', 'green', 'black'])
    ['black', 'green', 'red', 'white']
    >>> sort_unique_words([])
    []
    >>> sort_unique_words(['red', 'white', 'black', 'red', 'green', 'black'], reverse=True)
    ['white', 'red', 'green', 'black']
    >>> sort_unique_words(('red', 'white', 'black', 'red', 'green', 'black'))
    ['black', 'green', 'red', 'white']
    >>> sort_unique_words({'white', 'black', 'red', 'green'})
    ['black', 'green', 'red', 'white']
    >>> sort_unique_words({'white', 'black', 5, 'green'})
    Traceback (most recent call last):
    ...
    AssertionError: Different data types in imported collection. All items in collection must be string type
    """

    assert all(map(lambda x: isinstance(x, str), s)), 'Different data types in imported collection.' \
                                                      ' All items in collection must be string type'
    return sorted(set(s), reverse=reverse)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# print(sort_unique_words(['red', 'white', 'black', 'red', 'green', 'black']))
# print(sort_unique_words(['red', 'white', 'black', 'red', 'green', 'black'], reverse=True))
# print(sort_unique_words(('red', 'white', 'black', 'red', 'green', 'black')))
# print(sort_unique_words({'white', 'black', 'red', 'green'}))
# print(sort_unique_words({'white', 'black', 5, 'green'}))
