# Task 2.3
'''Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form.
Examples:
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']'''

numbers = ['red', 'white', 'black', 'red', 'green', 'black']
unique_list = sorted(set(numbers))
print(unique_list)
