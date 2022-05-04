def most_common_words(filepath, number_of_words=3):
    l = []
    count = 0
    with open(filepath) as file:
        strings = file.read()
    one_string = strings.replace("\n", "")
    one_string = one_string.replace(",", " ")
    one_string = one_string.replace(".", " ")
    one_string = one_string.lower()
    list_of_words = one_string.split()
    dict_of_words = {word: list_of_words.count(word) for word in list_of_words}
    while count != number_of_words:
        for key, value in dict_of_words.items():
            if dict_of_words[key] == max((dict_of_words.values())):
                l.append(key)
                dict_of_words.pop(key)
                break
        count += 1
    return l


print(most_common_words("lorem_ipsum.txt"))
