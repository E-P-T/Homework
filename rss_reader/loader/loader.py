"""This module contains a set of handlers for receiving data.

The handler receives data from a specific source, selects the necessary
data elements and forms the final result.
"""


from typing import Dict, List, Optional
from numpy import nan
from pandas import DataFrame

from rss_reader.interfaces.iloader.iloader import IHandler, ILoadHandler
from rss_reader.interfaces.icrawler.icrawler import ICrawler
from rss_reader.interfaces.iparser.iparser import IParser
from rss_reader.logger.logger import Logger
from rss_reader.decorator.decorator import send_log_of_start_function
from rss_reader.date_converter.date_converter import DateConverter
from rss_reader.parser.exceptions import EmptyListError


from .reader import ReaderCSVFile
from .decorators import BaseComponent, SortByEqual, LimitRecords
from .exceptions import DataEmptyError, EmptyURLError


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

            # load data from local storage
            raw_data = ReaderCSVFile.read(self._file)

            # convert date to string
            try:
                dt = DateConverter().date_convert(date)
            except ValueError as e:
                raise ValueError('Wrong time format') from e

            # design pattern - decorator
            bc = BaseComponent()
            # sort by date
            fined_data = SortByEqual('item.pubDate', dt.__str__(), bc)

            source = self._request.get('source')
            if source:
                # sort by source
                fined_data = SortByEqual(
                    'link', source, fined_data)

            limit = self._request.get('limit')
            if limit:
                # sort by limit
                fined_data = LimitRecords(limit, fined_data)
            # start execution of the decorator pattern
            fined_data = fined_data.operation(raw_data)

            if fined_data.empty:
                raise DataEmptyError(
                    'There is no data to provide for the current date.')

            # convert to the given dictionary structure
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


class FromWebHandler(AbstractLoaderHandler):
    """Internet data handler."""

    template = {'title': 'text',
                'pubDate': 'text',
                'source': 'text',
                'link': 'text',
                'content': ['url', 'title']
                }

    def __init__(self,
                 tag_name: str,
                 title_tag: str,
                 source: str,
                 limit: Optional[int],
                 crawler: ICrawler,
                 parser: IParser) -> None:
        """Initializer.

        :param tag_name: The name of the tag in which the news is stored.
        For example <item>.
        :type tag_name: str
        :param title_tag: The name of the tag that contains the title.
        It is CSS selector.
        :type title_tag: str
        :param source: News source url.
        :type source: str
        :param limit: The number of elements to return.
        :type limit: Optional[int]
        :param crawler: Crawler object. Used to get information
        from the Internet.
        :type crawler: ICrawler
        :param parser: Parser object. Used to parse information
        received from the Internet.
        :type parser: IParser
        """
        self._tag_name = tag_name
        self._title_tag = title_tag
        self._source = source
        self._limit = limit
        self._crawler = crawler
        self._parser = parser

    @send_log_of_start_function
    def get_data(self) -> List[dict]:
        """Return a list with parsed data.

        :raises EmptyURLError: Occurs when the url is empty.
        :raises DataEmptyError: Occurs when there is no data.
        :return: List with data.
        :rtype: List[dict]
        """
        if not self._source:
            raise EmptyURLError('Passed url is empty!')

        # get data from internet
        cr = self._crawler(self._source)
        response_ = cr.get_data()

        log.debug('Start creating the parser.')
        self._parser.create_parser(markup=response_)
        log.debug('Stop creating the parser.')

        log.debug('Start the process of getting the resource title.')
        try:
            title_tag = self._parser.get_tags_text(selector=self._title_tag)
            title_text = next(title_tag)
        except EmptyListError:
            title_text = None
        log.debug('Stop the process of getting the resource title.')

        # get news
        items = self._parser.get_items(
            self.template, name=self._tag_name, limit_elms=self._limit)

        if not items:
            raise DataEmptyError('no news')

        # collect all the data in a dictionary
        log.debug('Start generating results.')
        result = {'title_web_resource': title_text}
        result.update({'link': self._source})
        items_dict = {'items': items}
        result.update(items_dict)
        log.debug('Result was formed.')

        return [result]
