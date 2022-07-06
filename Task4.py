# Task 7.4


class SupressDecorator(ContextDecorator):
    def __init__(self, file) -> None:
        super().__init__()
        self._file = file
