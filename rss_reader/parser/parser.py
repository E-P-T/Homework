
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.interfaces.iparser.isubsystem import ISubsystem


class BeautifulParser(IParser):

    def __init__(self, subsystem: ISubsystem) -> None:
        """Initializer.

        :param subsystem: Third party parser.
        :type subsystem: ISubsystem
        """
        self._subsystem = subsystem

    def create_parser(self, markup: bytes, features: str = 'xml') -> None:
        self._subsystem = self._subsystem(markup, features)
