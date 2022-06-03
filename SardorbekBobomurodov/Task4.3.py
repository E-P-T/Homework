def main(input_txt):
    list = []
    temp = ''
    for char in input_txt:
        if char == " ":
            list.append(temp)
            temp = ''
        else:
            print("Before %s" % id(temp))
            temp += char
            print("After %s" % id(temp))
    if temp is not None:
        list.append(temp)
        print(list)


if __name__ == "__main__":
    while True:
        input_str = input("Input a string: ")
        main(input_str)
