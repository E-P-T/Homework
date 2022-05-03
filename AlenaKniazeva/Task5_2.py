"""This program implements a function which search for most common words in the file"""

from collections import OrderedDict
import itertools

def most_common_words(filepath, number_of_words=3):
    with open (filepath, 'r') as f:
        wdict = {}
        for line in f:
            if line != '\n':
                # create list of words of the read line
                list_line = line.lower().strip('\n').split(' ')
                for word in list_line:
                    new_word = word.strip(',.')
                    # iterate by words from list and check whether word is in dictionary
                    if new_word in wdict:
                        wdict[new_word] +=1
                    else:
                        wdict[new_word] = 1
        # create ordered dictionary sorted by values in descending order
        sorted_dict = OrderedDict(sorted(wdict.items(), key=lambda x: x[1], reverse=True))
        # return first number_of_words elements of the ordered dictionary
        return list(itertools.islice(sorted_dict.items(), 0, number_of_words))

if __name__ == "__main__":
    fname = input("Enter a filename: ")
    num_word = int(input("Enter the needed number of common words: "))
    print(most_common_words(fname, num_word))