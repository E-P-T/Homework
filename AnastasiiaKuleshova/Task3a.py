# Task 2.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form. Examples:
#
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']

def words_sorting():
    words = []
    uniquelist = []
    words = (input("input words:")).split(",")
    for word in words:
        if word not in uniquelist:
            uniquelist.append(word)
    uniquelist.sort()
    print(uniquelist)


words_sorting()
