# ### Task 2.3.1
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']
# ```

def print_sorted_list(list1):
    list3 = list(set(list1))
    print(sorted(list3))