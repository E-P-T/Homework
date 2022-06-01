# Task 5.1
# Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new file called
# sorted_names.txt. Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier

import os

src_file = os.path.join("..", "data", "unsorted_names.txt")
dst_file = os.path.join("..", "data", "sorted_names.txt")

with open(src_file, 'r') as src, open(dst_file, 'w') as dst:
    dst.writelines(sorted(src.readlines()))
