"""Implement a function `get_shortest_word` which returns the
longest word in the given string"""

def get_shortest_word(s):
    list_w = s.split(" ")
    res, len_res = list_w[0], len(list_w[0])
    for i in list_w:
        if len(i)>len_res:
            res, len_res = i, len(i) 
    return res

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("The longest word is: {}".format(get_shortest_word(s)))