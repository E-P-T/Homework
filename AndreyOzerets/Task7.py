# Task 7.7

from collections.abc import Iterable
from typing import List


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

    def append(self, value):
        """Add item to the collection."""
        if self._validate(value, f"'string' - object is not a number!"):
            self._add_el(value)

    def _init_collection(self) -> None:
        """Complete the original list."""
        if isinstance(self.start, Iterable):
            self._add_el(self.start)
        else:
            self._collection = [i for i in range(self.start, self.stop,
                                                 self.step)
                                ] + [self.stop]

    def _add_el(self, value) -> None:
        """Add items to the list."""

        if isinstance(value, Iterable):
            for i in value:
                if isinstance(i, Iterable):
                    self._add_el(i)
                else:
                    self._collection.append(i)
        else:
            self._collection.append(value)

    def _validate(self, value, message) -> bool:
        """Check if the passed value is not a string."""
        if isinstance(value, Iterable):
            for i in value:
                if isinstance(i, Iterable) and not isinstance(i, str):
                    self._validate(i, message)
                if isinstance(i, (str)):
                    raise TypeError(message)
        return True

    def __str__(self) -> str:
        return f'{self._collection}'

    def __getitem__(self, item):
        return self._collection[item] ** 2

    def __add__(self, other):
        return self._collection + other._collection

    def __iter__(self):
        for i in self._collection:
            yield i
