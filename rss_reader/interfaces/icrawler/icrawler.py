"""This module contains a set of interfaces for the crawler."""

from abc import ABC, abstractmethod


class ICrawler(ABC):
    """Interface for a crawler."""

    @abstractmethod
    def get_data(self) -> bytes:
        """Get the content of the requested page.

        :return: Returns the result as a byte string.
        :rtype: bytes
        """
        pass
