class EvenRange:
    def __init__(self, start, end):
        self.end = end
        if start % 2 == 0:
            self.index = start
        else:
            self.index = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.end:
            self.index += 2
            return self.index - 2
        else:
            print('"Out of numbers!"')
            raise StopIteration


myRange = EvenRange(1, 11)
for number in myRange:
    print(number, end = ' ')
yourRange = EvenRange(7, 11)
print(next(yourRange))
print(next(yourRange))
print(next(yourRange))
