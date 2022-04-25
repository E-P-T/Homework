def firstItem(item):
    return item[0]

def most_common_words(filepath, number_of_words = 3):
    a = open(filepath, 'r')
    dict = {}
    for x in a.readlines():
        c = x.replace(",","").replace(".","").replace('\n','').lower().split()
        for n in c:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
    a.close()
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    g = list(map(firstItem, sorted_dict[-number_of_words:]))
    g.reverse()
    print(g)
most_common_words("../data/lorem_ipsum.txt")
