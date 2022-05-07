'''
Task 5.1
Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`.
Each name should start with a new line as in the following example:
```
Adele
Adrienne
...
Willodean
Xavier
'''
from typing import List


def read_file(path: str):
    with open(path, 'r') as inf:
        list_of_names = [line.rstrip('\n') for line in inf]
        return sorted(list_of_names)


def write_file(fname: str, lst: List[str]):
    with open(fname, 'w') as outf:
        for name in lst:
            outf.write("%s\n" % name)


if __name__ == '__main__':
    fpath = 'data/unsorted_names.txt'  # there might be different path
    write_file('data/sorted_names.txt', read_file(fpath))
