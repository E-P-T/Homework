a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))


m1_list = list(''.join((str(a), str(b), str(c), str(d))))
m2_list = list(''.join((str(a), str(b), str(c), str(d))))

print("*** Multiplication table ***")
print()
print(('\t'.join(m2_list)).rjust(11, ' '))
for i in range(len(m1_list)):
    line = []
    line.append(m1_list[i])
    for j in range(len(m2_list)):
        line.append(str(int(m1_list[i]) * int(m2_list[j])))
    print('\t'.join(line))

