def minus(list):
    list_for_split = []
    for i in range(len(list)-1):
        list_for_split.append(list[i+1] - list[i])
    return(list_for_split)

def split_by_index(s, l):
    global list_of_ind
    final_list = []
    if list_of_ind[0] != 0:
        new_s = s[:list_of_ind[0]]
        final_list.append(new_s)
        new_s = s[list_of_ind[0]:]
        s = new_s
    else:
        final_list.append(s)
        return final_list
    for i in l:
        new_s = s[:i]
        final_list.append(new_s)
        new_s = s[i:]
        s = new_s
    if s != "":
        final_list.append(s)
    return final_list


st = input("string: ")
li = input("indexes, separated by comma: ")
list_of_char_indexes = li.split(", ")
list_of_ind = [int(c) for c in list_of_char_indexes if int(c) < len(st)]
if list_of_ind == []:
    list_of_ind.append(0)
print(split_by_index(st, minus(list_of_ind)))
