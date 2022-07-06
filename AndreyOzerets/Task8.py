# Task 7.8

from copy import deepcopy


class MySquareIterator:
    def __init__(self, el):
        self._el = deepcopy(el)
        self._len = len(el)
        self._i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._i += 1
        if self._i >= self._len:
            raise StopIteration
        return self._el[self._i]**2
