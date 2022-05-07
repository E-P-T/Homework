'''
Task 5.2
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
['donec', 'etiam', 'aliquam']
```

NOTE: Remember about dots, commas, capital letters etc.
'''

from collections import Counter


def file_to_list(filepath):
    with open(filepath, 'r') as inf:
        list_of_words = []
        for line in inf:
            list_of_words.extend(line.lower().replace(',', '').replace('.', '').split())
        return list_of_words


def most_common_words(filepath, number_of_words=3):
    lst = file_to_list(filepath)
    counter = Counter(lst)
    d = dict(counter.most_common(number_of_words))
    print(list(d.keys()))


if __name__ == '__main__':
    fpath = 'data/lorem_ipsum.txt'
    most_common_words(fpath, 4)
