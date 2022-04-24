# Task 5.1
# Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new file called sorted_names.txt.
# Each name should start with a new line as in the following example:
#
# Adele
# Adrienne
# ...
# Willodean
# Xavier


def sort_file(filepath):

    """ Open file, sort the names and write them to a new file.
        Each name should start with a new line """

    names = list()
    with open(filepath, 'r') as fd:
        for name in fd.readlines():
            names.append(name)
    names.sort()
    with open('sorted_names.txt', 'w') as new_fd:
        for name in names:
            new_fd.write(name)
