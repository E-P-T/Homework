from collections import OrderedDict
dictOne = {' ': 8, 'e': 3, 'd': 1, 'g': 1, 'f': 1, 'i': 5, 'h': 1, 'm': 5, 'l': 2, 'o': 2, 'n': 2, 'p': 3, 's': 3, 'r': 2, 'u': 2, 't': 4, 'y': 2, 'x': 1}
sorted_dict = sorted(dictOne.items(), key = lambda kv: kv[0])
print(dict(sorted_dict))