
def get_shortest_word(string):
    non_word_symbols = "\t\n,.!"

    words = sorted(
        {
            len(word.strip(non_word_symbols)): word.strip(non_word_symbols) for word in string.split(" ")
        }
        .items()
    )
    print(words)
    return words[0][1]


def get_longest_word(string):
    non_word_symbols = "\t\n,.!"

    words = sorted(
        {
            len(word.strip(non_word_symbols)): word.strip(non_word_symbols) for word in string.split(" ")
        }
        .items(), reverse=True)

    print(words)
    return words[0][1]


print(
    get_shortest_word('Python is simple and effective!')
)

print(
    get_longest_word('Python is simple and effective!')
)
