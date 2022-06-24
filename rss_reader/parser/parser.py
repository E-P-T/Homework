
from typing import Generator, Iterable

from rss_reader.logger.logger import Logger
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.interfaces.iparser.isubsystem import ISubsystem
from rss_reader.decorator.decorator import send_log_of_start_function
from .exceptions import EmptyListError

log = Logger.get_logger(__name__)


class BeautifulParser(IParser):

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

    def get_tags_text(self,
                      selector: str,
                      limit_elms: int = None) -> Generator[str, None, None]:
        tags = self._select(selector, limit_elms)

        if not tags:
            log.exception("No matching tags. Maybe the selector is wrong.")
            raise EmptyListError(
                "No matching tags. Maybe the selector is wrong.")

        for i in tags:
            yield i.text
