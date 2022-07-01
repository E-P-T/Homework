"""This module contains a set of interfaces for the loader."""

from __future__ import annotations
from abc import ABC, abstractmethod


class IHandler(ABC):
    """Interface for receiving data."""

    def get_data(self, tag_name: str,
                 title_tag: str,
                 source: str,
                 limit: int) -> dict:
        """Return a dictionary with parsed data.

        :param tag_name: The name of the tag in which the news is stored.
        :type tag_name: str
        :param title_tag: The name of the tag in which the name
                            of the rss resource is stored.
        :type title_tag: str
        :param source: Resource URL.
        :type source: str
        :param limit: Number of news items to display.
        :type limit: int
        :return: Dictionary with parsed data.
        :rtype: dict
        """
        pass


class ILoadHandler(ABC):
    """Interface for loaders data."""

    @abstractmethod
    def set_next(self, handler: ILoadHandler) -> ILoadHandler:
        """Set the next viewer in the handler chain.

        :param handler: Next handler.
        :type handler: ILoadHandler
        :return: Handler.
        :rtype: ILoadHandler
        """
        pass

    @abstractmethod
    def get_data(self) -> list:
        """Get the requested data.

        :return: List with data.
        :rtype: list
        """
        pass
