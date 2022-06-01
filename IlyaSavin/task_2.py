#! /usr/bin/env python
# TODO: Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.
# >>> python
# def most_common_words(filepath, number_of_words=3):
#     pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


"""
task_2.py: implemented two functions which search the most common words in
the file. Module also contains speed tests for these functions and the final
conclusion about performance.
"""


import timeit
from numpy import average as avg
from string import punctuation
from collections import Counter


def most_common_words(filepath, number_of_words=3):
    """
    most_common_words: own implementation with built-in instuments. It
    searchs the most common words in the file with path <filepath>. Number of
    words specify in argument number_of_words.
    """
    low_text = open(filepath).read().lower()
    list_of_words = [word.strip(punctuation) for word in low_text.split()]

    words_frequency = {}
    for word in list_of_words:
        words_frequency[word] = 1 if word not in words_frequency \
            else words_frequency[word] + 1

    words_by_frequency = sorted(
        words_frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    most_common_words = []
    for i in range(number_of_words):
        most_common_words.append(words_by_frequency.pop(0)[0])

    return most_common_words


def most_common_words2(filepath, number_of_words=3):
    """
    most_common_words: Implementation with class Counter from collections. It
    searchs the most common words in the file with pathe <filepath>. Number of
    words specify in argument number_of_words.
    """
    low_text = open(filepath).read().lower()
    list_of_words = [word.strip(punctuation) for word in low_text.split()]

    words_frequency = Counter()
    for word in list_of_words:
        words_frequency[word] = 1 if word not in words_frequency \
            else words_frequency[word] + 1

    return [el[0] for el in words_frequency.most_common(number_of_words)]


if __name__ == "__main__":
    print(most_common_words("data/lorem_ipsum.txt"))
    # Result: ['donec', 'etiam', 'aliquam']
    print(most_common_words2("data/lorem_ipsum.txt"))
    # Result: ['donec', 'etiam', 'aliquam']

    result = timeit.repeat(
        stmt="""most_common_words("data/lorem_ipsum.txt")""",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.17893063340052323

    result = timeit.repeat(
        stmt="""most_common_words2("data/lorem_ipsum.txt")""",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.2286652419996244

    # As we can see the class Counter worse than own implementation.
    # I think the first implementation also readable enough.
