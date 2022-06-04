# Task 6.1


def type_validator(type_=int):
    """Argument type validator"""

    def decorator(func):
        def wrapper(self, value):
            if isinstance(value, type_) or value is None:
                func(self, value)
            else:
                raise TypeError('{} must be a {}'.format(value, type_))
        return wrapper
    return decorator


class Counter():

    def __init__(self, start=0, stop=None) -> None:
        self.start = start
        self.stop = stop

    @property
    def start(self):
        return self._start

    @start.setter
    @type_validator()
    def start(self, value):
        self._start = value
