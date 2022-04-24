'''
### Task 2.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:
```
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white']
```
'''

# Sample input
# red, white, black, red, green, black
# lol, kek, aa, ds, a, a, aa, b, TTT, What?, What
input_sequence = input()
input_sequence_list = input_sequence.replace(' ', '')
input_sequence_list = input_sequence_list.split(',')

words = set()
for word in input_sequence_list:
    words.add(word)

words = list(words)
words.sort()
print(words)