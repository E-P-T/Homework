# Task 5.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.
# > NOTE: Remember about dots, commas, capital letters etc.


def most_common_words(filepath: str, number_of_words: int = 3) -> list[str]:
    """
    The function searches for most common words in the file, excluding dots, commas, etc. and capital letters, and then
    returns a list of a given number of most common words (frequency descending).

    :param filepath: path to input file
    :param number_of_words: number of most common words to return
    :return:
    :raises AssertionError if second argument is not integer
    """
    assert isinstance(number_of_words, int), 'Incorrect input, second argument must be an integer'
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        rejected = ',.!:;'
        words_freq = {}
        for line in lines:
            new_line = ''.join([i.lower() for i in line.strip() if i not in rejected])
            for word in new_line.split():
                words_freq[word] = words_freq.get(word, 0) + 1
    return [key for key in sorted(words_freq, reverse=True, key=words_freq.get)[:number_of_words]]


print(most_common_words('data/lorem_ipsum.txt'))
# ['donec', 'etiam', 'aliquam']
