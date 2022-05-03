# ### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.
#
import string

def quot_replace(string):
    conversion_table = str.maketrans({'"': "'", "'": '"'})
    return string.translate(conversion_table)