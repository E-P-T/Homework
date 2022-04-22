# Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.


def get_shortest_word(string: str) -> str:
    """
    Despite its name saying quite the opposite the function processes a string and returns the longest word in string
    (punctuation symbols included). all whitespaces are ignored. If there are multiple longest words in
    the string with a same length it returns the word that occurs first. If given an empty string the function returns
    a message 'Empty string input'.
    :param string: input string
    :return: a string
    :raises AssertionError if input is not string type
    """
    assert isinstance(string, str), 'Incorrect input. first argument must be a string'
    words = string.split()
    lengths_list = [len(i) for i in words]
    for i, length in enumerate(lengths_list):
        if length == max(lengths_list):
            return words[i]
    return 'Empty string input'

# print(get_shortest_word('Python is simple and effective!'))
# 'effective!'

# print(get_shortest_word('Any pythonista like namespaces a lot.'))
# 'pythonista'

# print(get_shortest_word(''))
# 'Empty string input'
