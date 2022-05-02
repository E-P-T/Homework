def get_pairs(list_in):
    temp_list=[]
    if len(list_in) > 2:
        for i in range(len(list_in)-1):
            temp_list.append((list_in[i], list_in[i+1]))
    else: return
    return(temp_list)

a=[1, 2, 3, 8, 9]
b=['need', 'to', 'sleep', 'more']
c=[1]
print(get_pairs(a))
print(get_pairs(b))
print(get_pairs(c))