# Task 7.8

class MySquareIterator:
    def __init__(self, el):
        self._el = deepcopy(el)
        self._len = len(el)
        self._i = -1
