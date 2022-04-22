# Task 5.1
# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
# `sorted_names.txt`. Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier


def sort_file(uns_path: str ='data/unsorted_names.txt', sort_path: str ='data/sorted_names.txt') -> None:
    """
    The function opens file in given path (default path is 'data/unsorted_names.txt'),
    sorts the names in it and writes them to a new file in given path(default path is 'data/sorted_names.txt').
    Each name starts with a new line.
    :param uns_path: path to unsorted file
    :param sort_path: path to output sorted file
    :return: None
    """
    with open(uns_path, 'r', encoding='utf-8') as uns_file, \
            open(sort_path, 'w', encoding='utf-8') as sort_file:
        for line in sorted(uns_file.readlines()):
            print(line.strip(), file=sort_file)

sort_file('data/unsorted_names.txt', 'data/sorted_names.txt')