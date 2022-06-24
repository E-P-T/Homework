
from abc import ABC, abstractmethod


class ISubsystem(ABC):

    def find_all(self, name: str = None, limit: int = None) -> Iterable:
        pass
