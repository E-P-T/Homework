"""
Implement your custom iterator class called MySquareIterator which gives squares
of elements of collection it iterates through.
"""

class MySquareIterator:
    def __init__(self, mylist):
        self.mylist = mylist
        self.pointer = 0  # index pointer for the iterable ibject

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer <= len(self.mylist)-1:
            cur = self.mylist[self.pointer]
        else:
            raise StopIteration
        res = cur**2
        self.pointer += 1
        return res

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
