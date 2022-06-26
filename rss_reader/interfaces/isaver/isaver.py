from __future__ import annotations
from abc import ABC, abstractmethod


class ISaveHandler(ABC):
    @abstractmethod
    def set_next(self, handler: ISaveHandler) -> ISaveHandler:
        pass

    def save(self, data: dict):
        pass
