def ex4(num):
    listNum = []
    print(id(listNum))
    for n in range(1, num + 1):
        if num % n == 0:
            listNum.append(n)
    print(listNum)
    print(id(listNum))


if __name__ == "__main__":
    while True:
        val = input("Input a number: ")
        ex4(int(val))
