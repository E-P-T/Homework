"""This module contains a set of interfaces that describe the work
data parsers.
"""


from abc import ABC, abstractmethod
from typing import Generator, List


class IParser(ABC):
    """Interface for a parser."""

    @abstractmethod
    def create_parser(self, markup: bytes, features: str = 'xml') -> None:
        """Create a parser object.

       :param markup: A string or a file-like object representing markup
                      to be parsed.
       :type markup: bytes
       :param features: Desirable features of the parser to be used. This may
                        be the name of a specific parser ("lxml", "lxml-xml",
                        "html.parser", or "html5lib") or it may be the type
                        of markup to be used ("html", "html5", "xml").
                        Defaults to 'xml'.
       :type features: str, optional
       """

    @abstractmethod
    def get_tags_text(self,
                      selector: str,
                      limit_elms: int = None) -> Generator[str, None, None]:
        """Returns the text stored in the tag(s).

        :param selector: A string containing a CSS selector.
        :type selector: str
        :param limit_elms: The number of elements to return, defaults to None.
        :type limit_elms: int, optional
        :yield: Returns the text of each element.
        :rtype: Generator[str, None, None]
        """
        pass

    @abstractmethod
    def get_items(self,
                  template: dict,
                  name: str,
                  limit_elms: int = None) -> List[dict]:
        """Get a list of found items.

        :param template: Specifies the element search pattern. Represents a
                         dictionary. The keys of the dictionary are the tags
                         to be found, and the value is just a string
                         (for example, 'text'). If you need to find the
                         attributes of a tag, then the value is a list that
                         lists all the attributes you need to search
                         (for example, <media:content height="86"
                         url="https://s.com,
                         then: template = {'title': 'text',
                                           'pubDate': 'text',
                                           'content': ['url', 'title']}).
        :type template: dict
        :param name: The name of the tag in which the news is stored.
        :type name: str
        :param limit_elms: The number of elements to return, defaults to None.
        :type limit_elms: int, optional
        :return: List of found news. The dictionary structure corresponds to
                 the template parameter. For example:
                 [{
                    'title': 'Wisconsin',
                    'pubDate': '2022-06-23T15:52:47Z',
                    'content':{
                        'url': 'https://s.yimg.com/uu/ldskdk',
                        'title': None}}]
        :rtype: List[dict]
        """
        pass
