

from rss_reader.interfaces.iloader.iloader import IHandler
from rss_reader.logger.logger import Logger


log = Logger.get_logger(__name__)


class FromWebHandler(IHandler):
    def __init__(self,
                 crawler: ICrawler,
                 parser: IParser) -> None:
        pass
