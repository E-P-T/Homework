

from rss_reader.interfaces.iloader.iloader import IHandler
from rss_reader.interfaces.icrawler.icrawler import ICrawler
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.logger.logger import Logger


log = Logger.get_logger(__name__)


class FromWebHandler(IHandler):
    def __init__(self,
                 crawler: ICrawler,
                 parser: IParser) -> None:
        """Initializer.

        :param crawler: Crawler object. Used to get information
                        from the Internet.
        :type crawler: ICrawler
        :param parser: Parser object. Used to parse information
                        received from the Internet.
        :type parser: IParser
        """
        self._crawler = crawler
        self._parser = parser

        def get_data(self,
                     tag_name: str,
                     title_tag: str,
                     source: str,
                     limit: int) -> dict:

            cr = self._crawler(source)
            response_ = cr.get_data()

            self._parser.create_parser(markup=response_)
