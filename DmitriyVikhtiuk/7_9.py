class EvenRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop



    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            if self.start % 2 == 0:
                res = self.start
                self.start += 2
                return res
            else:
                self.start += 1
                res = self.start
                self.start += 2
                return res
        else:
            print("Out of numbers")
            raise StopIteration("Out of numbers")


er1 = EvenRange(7, 11)
er2 = EvenRange(3, 14)
print(next)
for elem in er2:
    print(elem)