# Task 2.1 Write a Python program to calculate the length of a string without using the `len` function.
from __future__ import unicode_literals
from itertools import count
from pstats import SortKey
from re import L


S1 = "Python is a program language"
count = 0 
for i in S1:
    count += 1
print (count)    

#Task 2.2 Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).

S2 = "Oh, it is python"
D1 = {}
for i in S2:
    if i in D1:
        D1[i] +=1 
    else:
       D1[i] =1  
print (D1)

# Task 2.3.1 Write a Python program that accepts a comma separated sequence of words as input and prints the unique words insorted form.


L1 = ['red', 'white', 'black', 'red', 'green', 'black']
unique_L1 = sorted(set(L1)) 
print(unique_L1)

# Task 2.3.2 Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.

N1 = int(input("Enter a num: "))
L_div=[]
for i in range(1,N1+1):
    if N1 % i == 0:
        L_div.append(i)
print(L_div)


# Task 2.4 Write a Python program to sort a dictionary by key.

Dic4 = {"John":24,"Kim":36,"Anna":55}
print(sorted(Dic4.keys()))



# Task 2.5 Write a Python program to print all unique values of all dictionaries in a list.

L5 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_values = set(val for dic in L5 for val in dic.values())
print(unique_values)

#Task 2.6 Write a Python program to convert a given tuple of positive integers into an integer.


Tup6 = (1, 2, 3, 4)
print (int(''.join(map(str, Tup6))))

# Task 2.7 Write a program which makes a pretty print of a part of the multiplication table.

L7 = [1,2,3,4]
for row in L7:
         print(row,*(f"{row*col:2}" for col in range(3,8)))

