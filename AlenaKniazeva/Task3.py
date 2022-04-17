"""This program accepts a comma separated sequence of words as input 
and prints the unique words in sorted form"""

def unique_words(s):
    set_s = set()
    for word in s.split(','):
        set_s.add(word.strip(' \''))
    return set_s

if __name__ == "__main__":
    input_str = input("Enter a comma separated sequence of words: ")
    print("Unique words are: {}".format(sorted(unique_words(input_str))))