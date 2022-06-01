# Task 5.2
# Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a
# example.
# def most_common_words(filepath, number_of_words=3):
# pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.

import os
from string import punctuation


def most_common_words(filepath, number_of_words=3):
    """
    Search for most `number_of_words` common words in the `filepath` specified.
    """
    freq = {}

    with open(filepath, 'r') as f:
        for line in f:
            for word in line.lower().split():
                # Remove punctuation chars
                word = ''.join(filter(lambda ch: ch not in punctuation, word))
                # Count word
                freq[word] = freq.get(word, 0) + 1

    freq = dict(sorted(freq.items(), key=lambda t: t[1], reverse=True))

    return list(freq.keys())[0:number_of_words]


def main():
    """
    Entry point function.
    """
    filepath = os.path.join("..", "data", "lorem_ipsum.txt")
    print(most_common_words(filepath, 1))
    print(most_common_words(filepath))


if __name__ == '__main__':
    main()
