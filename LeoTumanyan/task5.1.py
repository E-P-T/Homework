### Task 5.1

# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`. Each name should start with a new line as in the following example:

# ```
# Adele
# Adrienne
# ...
# Willodean
# Xavier
# ```

with open("../data/unsorted_names.txt", 'r') as nmz:
    d_data = nmz.readlines()
    sorted_list = sorted(d_data)
with open("sorted_names.txt", 'w') as emz:
    for name in sorted_list:
        emz.write(f'{name.strip()}\n')