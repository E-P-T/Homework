def generate_squares(val_in):
    val_out={i: i**2 for i in range(1,val_in+1)}
    return(val_out)

print(generate_squares(int(input('Enter a number to squares: '))))