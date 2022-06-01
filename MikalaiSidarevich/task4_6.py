# Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
# Example:
# ```python

# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'

# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```

def get_longest_word(s: str) -> str:
    """
    Return the longest word in the given string.
    The word can contain any symbols except whitespaces.
    If there are multiple longest words in the string with a same length return the word that occures first.
    """
    words = s.split()
    longest = ''

    for word in words:
        if len(word) > 0:
            if len(word) > len(longest):
                longest = word
    return longest


def main():
    """
    Entry point function.
    """
    s = "Python\tis\nsimple and effective!"
    print(get_longest_word(s))
    s = "Any pythonista like namespaces a lot."
    print(get_longest_word(s))
    s = ""
    print(get_longest_word(s))


if __name__ == '__main__':
    main()
