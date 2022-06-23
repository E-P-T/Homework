
from abc import ABC, abstractmethod


class ICrawler(ABC):
    def get_data(self) -> bytes:
        pass
