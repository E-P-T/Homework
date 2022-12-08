def get_pairs(lst):
    res=[]
    my_tuple=[]
    for i in range(1,len(lst)):
        my_tuple.append(lst[i-1])
        my_tuple.append(lst[i])
        res.append(tuple(my_tuple))
        my_tuple.clear()
    print(res)

if __name__ == '__main__':
    get_pairs(['need', 'to', 'sleep', 'more'])