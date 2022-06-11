# Task 5.1
# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to
# a new file called `sorted_names.txt`. Each name should start with a new line.


with open('data/unsorted_names.txt', mode='r') as file:
    result = ''.join(sorted(list(file)))

with open('data/sorted_names.txt', mode='w') as file:
    file.write(result)

with open('data/sorted_names.txt', mode='r') as file:
    print(*list(file))
