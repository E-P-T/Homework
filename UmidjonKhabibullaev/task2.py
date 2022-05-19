def most_common_words(filepath, number_of_words = 3) -> list:
    """ Function which receives a path to a text file and 
        finds the most common `number_of_words` words.
        Returns the list of such words.
    """
    ### Read from a file and store its content in a string ###
    with open(filepath, "r") as f:
        text = f.read()
    
    non_letters = set() # the set of all characters in `text` that are not alphabetical letters
    for char in text:
        if char != " " and not char.isalpha():
            non_letters.add(char)
    
    ### Remove all non letter characters ###
    for non_letter in non_letters:
        text = text.replace(non_letter, "")

    ### Separate all words for statistics ###
    all_words = text.split()
    all_words = [word.lower() for word in all_words]

    unique_words = set(all_words)
    words_count = {
        word: 0
        for word in unique_words
    }

    ### Count words ###
    for word in all_words:
        words_count[word] += 1
    
    sorted_words = sorted(words_count.items(), key = lambda item: item[1])
    
    common_words = [pair[0] for pair in sorted_words[-number_of_words:]]
    
    return common_words
    


if __name__ == "__main__":
    file = "../data/lorem_ipsum.txt"
    print(most_common_words(file))