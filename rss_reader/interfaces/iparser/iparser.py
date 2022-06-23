
from abc import ABC, abstractmethod
from typing import Generator, List


class IParser(ABC):
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
        pass
