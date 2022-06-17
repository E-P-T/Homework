# Task 5.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as an example.

# ```python
# def most_common_words(filepath, number_of_words=3):
#     pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# ```

# > NOTE: Remember about dots, commas, capital letters etc.

def most_common_words(filepath="data/lorem_ipsum.txt", number_of_words=3):
    with open(filepath, mode='r') as file:
        words = str([x for x in file if x != '\n'])
        words = words.replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()
        words = [x.lower() for x in words]

        set_words = set(words)

        dict_words = dict()
        for i in set_words:
            dict_words[i] = words.count(i)
        dict_words = sorted(dict_words.items(), key=lambda i: i[1], reverse=True)
        dict_words = dict_words[0:number_of_words]

        result = []
        for i in range(len(dict_words)):
            result.append(dict_words[i][0])
        return result

print(most_common_words())
