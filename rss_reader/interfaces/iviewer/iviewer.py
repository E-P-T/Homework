"""This module contains a set of interfaces for data viewers."""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IViewHandler(ABC):
    """Interface for a parser."""

    @abstractmethod
    def set_next(self, handler: IViewHandler) -> IViewHandler:
        """Set the next viewer in the handler chain.

        :param handler: Next handler.
        :type handler: IViewHandler
        :return: Handler.
        :rtype: IViewHandler
        """
        pass

    @abstractmethod
    def show(self, data: List[dict]) -> None:
        """Show data.

        :param data: Dictionary with data to be printed on the screen.
        :type data: dict
        """
        pass
