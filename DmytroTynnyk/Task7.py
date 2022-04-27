import math


def foo(list_in):
    temp_list=[]
    for i in range(len(list_in)):
        temp_list.append(int(math.prod(list_in)/list_in[i]))
    return(temp_list)

a=[1,2,3,4,5]
b=[3,2,1]
print(foo(a))
print(foo(b))