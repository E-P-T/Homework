def foo(my_list):
    res=[]
    for index in range(len(my_list)):
        mult=1
        for i in range(len(my_list)):
            if i != index:
                mult*=my_list[i]
        res.append(mult)

    return res
if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))