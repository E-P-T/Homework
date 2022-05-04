# ### Task 2.4
# Write a Python program to sort a dictionary by key.
#
def dict_sorted(data) -> dict:
    new_dict = {key: value for (key, value) in sorted(data.items())}
    return new_dict