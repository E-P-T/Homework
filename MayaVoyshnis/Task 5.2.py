def most_common_words(filepath, number_of_words=3):
    with open(filepath, "r") as unsorted_file:
        text = unsorted_file.read().replace(',', '').replace('.', '').replace('\n', '').lower().split(' ')
    set_text = list(set(text))
    cnt = [text.count(word) for word in set_text]
    res = []
    for i in range(number_of_words):
        res.append(set_text[cnt.index(max(cnt))])
        cnt[cnt.index(max(cnt))] = 0
    return res


print(most_common_words('../data/lorem_ipsum.txt', 5))