"""Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
['donec', 'etiam', 'aliquam']"""

from string import punctuation
from collections import Counter


def most_common_words(filepath, number_of_words=3):
    file = open(filepath, "r")
    words = []
    for line in file.readlines():
        words += line.split()
    file.close()
    clear_words = [word.strip(punctuation).lower() for word in words]
    freq_counter = Counter(clear_words)
    most_common = [word[0] for word in freq_counter.most_common(number_of_words)]
    return most_common


if __name__ == '__main__':
    print(most_common_words("data/lorem_ipsum.txt"))
