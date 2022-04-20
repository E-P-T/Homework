### Task 2.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# ```

string = 'Oh, it is python'
print('Input: \'' + string + '\'')
string = string.lower()
characters = set(string)
output = {}
for i in characters: output[i] = 0
for i in string: output[i] += 1
print('Output:', output)