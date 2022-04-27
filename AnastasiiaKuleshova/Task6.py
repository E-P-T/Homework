# Implement a function get_shortest_word(s: str) -> str which returns the longest
# word in the given string. The word can contain any symbols except
# whitespaces (, \n, \t and so on). If there are multiple longest words in the string
# with a same length return the word that occures first. Example:
#
#
# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'
#
# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'


def get_longest_word(line: str) -> str:
    longest_word = ""
    temp_index = 0
    for index in range(0, len(line)):
        if ord(line[index]) not in (range(48, 57) and range(65, 90) and range(97, 122)):
            if len(longest_word) < len(line[temp_index:index]):
                longest_word = line[temp_index:index]
            temp_index = index
    return longest_word


print(get_longest_word("fdsfjhh dlkf    dlklk/pp"))
