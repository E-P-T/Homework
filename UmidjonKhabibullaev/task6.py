from turtle import position
from task3 import custom_split

def get_longest_word(sentence: str) -> str:
    """ Function that finds the longest word in a given `sentence`.
        Returns that word.
    """
    longest_word = ""
    words = custom_split(sentence)
    max_length = max([len(word) for word in words])

    for word in words:
        if len(word) == max_length:
            longest_word = word
            break

    return longest_word


if __name__ == "__main__":
    s = "Any pythonista like namespaces a lot."
    print(get_longest_word(s))