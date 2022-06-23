
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
