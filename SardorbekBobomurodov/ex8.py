def ex8(integer_tuple):
    print("    %d  %d  %d  %d" % (integer_tuple[0], integer_tuple[1], integer_tuple[2], integer_tuple[3]))
    for num in integer_tuple:
        print("%d   %d  %d  %d  %d" % (
            num, integer_tuple[0] * num, integer_tuple[1] * num, integer_tuple[2] * num, integer_tuple[3] * num))


if __name__ == '__main__':
    count = 0
    integer_tuple = []
    while count < 4:
        val = input("Enter integer: ")
        integer_tuple.append(int(val))
        count += 1
    ex8(integer_tuple)
