str = input("Please set string: ")

def splitString(a = str):

    words = []
    current_word = ""


    for char in a:
        if char == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    words.append(current_word)
    return words
print(splitString())
