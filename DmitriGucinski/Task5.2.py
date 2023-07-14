#Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.
import collections

data_path = '/home/python/code/epam/workingcopy/EpamPythonHomework/data/'
inputfile = data_path + 'lorem_ipsum.txt'

def most_common_words(filepath, number_of_words=3):
    strip_chars = '.,!?:;'
    words = []
    with open(filepath) as file:
        for line in file:
            words += [word.strip(strip_chars) for word in line.split()]

    frequency = collections.OrderedDict(collections.Counter(words))
    frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

    return [word for i, word in enumerate(frequency) if i < number_of_words]

print(
    most_common_words(inputfile, 3)
)
