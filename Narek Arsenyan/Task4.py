str = input("Please set string: ")
ind = input("Please set indexes: ")

def splitString(current_word = str, indexes = ind):

    words = []
    previousIndex = 0
    for n in indexes:
        if n <= len(current_word):
            words.append(current_word[previousIndex:n])
            previousIndex = n
        else:
            words.append(current_word)
            return words
    if indexes[len(indexes) - 1] < len(current_word):
        words.append(current_word[indexes[len(indexes) - 1]:])
    return words
print(splitString())
