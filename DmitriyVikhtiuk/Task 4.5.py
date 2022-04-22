def split_by_index(i):
    str_num = str(i)
    l = [int(c) for c in str_num]
    return tuple(l)
num = int(input("number: "))
print(split_by_index(num))