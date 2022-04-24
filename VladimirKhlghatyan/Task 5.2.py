# Task 5.2
# Implement a function which search for most common words in the file.
# Use data/lorem_ipsum.txt file as a example.
#
# def most_common_words(filepath, number_of_words=3):
#    pass
#
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.


def most_common_words(filepath, number_of_words=3):

    """ a function which search for most common words in the file """

    with open(filepath, 'r') as fd:
        words_lst = fd.read().replace('.', '').replace(',', '').lower().split()
    words_dict = dict()
    for word in words_lst:
        words_dict[word] = words_dict.get(word, 0) + 1
    sorted_words_lst = sorted(words_dict, reverse=True, key=lambda key: words_dict[key])
    common_words = list()
    for key in sorted_words_lst:
        if len(common_words) == number_of_words:
            return common_words
        common_words.append(key)
    return common_words
