# Task 7.8
# Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.

# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item)
# >>> 1 4 9 16 25

class MySquareIterator:
    """Custom iterator class which gives squares of elements of collection it iterates through"""
    def __init__(self, collection):
        self.collection = collection
        self.index = -1
        self.stop = len(collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.stop:
            self.index += 1
            return self.collection[self.index] ** 2
        else:
            raise StopIteration

def main():
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    main()

# 1 4 9 16 25