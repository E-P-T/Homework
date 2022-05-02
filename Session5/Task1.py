"""
### Task 4.1
Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
`sorted_names.txt`. Each name should start with a new line as in the following example:

```
Adele
Adrienne
...
Willodean
Xavier
```
"""
import os
names = []
with open("C:/Users/hopoghosyan/Desktop/HPHomework/Homework-session_5/data/unsorted_names.txt", "r") as f:
    for n in f.readlines():
        names.append(n)
names.sort()
with open("C:/Users/hopoghosyan/Desktop/HPHomework/Homework-session_5/data/sorted_names.txt", "w") as sorted_f:
    for n in names:
        sorted_f.write(n)



