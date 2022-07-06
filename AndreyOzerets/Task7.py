# Task 7.7

def typed_prop(name, expectrd_type):
    """Type checking"""

    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if isinstance(value, expectrd_type) and \
                self._validate(value, f'{self.__class__.__name__} supports only numbers!'):
            setattr(self, storage_name, value)
        else:
            raise TypeError(
                f'{self.__class__.__name__} supports only numbers!')

    return prop


class MyNumberCollection:
    start = typed_prop('start', (int, Iterable))
    stop = typed_prop('stop', (int, Iterable, type(None)))
    step = typed_prop('step', (int, Iterable, type(None)))

    def __init__(self, start, stop=None, step=None) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        self._collection: List[int] = []
        self._init_collection()
