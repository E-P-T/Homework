def palindrom_check(str_in):
    exclude=(',', '-','.',' ', '?')
    list_forw=[]
    list_rew=[]
    for i in range(len(str_in)):
        if str_in[i].lower() not in exclude: list_forw.append(str_in[i].lower())
        if str_in[len(str_in)-i-1].lower() not in exclude: list_rew.append(str_in[len(str_in)-i-1].lower())
    return(list_rew==list_forw)

# Live on time, emit no evil
# Mr. Owl ate my metal worm
# Do geese see God?
# Was it a car or a cat I saw?
print(palindrom_check(input('Enter a checked string: ')))