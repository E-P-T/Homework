"""This module contains a class for parsing data received from the net."""


from typing import Generator, Iterable, List

from rss_reader.logger.logger import Logger
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.interfaces.iparser.isubsystem import ISubsystem
from rss_reader.decorator.decorator import send_log_of_start_function
from .exceptions import EmptyListError

log = Logger.get_logger(__name__)


class BeautifulParser(IParser):
    """A class to represent a parser."""

    def __init__(self, subsystem: ISubsystem) -> None:
        """Initializer.

        :param subsystem: Third party parser.
        :type subsystem: ISubsystem
        """
        self._subsystem = subsystem

    @send_log_of_start_function
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
        self._subsystem = self._subsystem(markup, features)

    def _find_all(self, name: str = None, limit_elms: int = None) -> Iterable:
        """Return all tags with the given name."""
        return self._subsystem.find_all(name, limit=limit_elms)

    def _select(self, selector: str, limit_elms: int = None) -> Iterable:
        """Return tags selected by CSS selector."""
        return self._subsystem.select(selector, limit=limit_elms)

    @send_log_of_start_function
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

        tags = self._select(selector, limit_elms)

        if not tags:
            log.exception("No matching tags. Maybe the selector is wrong.")
            raise EmptyListError(
                "No matching tags. Maybe the selector is wrong.")

        for i in tags:
            yield i.text

    @send_log_of_start_function
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

        final_dict = []
        items = self._find_all(name, limit_elms)

        for item in items:

            # The dictionary stores information about a particular news item.
            item_dict = {}
            # find all tags inside the tag that stores the news
            item_tags = item.find_all()
            for tag in item_tags:
                tag_name = tag.name
                # if the tag name is contained in the template,
                # then we write its contents to the dictionary.
                if tag_name in template:
                    if isinstance(template[tag_name], str):
                        item_dict[tag_name] = tag.text
                    else:
                        # A dictionary with subtag attribute data
                        attrs_dict = {}
                        # The tag attributes from the template to find
                        attrs = template[tag_name]
                        for attr in attrs:
                            # Write down the value of each attribute
                            # if present or None
                            attrs_dict.update({attr: tag.get(attr, None)})
                        item_dict[tag_name] = attrs_dict
            final_dict.append(item_dict)
        return final_dict
