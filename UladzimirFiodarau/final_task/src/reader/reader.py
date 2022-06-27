import datetime
import html
import re
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from urllib.request import Request, urlopen
from urllib.parse import urlparse

from django.db import IntegrityError
from reader.models import Cache


class RssReaderException(Exception):
    pass


class DateUnifyError(RssReaderException):
    pass


class EmptyUrlError(RssReaderException):
    pass


class InvalidUrlError(RssReaderException):
    pass


class NoDataInCache(RssReaderException):
    pass


class RssReader:
    """
    Base class of rss-reader, gathers required information from rss-feeds and forms a dictionary with valuable data.
    """

    def __init__(self, url: str):
        """
        Method serves for processing news from rss feeds
        On object creation it gathers required news data, updates news cache and processes data for future output
        :param url: URL of rss-feed
        """
        self.url = url
        self.news_cache = RssReader.prepare_dict(url)
        if self.news_cache:  # to prevent further funcs if prepare_dict failed
            self.news_dict = RssReader.limit_news_dict(self.news_cache)

    @staticmethod
    def process_string(string: str) -> str:
        """
        The method is used to guarantee human readability for parsed text data.
        1. html.unescape() converts all named and numeric character references (e.g. &gt;, &#62;, &#x3e;) in string to
        corresponding Unicode characters.
        2. re.sub() removes xml tags and replaces common Unicode characters (e.g. '\xa0', '\u201c') with
        correspondent readable symbols

        :param string: a string of text
        :return: a processed string
        """
        sub_dict = {'\u203a': '>', '\xa0': ' ', '\u2019': "'", '\u2014': '-', '\u201c': '"', '\u201d': '"',
                    '\u2026': '...',
                    }
        processed_string = re.sub('<[^<]+>', '', html.unescape(string))
        for key, value in sub_dict.items():
            processed_string = re.sub(key, value, processed_string)
        processed_string = processed_string.strip()
        return processed_string

    @staticmethod
    def unify_pubdate(pubdate: str) -> str:
        """
        Method is used to unify most common variants of XML pubDate formats to a datetime.datetime object and then
        return a string representation of the object in preset format
        Method can process RFC-822 date-time format and ISO 8601 date-time format with time and time offset
        (also called 'TZ')

        :param pubdate: a representation of datetime parsed from xml pubDate tag
        :return: a string representation of datetime in "%Y:%m:%d %H:%M:%S" format
        :raise rss_exceptions.DateUnifyError if pubdate format is not supported by function
        """
        try:
            date_time = parsedate_to_datetime(pubdate)
        except (TypeError, ValueError):
            try:
                date_time = datetime.datetime.strptime(pubdate, '%Y-%m-%dT%H:%M:%S%z')
            except (TypeError, ValueError):
                raise DateUnifyError(f'unsupported pubDate format in feed, expected RFC-822 '
                                     f'or ISO 8601 with time offset')
        return f'{date_time:%Y:%m:%d %H:%M:%S}'

    @staticmethod
    def validate_url(url: str = '') -> bool:
        """
        The method checks input for being a valid URL by parsing a request with builtin urlparse package and checking
        it for having two attributes: netloc and scheme

        :param url: URL given for validation
        :return: True if given URL is a valid URL
        :raise rss_exceptions.EmptyUrlException if passed an empty argument
        :raise rss_exceptions.InvalidUrlError if passed an incorrect URL
        """
        url = url.strip()
        if not url:
            raise EmptyUrlError('Empty argument passed, please pass an URL to proceed')
        if len(url) > 2048:
            raise InvalidUrlError(f"URL exceeds maximum length of 2048 characters (given length={len(url)})")
        result = urlparse(url)
        if all([result.netloc, result.scheme]):
            return True
        else:
            raise InvalidUrlError('Invalid URL: URL must contain scheme and network location')

    @staticmethod
    def get_rss_data(url: str) -> str:
        """
        The method takes a URL as an argument and returns request response in form of a string.
        To prevent some of http error 403: forbidden, headers parameter of urllib.request.urlopen is specified
        to mimic a web-browser and timeout is set to 10.
        \nMethod decodes response data from byte string to a string to handle encoding issues with non-cp1251 and
        non-utf-8 encoded symbols (e.g. converting "\xe2\x80\x93" to "–"(en-dash)).

        :param url: URL of rss-feed
        :return: string, containing rss data
        """
        headers_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/102.0.5005.62 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                  'q=0.9,image/avif,image/webp,image/apng,*/*;'
                                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
                        }
        with urlopen(Request(url, headers=headers_dict), timeout=10) as response:
            rss_data = response.read()
            if b'encoding="windows-1251"' in rss_data:
                rss_data = rss_data.decode('cp1251')
            else:
                rss_data = rss_data.decode('utf-8')
        return rss_data

    @staticmethod
    def convert_rss_data_to_root(rss_data: str) -> ET.Element:
        """
        The method takes a string of XML data and uses ElementTree.fromstring function to parse XML from a string
        directly into an Element, which is the root element of the parsed tree.

        :param rss_data: string, containing rss data
        :return: ElementTree.Element object
        """
        root = ET.fromstring(rss_data)
        return root

    @staticmethod
    def convert_root_to_dict(root: ET.Element) -> dict:
        """
        The method takes an ElementTree.Element object and returns a dictionary cache with required data structured.
        Tags that are required for the structure of the dictionary are pre-set in required_data dict.
        Correct tags in which media data should be stored according to rss 2.0 standard are set in media_data dicts.
        1. iteration over root.iter() is done till the first 'item' tag is met to create rss-feed information pairs
        2. iteration over root.iter('item') is done to create rss-items information pairs and find items-media URLs.
        Rss-item date pairs are grouped using unified format datetime information as a key.
        \nThe method looks for media URLs in:
        1. text of sub-elements of elements, listed in media_dict
        2. attributes of elements, listed in media_dict
        3. text of elements, listed in media_dict
        4. attributes of elements <{.*}content>, <{.*}thumbnail> and <thumbnail>
        5. <img src> tags in text of elements

        :param root: an ET.Element object
        :return: dictionary with required data cached
        """
        feed_items = {}
        news_cache = {}
        required_data = ('title', 'description', 'link', 'pubDate')
        media_data = ('image', 'enclosure')

        for element in root.iter():
            if element.tag == 'item':
                break
            elif element.tag in media_data:
                media_dict = {subelement.tag: RssReader.process_string(subelement.text) for subelement in element
                              if subelement.tag in ('url', 'type') and subelement.text}
                news_cache['feed_media'] = media_dict
            elif element.tag in required_data and element.text:
                news_cache['feed_' + element.tag] = RssReader.process_string(element.text)
        for item in root.iter('item'):
            temporary_item_dict = {}
            for element in item:
                if element.tag in media_data or re.search('{.+}content|{.+}thumbnail|thumbnail', element.tag):
                    media_dict = {subelement.tag: subelement.text for subelement in element  # if no text - text
                                  if subelement.tag in ('url', 'type') and subelement.text}  # is either None or ''
                    if 'url' not in media_dict and 'url' in element.attrib:
                        media_dict['url'] = element.attrib['url']
                        if 'type' in element.attrib:  # to specify images from audio and video
                            media_dict['type'] = element.attrib['type']
                    elif 'url' not in media_dict and element.text and re.search('http.?://', element.text):
                        media_dict['url'] = re.search('http.?://[^\\s<>]+', element.text)[0]
                    temporary_item_dict['media'] = media_dict
                elif element.tag in required_data and element.text:
                    temporary_item_dict[element.tag] = RssReader.process_string(element.text)
                    if element.text and re.search('img.*src=', element.text) and 'media' not in temporary_item_dict:
                        temporary_item_dict['media'] = {'url': re.search('src="[^"]+', element.text)[0][5:]}
            if temporary_item_dict.get('pubDate', None):
                feed_items[RssReader.unify_pubdate(temporary_item_dict['pubDate'])] = temporary_item_dict
            else:
                feed_items[temporary_item_dict['title']] = temporary_item_dict
            news_cache['feed_items'] = feed_items
        return news_cache

    @staticmethod
    def prepare_dict(url: str) -> dict:
        """
        The method combines parts of the rss-to-dictionary parser into a single script
        :param url: URL of rss-feed
        :return: dictionary with required data cached
        """
        if RssReader.validate_url(url):
            rss_data = RssReader.get_rss_data(url)
            root = RssReader.convert_rss_data_to_root(rss_data)
            news_cache = RssReader.convert_root_to_dict(root)
            return news_cache

    @staticmethod
    def limit_news_dict(news_cache: dict, limit=None) -> dict:
        """
        Method prepares a limited number of news for output if limit is set

        :param news_cache: dictionary with required data cached
        :param limit: limit of news to output
        :return: dictionary with a limited number of news
        """
        if limit is None:
            news_dict = news_cache
        else:
            news_dict = {key: value for key, value in news_cache.items() if key != 'feed_items'}
            news_dict['feed_items'] = {}
            for item in sorted(news_cache['feed_items'], reverse=True)[:limit]:
                news_dict['feed_items'][item] = news_cache['feed_items'].get(item, None)
        return news_dict


class DjangoRssReader(RssReader):

    def __init__(self, url: str, news_limit: int = None):
        """
        Method serves for processing news from rss feeds
        On object creation it gathers required news data, updates news cache and processes data for future output
        :param url: URL of rss-feed
        """
        self.url = url
        self.news_cache = RssReader.prepare_dict(url)
        if self.news_cache:  # to prevent further funcs if prepare_dict failed
            self.news_dict = RssReader.limit_news_dict(self.news_cache, news_limit)

    def save_django_reader_cache(self):
        cache_dict = {"url": self.url, 'cache': self.news_cache}
        if cache_dict['cache']:
            c = Cache(**cache_dict)
            try:
                c.save()
            except IntegrityError:
                cache = Cache.objects.filter(url=self.url).first()
                cache.cache = c.cache
                cache.save()
        else:
            raise ValueError('No news found in URL, please check URL')


class DjangoRssReaderCached(RssReader):
    @staticmethod
    def limit_news_dict(news_cache: dict, limit=None, news_url: str = '', news_date: str = '') -> dict:
        """
        """
        if news_url and RssReader.validate_url(news_url):
            news_cache = {url: feed for url, feed in news_cache.items() if url == news_url}
            if len(news_cache) == 0:
                raise NoDataInCache('No news from such URL in cache or not a valid rss URL')
        if news_url:
            temp_news_dict = {key: value for url in news_cache.values() for key, value in url.items()
                              if key != 'feed_items'}
            temp_news_dict['feed_items'] = {}
        else:
            temp_news_dict = {'feed_title': f'Cached news of {news_date if news_date else "recent time"}',
                              'feed_description': f'Best news gathered for you and cached by our service',
                              'feed_link': f'News sources can be reached through links listed in news',
                              'feed_items': {},
                              }
        for url, feed in news_cache.items():
            for key, value in feed.items():
                if key == 'feed_items':
                    for news_tag, tag_text in value.items():
                        if news_date:
                            if news_date in news_tag:
                                temp_news_dict['feed_items'][news_tag] = tag_text
                        else:
                            temp_news_dict['feed_items'][news_tag] = tag_text
        if len(temp_news_dict['feed_items']) == 0:
            raise NoDataInCache('No news found in cache')
        news_dict = RssReader.limit_news_dict(temp_news_dict, limit)
        return news_dict
