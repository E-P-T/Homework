# Write a Python program to sort a dictionary by key.
from collections import OrderedDict

my_dict = {"Instrument": "guitar", "Car": "Volvo", "Type": "Object", "Container": "Dictionary"}

sorted_dict = OrderedDict()
for i in sorted(my_dict):
    sorted_dict[i] = my_dict[i]
    print("{:20} -> {:20}".format(i, my_dict[i]))

print("Result {}".format(sorted_dict))