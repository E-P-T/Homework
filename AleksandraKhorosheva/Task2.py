### Task 4.2
'''Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
['donec', 'etiam', 'aliquam']
```
NOTE: Remember about dots, commas, capital letters etc.'''
from collections import Counter


def most_common_words(filepath, number_of_words=3):
    with open(filepath, "r") as in_f:
        inpt = in_f.read()
        # lst = inpt.lower().translate(str.maketrans('', '', ',.')).split()
        lst = [x.strip('?.!,') for x in inpt.lower().split()]
        cnt = Counter(lst)
        return [x[0] for x in cnt.most_common(number_of_words)]
        # res = {x: lst.count(x) for x in lst}
        # s_res = sorted(res, key=res.get, reverse=True)[:number_of_words]
        #
        # return s_res


print(most_common_words('E:\PycharmProjects\Homework\data\lorem_ipsum.txt'))
