"""### Task 2.2
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
Examples:

Input: 'Oh, it is python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
"""

string = "Oh, it is python"
string = string.lower()
freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(str(freq))
