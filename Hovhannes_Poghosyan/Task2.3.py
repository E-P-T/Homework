""""### Task 2.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:

Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
"""

lst = input("Pls input the word seperated with comma").split(",")

to_set = set(lst)
to_lst = list(to_set)
to_lst.sort()

print(to_lst)

