from __future__ import annotations
from abc import ABC, abstractmethod


class IViewHandler(ABC):
    @abstractmethod
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain."""
        pass

    @abstractmethod
    def show(self, data: dict):
        pass
