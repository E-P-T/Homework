"""Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first."""


def get_shortest_word(s: str):
    words_lst = s.split()
    length_dict = {word: len(word) for word in words_lst}
    for k, v in length_dict.items():
        if v == max(length_dict.values()):
            return k


if __name__ == '__main__':
    print(get_shortest_word('Python is simple and effective!'))
    print(get_shortest_word('Any pythonista like namespaces a lot.'))
