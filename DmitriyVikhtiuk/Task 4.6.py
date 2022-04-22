def get_shortest_word(s):
    l = s.split()
    final_word = l[0]

    max = len(l[0])
    for word in l:
        if len(word) > max:
            max = len(word)
            final_word = word
    return final_word


inp = input("give me a string: ")
danger_list = ["\n", "\t", "\f", "\a", "\v", "\r", "\b"]
for c in danger_list:
    inp = inp.replace(f"{c}", " ")

print(get_shortest_word(inp))

