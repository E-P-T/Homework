# Task 2.4
'''Write a Python program to sort a dictionary by key'''

d = {'lion': 20, 'dog': 10, 'cat': 12}
d_sorted = {}
for i in sorted(d.keys()):
    d_sorted[i] = d[i]
print(d_sorted)
