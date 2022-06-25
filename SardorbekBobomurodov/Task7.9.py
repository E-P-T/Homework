class EvenRange:

    def __init__(self, start, end):
        self.curr = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr % 2 != 0:
            self.curr += 1
        else:
            self.curr += 2

        if self.curr < self.end:
            return self.curr
        else:
            raise StopIteration('Out of numbers')


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    # print(next(er1))
    # print(next(er1))
    for number in er1:
        print(number)
