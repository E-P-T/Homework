# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form. Examples:

# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white']

sequence_of_words = ('red', 'white', 'black', 'red', 'green', 'black')

# 1
print( 'result1 = {}'.format(sorted(set(sequence_of_words))) )

output = []
output = [word for word in sequence_of_words if word == 'black']

output.sort()

print('result3 = {}'.format(output))    
        
# 2
output = []
for word in sequence_of_words:
    if word not in output:
        output.append(word)

output.sort()

print('result2 = {}'.format(output))