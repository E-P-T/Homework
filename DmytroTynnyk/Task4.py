def split_by_index(str_in, idx_list):
    list_out=[]
    if len(str_in)>max(idx_list):
        list_out.append(str_in[:idx_list[0]])
        for i in range(len((idx_list))-1):
            list_out.append(str_in[idx_list[i]:idx_list[i+1]])
        list_out.append(str_in[idx_list[len(idx_list)-1]:])
    else: list_out.append(str_in)
    return(list_out)

# a="pythoniscool,isn'tit?"
b=[6, 8, 12, 13, 18]
a="pythoniscool,isn'tit?"
# b=[42]
print(split_by_index(a,b))