int_tuple = (1, 2, 3, 4)
L = [str(i) for i in int_tuple]
integer = int(''.join(L))
print(integer)
print(type(integer))
