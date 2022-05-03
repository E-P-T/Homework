# Task 5.1
# Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new
# file called sorted_names.txt. Each name should start with a new line as in the following example:
#
# Adele
# Adrienne
# ...
# Willodean
# Xavier
import os

names = []
path_to_unsorted_file = '..\\data\\unsorted_names.txt'
path_to_sorted_file = '.\\data\\Task1_sorted_names.txt'

full_path_unsorted_file = os.path.abspath(path_to_unsorted_file)

try:
    with open(full_path_unsorted_file, 'r') as unsorted_names:
        names = unsorted_names.readlines()
except FileNotFoundError:
    print("unsorted_names doesn't exist")

names.sort()
names_str = ''.join(names)

with open(os.path.abspath(path_to_sorted_file), 'w') as sorted_names:
    sorted_names.write(names_str)
