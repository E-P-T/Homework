"""Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse)."""



def my_split(text: str, splitter=" "):
    """This function takes string data and splitter, returns list of word split by splitter."""
    out_list = []
    index = 0
    while True:
        fnd = text.find(splitter, index)
        if fnd == -1:
            out_list.append(text[index:])
            break
        out_list.append(text[index:fnd])
        index = fnd + 1
    return out_list




if __name__ == '__main__':
    example = "Hello, my name is Wolly!"
    print(my_split(example))
    example_2 = "hello, my, dear, friend, where, is, your, flowers"
    print(my_split(example_2, ", "))