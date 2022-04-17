# Task 2.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# ```


def char_count(chars):
    low_chars = chars.lower()
    char_dict = dict()
    for char in low_chars:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict
