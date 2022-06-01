#! /usr/bin/env python
# TODO: Open file `data/unsorted_names.txt` in data folder.
# Sort the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier


"""
task_1.py: implemented bunch of functions which read names from the ifile
sort it and write sorted names in ofile.
"""


import timeit
from numpy import average as avg


def get_names_from_file(filepath):
    """
    get_names_from_file: opens file with path <filepath> and reads all file
    content in a list which is returned then.
    """
    return open(filepath).readlines()


def sort_names(names):
    """
    sort_names: sorts name and returns list of sorted names.
    """
    return sorted(names)


def write_sorted_names_to_file(filepath, sorted_names):
    """
    write_sorted_names_to_file: open file with path <filepath> and writes
    sorted names into this file.
    """
    open(filepath, 'w').writelines(sorted_names)


def get_names_sort_write_names_to_new_file(ifilepath, ofilepath):
    """
    get_names_sort_write_names_to_new_file: function dispatcher, which calls
    three another functions which is more unified.
    """
    names = get_names_from_file(ifilepath)
    sorted_names = sort_names(names)
    write_sorted_names_to_file(ofilepath, sorted_names)


def get_names_sort_write_names_to_new_file2(ifilpath, ofilepath):
    """
    get_names_sort_write_names_to_new_file2: reads names from file with path
    <ifilepath>, then sorts it and writes sorted names into the tile with path
    <ofilepath>. Don't follow SRP because it does three actions straight away.
    """
    names = open(ifilepath).readlines()
    open(ofilepath, 'w').writelines(sorted(names))


if __name__ == "__main__":
    ifilepath = "data/unsorted_names.txt"
    ofilepath = "data/sorted_names.txt"
    get_names_sort_write_names_to_new_file(ifilepath, ofilepath)
    get_names_sort_write_names_to_new_file2(ifilepath, ofilepath)

    result = timeit.repeat(
        stmt="get_names_sort_write_names_to_new_file(ifilepath, ofilepath)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.11870810699947469

    result = timeit.repeat(
        stmt="get_names_sort_write_names_to_new_file2(ifilepath, ofilepath)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.12041320879943669

    # As we can see the results are almost the same. Three function calls
    # in the first implementation don't change performance. The first
    # implementation even more readable and follows SRP.
