def change_quotes(str_in):
    str_out=''
    if ('"' or '\'') in str_in:
        for i in range(len(str_in)):
            if str_in[i] == '"':
                str_out=str_out+'\''
            elif str_in[i] == '\'':
                str_out = str_out + '"'
            else:
                str_out=str_out+str_in[i]
    else: str_out=str_in
    return(str_out)

print(change_quotes(input('Enetr a string with a any quotes ')))