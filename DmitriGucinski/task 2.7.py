# Write a Python program to convert a given tuple of positive integers into an integer. Examples:

# Input: (1, 2, 3, 4)
# Output: 1234

my_tuple = (1, 2, 3, 4)

def convert_tuple_to_int(tuple_var):
    tuple_string = ''
    for s in my_tuple:
        tuple_string += str(s)
    return int(tuple_string)
    
int_var = convert_tuple_to_int(my_tuple)     
print(int_var)
print(type(int_var))
