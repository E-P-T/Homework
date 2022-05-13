#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.3 Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.')

words = input('Type a comma separated sequence of words to receive unique words in sorted form: ').strip().replace(' ', '').split(',')

# First version
sorted_unique_words = sorted(set(words))
print(f'The unique words in sorted form: {sorted_unique_words} (The first version)')

# Second version
index = 0

while index < len(words):
    if words.count(words[index]) > 1:
        words.remove(words[index])
    else:
        index += 1

for i in range(len(words)):
    for j in range(1, len(words)):
        if words[j] < words[j - 1]:
            words[j], words[j - 1] = words[j - 1], words[j]

print(f'The unique words in sorted form: {words} (The second version)')