"""Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
`sorted_names.txt`. Each name should start with a new line as in the following example:

```
Adele
Adrienne
...
Willodean
Xavier
```"""

names = []

with open("data/unsorted_names.txt", "r") as read_file,\
        open("data/sorted_names.txt", "w") as write_file:
    for line in read_file:
        names.append(line)
        names.sort()
    for name in names:
        write_file.write(name)
