class MySquareIterator:

    def __init__(self, list):
        self.list = iter(list)

    def __iter__(self):
        return self

    def __next__(self):
        return self.list.__next__()


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=' ')
    print()