# Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
# Example:
# ```python
#
# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'
#
# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```


def get_shortest_word(s: str) -> str:
    s.replace('\t', ' ')
    s.replace('\n', ' ')
    s.replace('\v', ' ')
    s.replace('\f', ' ')
    s.replace('\r', ' ')
    words = s.split()
    words.sort(key=len)
    words.reverse()
    if len(words) == 1:
        return words[0]
    for i in range(len(words)):
        if len(words[i+1]) < len(words[i]):
            return words[i]
