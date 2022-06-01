# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:

# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

# ```python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
# ```

from string import ascii_lowercase


def test_1_1(*strings: list[str]) -> set[str]:
    """
    Return characters that appear in all strings.
    """
    if strings:
        chars = set(strings[0])
        for s in strings:
            chars = chars.intersection(set(s))
        return chars


def test_1_2(*strings: list[str]) -> set[str]:
    """
    Return characters that appear in at least one string.
    """
    if strings:
        chars = set()
        for s in strings:
            chars = chars.union(set(s))
        return chars


def test_1_3(*strings: list[str]) -> set[str]:
    """
    Return characters that appear at least in two strings.
    """
    if strings:
        chars = set()
        size = len(strings)
        for i in range(size):
            for j in range(i+1, size):
                found = set(strings[i]).intersection(set(strings[j]))
                chars = chars.union(found)
        return chars


def test_1_4(*strings: list[str]) -> set[str]:
    """
    Return characters of alphabet, that were not used in any string.
    """
    if strings:
        chars = set()
        for s in strings:
            chars = chars.union(set(s))
        return set(ascii_lowercase).difference(chars)


def main():
    """
    Entry point function.
    """
    test_strings = []
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))

    test_strings = ["hello", "world", "python", ]
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))


if __name__ == '__main__':
    main()
