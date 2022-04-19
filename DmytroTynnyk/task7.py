def space(num_in):
    out_space=" "
    out_space*=9-len(str(num_in))
    return(out_space)


a = input("Enter a minimum rows range: ")
b = input("Enter a maximum rows range: ")
c = input("Enter a min columns range: ")
d = input("Enter a max columns range: ")
row_str=[]
header=["         "]
for i in range(int(c), int(d)+1):
    header.append(str(i))
    header.append(space(i))
print("".join(list(header)))
for i in range(int(a), int(b)+1):
    row_str.append(str(i))
    row_str.append(space(i))
    for j in range(int(c), int(d)+1):
       row_str.append(str(i*j))
       row_str.append(space(i*j))
    print("".join(list(row_str)))
    row_str.clear()