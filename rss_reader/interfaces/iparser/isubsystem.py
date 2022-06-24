
from abc import ABC, abstractmethod
from typing import Iterable


class ISubsystem(ABC):

    def find_all(self, name: str = None, limit: int = None) -> Iterable:
        pass

    def select(self, selector: str, limit: int = None) -> Iterable:
        pass
