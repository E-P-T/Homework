# Task 7.9

def typed_prop(name, expectrd_type):
    """Type checking"""

    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expectrd_type):
            raise TypeError(f'{name} must be a {expectrd_type}')
        setattr(self, storage_name, value)

    return prop


class EvenRange:
    start = typed_prop('start', int)
    stop = typed_prop('stop', int)

    def __init__(self, start: int, stop: int) -> None:
        """Initializer.

        :param start: Countdown start.
        :type start: int
        :param stop: End of countdown.
        :type stop: int
        """
        self.start = start
        self.stop = stop
        self.number = start
        self._text = "Out of numbers!"
        self._end_of_iteration = False
        self._for_loop = False

    def __iter__(self):
        self._for_loop = True
        return self

    def __next__(self):

        while self.start < self.stop:
            if self.start % 2 == 0:
                self.number = self.start
                self.start += 1
                return self.number
            else:
                self.start += 1
        else:
            if not self._end_of_iteration:
                self._end_of_iteration = True
                return self._text

        if not self._for_loop:
            return self._text

        raise StopIteration
