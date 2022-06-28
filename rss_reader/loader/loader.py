"""This module contains a set of handlers for receiving data.

The handler receives data from a specific source, selects the necessary
data elements and forms the final result.
"""


from typing import Dict, Optional
from numpy import nan
from pandas import DataFrame

from rss_reader.interfaces.iloader.iloader import IHandler, ILoadHandler
from rss_reader.interfaces.icrawler.icrawler import ICrawler
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.logger.logger import Logger
from rss_reader.decorator.decorator import send_log_of_start_function
from rss_reader.date_converter.date_converter import DateConverter

from .reader import ReaderCSVFile
from .decorators import BaseComponent, SortByEqual, LimitRecords
from .exceptions import DataEmptyError


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

    def __init__(self, file: str, request: Dict[str, str]) -> None:
        self._file = file
        self._request = request

    def get_data(self) -> list:
        date = self._request.get('date')
        if date:

            raw_data = ReaderCSVFile.read(self._file)

            try:
                dt = DateConverter().date(date)
            except ValueError as e:
                raise ValueError('Wrong time format') from e

            bc = BaseComponent()
            fined_data = SortByEqual('item.pubDate', dt.__str__(), bc)

            source = self._request.get('source')
            if source:
                fined_data = SortByEqual(
                    'link', source, fined_data)

            limit = self._request.get('limit')
            if limit:
                fined_data = LimitRecords(limit, fined_data)

            fined_data = fined_data.operation(raw_data)

            if fined_data.empty:
                raise DataEmptyError(
                    'There is no data to provide for the current date.')

            data = self._convert_to_dict(fined_data)
            return data
        else:
            return super().get_data()

    def _convert_to_dict(self, raw_data: DataFrame) -> list:
        l_item = []

        def new_item():
            new_source = {}
            new_source['title_web_resource'] = v.get('title_web_resource')
            new_source['link'] = link
            new_source['items'] = [item]
            l_item.append(new_source)

        for i, v in raw_data.iterrows():

            v.replace(nan, None, inplace=True)
            link = v.get('link')

            item = {}
            item['title'] = v.get('item.title')
            item['link'] = v.get('item.link')
            item['pubDate'] = v.get('item.pubDate')
            item['source'] = v.get('item.source')

            content = {}
            content['url'] = v.get('item.content.url')
            content['title'] = v.get('item.content.title')
            item['content'] = content

            if not l_item:
                new_item()
            else:
                for i in l_item:
                    if link == i.get('link'):
                        i['items'].append(item)
                        break
                else:
                    new_item()
        return l_item


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
