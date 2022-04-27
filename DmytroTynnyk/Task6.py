def get_shotest_word(str_in):
    temp_list=str_in.split(' ')
    idx_max_word=0
    for i in range(len(temp_list)):
        if len(temp_list[idx_max_word]) < len(temp_list[i]):
            idx_max_word=i
    return(temp_list[idx_max_word])

print(get_shotest_word(input('Enter a string: ')))