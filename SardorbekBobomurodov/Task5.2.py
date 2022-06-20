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

def most_common_words(filepath=r"C:\Users\Sardor\PycharmProjects\Homework\data\lorem_ipsum.txt", number_of_words=3):
    strip_chars = '.,!?:;'
    words = []
    result = {}
    answer = []
    with open(filepath) as file:
        for line in file:
            words += [word.strip(strip_chars) for word in line.split()]
    for word in words:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    sorted_x = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
    for i in sorted_x:
        answer.append(i[0])
    return answer[:number_of_words]


print(most_common_words())
