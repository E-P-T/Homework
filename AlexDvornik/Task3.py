'''
Task 2.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples: red, white, black, red, green, black
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
'''

seq_of_words = list(map(str, input().split(', ')))
print(sorted(set(seq_of_words)))
