### Task 4.1
'''Open file `data/unsorted_names.txt` in data folder. Sort the names and write them
to a new file called `sorted_names.txt`.
Each name should start with a new line as in the following example:
Adele
Adrienne
...
Willodean
Xavier
'''

with open("E:/PycharmProjects/Homework/data/unsorted_names.txt", "r") as in_f:
    f = in_f.read().splitlines()
    s_f = sorted(f)
    with open("output/sorted_names.txt", "w") as out_f:
        out_f.write('\n'.join(s_f))
