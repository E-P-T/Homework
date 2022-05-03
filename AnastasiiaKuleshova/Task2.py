# Task 4.2
# Implement a function which search for most common words in the file.
# Use data/lorem_ipsum.txt file as a example.
#
# def most_common_words(filepath, number_of_words=3):
#     pass
#
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# NOTE: Remember about dots, commas, capital letters etc.

import os
import re


def most_common_words(filepath, number_of_words=3):
    words_dict = {}
    result_list_of_words = []
    try:
        with open(filepath, 'r') as opened_file:
            text = opened_file.read()
        filtered_text = re.sub(r'[^a-zA-Z\d ]', '', text).split(' ')
        for word in filtered_text:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] = words_dict[word] + 1
        for word in words_dict:
            if words_dict[word] >= number_of_words:
                result_list_of_words.append(word)

    except FileExistsError:
        print("there is no file")

    return result_list_of_words


print(most_common_words('..\data\lorem_ipsum.txt', 12))
