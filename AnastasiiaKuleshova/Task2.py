# ### Task 2.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# ```

def countUniqueSymbolsInString(line):
    dict = {}
    for symbol in line:
        if symbol not in dict:
            dict[symbol] = 1
        else:
            dict[symbol] += 1
    print(dict)


print("input string")
enteredLine = input()
countUniqueSymbolsInString(enteredLine)