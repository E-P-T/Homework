'''
Task 4.3
Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse).
'''


def split_by_symbol(string: str, symbol: str) -> list:
    resulted_list = []
    splitted_words = []
    for letter in string:
        if letter != symbol:
            splitted_words.append(letter)
        else:
            resulted_list.append(''.join(splitted_words))
            splitted_words = []
    resulted_list.append(''.join(splitted_words))
    return resulted_list


print(split_by_symbol("text text2 text1", " "))

