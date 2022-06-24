
from rss_reader.interfaces.iparser.iparser import IParser


class BeautifulParser(IParser):

    def __init__(self, subsystem: ISubsystem) -> None:
        self._subsystem = subsystem
