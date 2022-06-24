
from abc import ABC, abstractmethod
from typing import Iterable


class ISubsystem(ABC):

    def find_all(self, name: str = None, limit: int = None) -> Iterable:
        """Return all tags with the given name.

        :param name: A filter on tag name, defaults to None
        :type name: str, optional
        :param limit: Stop looking after finding this many results,
                      defaults to None.
        :type limit: int, optional
        :return: An iterable object that provides the found elements.
        :rtype: Iterable
        """
        pass

    def select(self, selector: str, limit: int = None) -> Iterable:
        pass
