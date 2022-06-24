
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.interfaces.iparser.isubsystem import ISubsystem
from rss_reader.decorator.decorator import send_log_of_start_function


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
