"""This program makes a pretty print of a part of
the multiplication table in ranges [a,b] and [c,d]"""

import pandas as pd

def pretty_mult(a, b, c, d):
    # fill the table
    data = {}
    for j in range(c,d+1):
        list_j = [i*j for i in range(a,b+1)]
        data[j] = list_j
    # fill names of rows of the table
    ind_x = [i for i in range(a,b+1)]
    
    frame = pd.DataFrame(data,columns = data.keys(), index = ind_x)
    print(frame)

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))
    pretty_mult(a,b,c,d)
