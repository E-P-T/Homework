class MySquareIterator:                                             
    def __init__(self, collection):
        self.collection = collection
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection) - 1:
            self.index += 1
            return self.collection[self.index] ** 2
        else:
            raise StopIteration

itr = MySquareIterator([1, 2, 3, 4, 5])
for item in itr:
    print(item, end = " ")
