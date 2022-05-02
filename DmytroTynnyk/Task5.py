def get_digit(num_in):
    return(tuple(i for i in (str(num_in))))
print(get_digit(int(input('Enter a numbers: '))))