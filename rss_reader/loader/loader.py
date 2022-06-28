"""This module contains a set of handlers for receiving data.

The handler receives data from a specific source, selects the necessary
data elements and forms the final result.
"""


from rss_reader.interfaces.iloader.iloader import IHandler
from rss_reader.interfaces.icrawler.icrawler import ICrawler
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.logger.logger import Logger
from rss_reader.decorator.decorator import send_log_of_start_function


log = Logger.get_logger(__name__)


class AbstractLoaderHandler(ILoadHandler):

    _next_handler: Optional[ILoadHandler] = None

    @send_log_of_start_function
    def set_next(self, handler: ILoadHandler) -> ILoadHandler:
        self._next_handler = handler
        return handler

    @send_log_of_start_function
    def get_data(self) -> list:
        if self._next_handler:
            return self._next_handler.get_data()
        return None


class FromLocalSTorageHandler(AbstractLoaderHandler):
    pass


class FromWebHandler(IHandler):
    """Internet data handler."""

    template = {'title': 'text',
                'pubDate': 'text',
                'source': 'text',
                'link': 'text',
                'content': ['url', 'title']
                }

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

    @send_log_of_start_function
    def get_data(self,
                 tag_name: str,
                 title_tag: str,
                 source: str,
                 limit: int) -> dict:
        """Return a dictionary with parsed data.

        :param tag_name: The name of the tag in which the news is stored.
        :type tag_name: str
        :param title_tag: The name of the tag in which the name
                            of the rss resource is stored.
        :type title_tag: str
        :param source: Resource URL.
        :type source: str
        :param limit: Number of news items to display.
        :type limit: int
        :return: Dictionary with parsed data.
        :rtype: dict
        """

        cr = self._crawler(source)
        response_ = cr.get_data()

        log.debug('Start creating the parser.')
        self._parser.create_parser(markup=response_)
        log.debug('Stop creating the parser.')

        log.debug('Start getting parsed data.')
        title_text = next(self._parser.get_tags_text(
            selector=title_tag))
        items = self._parser.get_items(
            self.template, name=tag_name, limit_elms=limit)
        log.debug('Stop getting parsed data.')

        log.debug('Start generating results.')
        result = {'title_web_resource': title_text}
        items_dict = {'items': items}
        result.update(items_dict)
        log.debug('Result was formed.')

        return result
