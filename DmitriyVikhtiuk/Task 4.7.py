def create_list():
    st = input("write your numbers for int list, separated by comma like this(2, 3, 5, 6): ")
    list_of_charnum = st.split(", ")
    list_of_num = [int(num) for num in list_of_charnum]
    return list_of_num
list_num = create_list()
def mult_num(list):
    mult = 1
    for num in list:
        mult *= num
    final_list = [int(mult/num) for num in list]
    return final_list
print(mult_num(list_num))
