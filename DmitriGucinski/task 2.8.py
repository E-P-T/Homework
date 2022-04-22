# Write a program which makes a pretty print of a part of the multiplication table. Examples:

# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7	
# 2	6	8	10	12	14	
# 3	9	12	15	18	21	
# 4	12	16	20	24	28

a = 2
b = 4
c = 3
d = 7

num_list2d = []
for i, value in enumerate(range(a,b+1)):
    num_list2d.append([])
    for k in range(c,d+1):
        num_list2d[i].append(value*k)     

for r in range(c,d+1):
    print('{:3}'.format(r), end=" ")
print()    
 
f_col  = range(a,b+1)
c = 0    
for i in range(len(num_list2d)) : 
    print('{:<2}'.format(f_col[c]), end="")
    c += 1
    for j in range(len(num_list2d[i])) : 
        print('{0:<3}'.format(num_list2d[i][j]), end=" ")        
    print()
    
        