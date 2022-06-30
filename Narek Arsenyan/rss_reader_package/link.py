"""
Module for Link class

exports Link class
"""

from utils.exceptions import LinkWithNoSourceError


class Link:
    """Class for specifying single Link object"""
    def __init__(self, href, link_type: str = "unknown"):
        """
        The constructor of Link class

        Args:
            href:       source of the link
            link_type:  type of the source
        """

        if href is None or type(href) is not str:
            raise LinkWithNoSourceError("Provided source is missing or of wrong type")
        self.href = href
        self.link_type = link_type

    def __str__(self) -> str:
        """
        The function for overriding string conversion behaviour

        Returns:
            str: formatted string version of Link object
        """

        return f"{self.href} ({self.link_type})"
