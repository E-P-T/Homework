### Task 5.2

# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

# ```python
# def most_common_words(filepath, number_of_words=3):
#     pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# ```

# > NOTE: Remember about dots, commas, capital letters etc.

def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as lora:
        a = lora.read()
        wc = {}
        for word in a.lower().split():
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            if word not in wc:
                wc[word] = 1
            else:
                wc[word] += 1
        new = [k for k, v in sorted(wc.items(), key=lambda item: item[1], reverse=True)]
        return [new[i] for i in range(number_of_words)]