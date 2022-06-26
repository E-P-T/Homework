"""This module contains a set of interfaces for savers."""

from __future__ import annotations
from abc import ABC, abstractmethod


class ISaveHandler(ABC):
    @abstractmethod
    def set_next(self, handler: ISaveHandler) -> ISaveHandler:
        """Set the next saver in the handler chain.

        :param handler: Next handler.
        :type handler: ISaveHandler
        :return: Handler.
        :rtype: ISaveHandler
        """

        pass

    def save(self, data: dict):
        """Save data.

        :param data: Dictionary with data to save.
        :type data: dict
        """
        pass
