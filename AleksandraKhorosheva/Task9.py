# Task 4.9
'''Implement a bunch of functions which receive a changeable number of strings and return next parameters:

1) characters that appear in all strings

2) characters that appear in at least one string

3) characters that appear at least in two strings

4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters

```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
{'o'}
print(test_1_2(*strings))
{'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
{'h', 'l', 'o'}
print(test_1_4(*strings))
{'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
'''
import string
from collections import Counter

def test_1_1(strings):
    result = set.intersection(*map(set, strings))
    return result

print(test_1_1(["hello", "world", "python"]))


def test_1_2(strings):
    result = set.union(*map(set, strings))
    return result

print(test_1_2(["hello", "world", "python"]))

def test_1_3(strings):
    letters = {k for k, v in Counter([l for x in strings for l in set(x)]).items() if v > 1}
    return letters

print(test_1_3(["hello", "world", "python"]))

def test_1_4(strings):
    all_letters = set(string.ascii_lowercase)
    result = all_letters.difference(test_1_2(strings))
    return result

print(test_1_4(["hello", "world", "python"]))
