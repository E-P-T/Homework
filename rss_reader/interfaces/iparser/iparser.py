
from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def create_parser(self, markup: bytes, features: str = 'xml') -> None:
        pass
