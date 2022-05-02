"""
Task 4.2
Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.

def most_common_words(filepath, number_of_words=3):
    pass
print(most_common_words('lorem_ipsum.txt'))
> ['donec', 'etiam', 'aliquam']
NOTE: Remember about dots, commas, capital letters etc.
"""

def most_common_words(filepath, number_of_words):

    Dict = {}
    with open(filepath, "r") as f:

        for line in f:
            line = line.replace(",","").replace(".","").replace('\n','').lower().split()
            if line == []:
                continue
            for word in line:
                if Dict.get(word, False):
                    Dict[word] += 1
                else:
                    Dict[word] = 1
    Dict = sorted(Dict.items(), key=lambda item: item[1], reverse=True)
    result = list(map(lambda item: item[0], Dict[:number_of_words]))
    return result


words = most_common_words('C:/Users/hopoghosyan/Desktop/HPHomework/Homework-session_5/data/lorem_ipsum.txt', 2)
print(words)