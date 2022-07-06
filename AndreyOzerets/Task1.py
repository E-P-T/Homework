# Task 7.1


class MyOpen:
    def __init__(self, file, mode='r') -> None:
        self._file = file
        self._mode = mode
        self._file_obj = None

    def __enter__(self):
        self._file_obj = open(self._file, self._mode)
        return self._file_obj
