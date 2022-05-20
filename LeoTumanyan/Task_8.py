### Task 7.8
# TODO: Implement your custom iterator class called MySquareIterator which gives squares of elements of
#  collection it iterates through.


class MySquareIterator:
    def __init__(self, items):
        self._data = items

    def __iter__(self):
        for i in self._data:
            yield i ** 2


lst = [1, 2, 3, 4, 5]

itr = MySquareIterator(lst)
for item in itr:
    print(item, end=' ')
# >>> 1 4 9 16 25
