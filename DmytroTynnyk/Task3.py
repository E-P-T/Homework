def my_split(str_in, separ_str):
    list_out=[]
    str_append=''
    i=0
    while i<=len(str_in)-1:
        if str_in[i:i+len(separ_str)] == separ_str:
            list_out.append(str_append)
            str_append=''
            i+=len(separ_str)-1
        else:
            str_append+=str_in[i]
        i+=1
    list_out.append(str_append)
    return(list_out)

print(my_split(input('Enter a string: '), input('Enter a separate: ')))