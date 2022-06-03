def main(text, indices):
    print(type(indices))
    split_list = []
    temp = 0
    for index in indices:
        split_list.append(text[temp:index])
        print(id(temp))
        temp = index
        print(id(temp))
        print('\n')

    print(split_list)


if __name__ == "__main__":
    main("no luck?", [42])
