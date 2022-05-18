# Task 7.8
# Implement your custom iterator class called MySquareIterator which gives squares of elements
# of collection it iterates through. Example:
#

class MySquareIterator:
    def __init__(self, input_list):
        self.list = input_list

    def __iter__(self):
        for elem in self.list:
            yield elem ** 2


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
