#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.7 Write a program which makes a pretty print of a part of the multiplication table.')

final = []

start = True
while start:
    a = input('Please, type the first num for vertical column (a): ')
    b = input('Please, type the second num for vertical column (b): ')
    c = input('Please, type the first num for horizontal column (c): ')
    d = input('Please, type the second num for horizontal column (d): ')

    if a.isdecimal() and b.isdecimal() and c.isdecimal() and d.isdecimal():
        a = int(a); b = int(b); c = int(c); d = int(d)
        if a < b and c < d:
            for i in range(a, b + 1):
                new = str(i)
                header = ''
                for j in range(c, d + 1):
                    header += f'\t\t{j}'
                    new += f'\t\t{i*j}'
                final.append(new)
            final.insert(0, header)

            print(f'Multiplication Table for {a} - {b} on {c} - {d}')
            for line in final:
                print(line)

            start = False
        else:
            print('Please, make sure to enter integers the way that a < b and c < d')
    else:
        print('Please, make sure to type only integers')


# hope you enjoyed it