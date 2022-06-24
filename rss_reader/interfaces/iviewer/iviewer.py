"""This module contains a set of interfaces for data viewers."""


from __future__ import annotations
from abc import ABC, abstractmethod


class IViewHandler(ABC):
    """Interface for a parser."""

    @abstractmethod
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain."""
        pass

    @abstractmethod
    def show(self, data: dict) -> None:
        """Show data."""
        pass
