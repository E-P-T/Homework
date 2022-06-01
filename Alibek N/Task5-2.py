import os

path_input = os.getcwd().rstrip('\Alibek N') + '\data' +  '\\' + 'lorem_ipsum.txt'


def most_common_words(path_input, n=3):
    strips = '.,!?:;'
    words = []
    result = {}
    answer = []
    with open(path_input) as file:
        for line in file:
            words += [word.strip(strips) for word in line.split()]
    file.close()
    for word in words:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    sorted_x = sorted(result.items(), key=lambda kv: kv[1]) 
    sorted_x.reverse()
    for i in sorted_x:
        answer.append(i[0])
    return answer[:n]


print(most_common_words(path_input))

