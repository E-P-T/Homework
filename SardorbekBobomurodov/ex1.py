def ex1(str):
    count = 0
    for x in str:
        count += 1
    print(count)


if __name__ == '__main__':
    while True:
        text = input("Enter your str: ")
        ex1(text)
