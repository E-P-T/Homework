class MySquareIterator:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.tmp = self.lst[:]
        return self

    def __next__(self):
        if self.tmp == []:
            raise StopIteration
        else:
            return self.tmp.pop(0) ** 2


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)

for item in itr:
    print(item)

# 1 4 9 16 25
