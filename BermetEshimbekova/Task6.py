# Task 4.6

def get_shortest_word(s: str):
    words = s.split()
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)


get_shortest_word('Python is simple and effective!')
get_shortest_word('Any pythonista like namespaces a lot.')
