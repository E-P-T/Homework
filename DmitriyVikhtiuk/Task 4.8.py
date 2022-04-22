def get_pairs(list):
    if len(list) > 1:
        final_list = [(list[i], list[i+1]) for i in range(len(list)-1)]
        return final_list
    else:
        return None
st = input("write your elements for list, separated by comma: ")
list_of_char = st.split(", ")
print(get_pairs(list_of_char))