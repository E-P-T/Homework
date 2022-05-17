class MySquareIterator:
    def __init__(self, lst):
        self.list = lst
        self.num = 0
        self.res = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.res < self.list[-1] ** 2:
            self.res = self.list[self.num] ** 2
            self.num += 1
            return self.res
        else:
            raise StopIteration





lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
