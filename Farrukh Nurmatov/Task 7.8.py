"""Implement your custom iterator class called MySquareIterator which gives
squares of elements of collection it iterates through."""


class MySquareIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for char in self.lst:
            yield char ** 2


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")
