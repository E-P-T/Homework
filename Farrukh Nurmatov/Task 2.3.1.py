"""Write a Python program that accepts a comma separated sequence of
   words as input and prints the unique words in sorted form.

    Input: ['red', 'white', 'black', 'red', 'green', 'black']
    Output: ['black', 'green', 'red', 'white', 'red']"""

input_seq = ['red', 'white', 'black', 'red', 'green', 'black']
unique_words = list(set(input_seq))

print("Output:", sorted(unique_words), sep=" ")