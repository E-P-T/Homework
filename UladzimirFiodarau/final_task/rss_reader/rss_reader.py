"""
Main rss-reader module.
Goal was to create a rss-reader using OOP and without third-party libraries to lessen external dependencies.
To make it easier to change the reader inner processing (if later needed) processing of the rss-feed into a
dictionary of necessary data is split into several staticmethods.
"""
import argparse
import datetime
import html
import json
import re
import os
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pprint import pprint
from urllib import error
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import rss_exceptions
from rss_logger import logger_info

script_root = os.path.dirname(__file__)
news_limit = None
to_json = False
verbose = False
news_date = None


class RssReader:
    """
    Base class of rss-reader, gathers required information from rss-feeds and forms a dictionary with valuable data
    provides methods for printing data in stdout with option of converting to JSON format.
    dictionary and JSON structure are described in README.md
    """
    def __init__(self, url: str):
        self.url = url
        self.news_cache = RssReader.prepare_dict(url)
        if self.news_cache:  # to prevent further funcs if prepare_dict failed
            RssReader.update_local_cache(self.url, self.news_cache)
            self.news_dict = RssReader.limit_news_dict(self.news_cache, news_limit)
            if to_json:
                self.news_dict_json = RssReader.convert_dict_to_json(self.news_dict)

    def __str__(self):
        return f'News from rss-feed {self.url}'

    def __repr__(self):
        return f'RssReader({self.url})'

    @staticmethod
    def log_runtime(text: str):
        """
        If --verbose is specified while running script user-friendly status messages are sent to stdout
        The method is used for logging in verbose mode and can be modified for other kinds of logging if needed.
        :param text: text for status logging
        :return: None
        """
        if verbose:
            logger_info.info(text)

    @staticmethod
    def process_string(string: str) -> str:
        """
        The method is used to guarantee human readability for parsed text data.
        1. html.unescape() converts all named and numeric character references (e.g. &gt;, &#62;, &#x3e;) in string to
        corresponding Unicode characters.
        2. re.sub() removes xml tags and replaces non-breakable space Unicode characters (\xa0) with whitespaces

        :param string: a string of text
        :return: a processed string
        """
        processed_string = re.sub('<[^<]+>', '', html.unescape(string))
        processed_string = re.sub('\xa0', ' ', processed_string).strip()
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
                raise rss_exceptions.DateUnifyError(f'unsupported pubDate format in feed, expected RFC-822 '
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
        RssReader.log_runtime(f'Validating URL: {url}')
        url = url.strip()
        if not url:
            raise rss_exceptions.EmptyUrlError('Empty argument passed, please pass an URL to proceed')
        if len(url) > 2048:
            raise rss_exceptions.InvalidUrlError(f"URL exceeds maximum length of 2048 characters "
                                                 f"(given length={len(url)})")
        result = urlparse(url)
        if all([result.netloc, result.scheme]):
            RssReader.log_runtime('URL validated successfully')
            return True
        else:
            raise rss_exceptions.InvalidUrlError('Invalid URL: URL must contain scheme and network location')

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
        RssReader.log_runtime('Making a URL request')
        with urlopen(Request(url, headers=headers_dict), timeout=10) as response:
            RssReader.log_runtime('URL request successful. Reading and decoding response data')
            rss_data = response.read()
            if b'encoding="windows-1251"' in rss_data:
                rss_data = rss_data.decode('cp1251')
            else:
                rss_data = rss_data.decode('utf-8')
            RssReader.log_runtime('Rss data successfully decoded')
        return rss_data

    @staticmethod
    def convert_rss_data_to_root(rss_data: str) -> ET.Element:
        """
        The method takes a string of XML data and uses ElementTree.fromstring function to parse XML from a string
        directly into an Element, which is the root element of the parsed tree.

        :param rss_data: string, containing rss data
        :return: ElementTree.Element object
        """
        RssReader.log_runtime('Converting rss data to ElementTree.Element object')
        root = ET.fromstring(rss_data)
        RssReader.log_runtime('Successfully converted rss data to ElementTree.Element object')
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

        RssReader.log_runtime(f'Converting ElementTree.Element object to a dictionary. '
                              f'Searching for tags: {required_data + media_data}')

        RssReader.log_runtime('Creating separate key-value pairs for feed tags')
        for element in root.iter():
            if element.tag == 'item':
                break
            elif element.tag in media_data:
                media_dict = {subelement.tag: RssReader.process_string(subelement.text) for subelement in element
                              if subelement.tag in ('url', 'type') and subelement.text}
                news_cache['feed_media'] = media_dict
            elif element.tag in required_data:
                news_cache['feed_' + element.tag] = RssReader.process_string(element.text) if element.text else None

        RssReader.log_runtime('Creating separate key-value pairs for item tags')
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
                elif element.tag in required_data:
                    temporary_item_dict[element.tag] = RssReader.process_string(element.text) if element.text else None
                    if element.text and re.search('img.*src=', element.text) and 'media' not in temporary_item_dict:
                        temporary_item_dict['media'] = {'url': re.search('src="[^"]+', element.text)[0][5:]}
            if temporary_item_dict.get('pubDate', None):
                feed_items[RssReader.unify_pubdate(temporary_item_dict['pubDate'])] = temporary_item_dict
            else:
                feed_items[temporary_item_dict['title']] = temporary_item_dict
            news_cache['feed_items'] = feed_items
        RssReader.log_runtime('Conversion to dictionary successful')
        return news_cache

    @staticmethod
    def prepare_dict(url: str) -> dict:
        """
        The method combines parts of the rss-to-dictionary parser into a single script while handling exceptions
        :param url: URL of rss-feed
        :return: dictionary with required data cached
        """
        try:
            if RssReader.validate_url(url):
                rss_data = RssReader.get_rss_data(url)
        except rss_exceptions.EmptyUrlError as exc:
            print(f'Error occurred while processing URL: {exc}')
        except rss_exceptions.InvalidUrlError as exc:
            print(f'Error occurred while processing URL: {exc}')
        except error.HTTPError as exc:
            print(f'Error occurred while accessing HTTP: {exc}')
        except error.URLError as exc:
            print(f'Error occurred while requesting URL: {exc}')
        except UnicodeDecodeError as exc:
            print(f'Error occurred while decoding byte string of rss data to UTF-8: {exc}')
        except Exception as exc:
            print(f'An unexpected error occurred while requesting and processing rss data: {exc}')
        else:
            try:
                root = RssReader.convert_rss_data_to_root(rss_data)
            except ET.ParseError as exc:
                print(f'Error while parsing rss data, possibly not an rss URL passed: ParseError {exc}')
            except Exception as exc:
                print(f'An unexpected error occurred while parsing rss data: {exc}')
            else:
                try:
                    news_cache = RssReader.convert_root_to_dict(root)
                except rss_exceptions.DateUnifyError as exc:
                    print(f'Error occurred while converting datetime: {exc}')
                except TypeError as exc:
                    print(f'Incorrect argument type while forming a news dictionary: {exc}')
                except ValueError as exc:
                    print(f'Incorrect argument value while forming a news dictionary: {exc}')
                except KeyError as exc:
                    print(f'Incorrect key while forming a news dictionary: {exc}')
                except Exception as exc:
                    print(f'An unexpected error occurred while forming a news dictionary: {exc}')
                else:
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
            RssReader.log_runtime(f'Preparing news quantity according to set limit: {limit}')
            news_dict = {key: value for key, value in news_cache.items() if key != 'feed_items'}
            news_dict['feed_items'] = {}
            for item in sorted(news_cache['feed_items'], reverse=True)[:limit]:
                news_dict['feed_items'][item] = news_cache['feed_items'].get(item, None)
        return news_dict

    @staticmethod
    def convert_dict_to_json(news_dict: dict) -> str:
        """
        Method converts a news dictionary into JSON string
        :param news_dict: a dictionary with news
        :return: JSON string
        """
        RssReader.log_runtime('Converting news to JSON format')
        json_string = json.dumps(news_dict)
        RssReader.log_runtime('Successfully converted news to JSON format')
        return json_string

    @staticmethod
    def load_from_local_cache() -> dict:
        """
        Method loads news cache from local cache in form of a nested dictionary if cache file exists.
        :return: a nested dictionary with cached news
        """
        RssReader.log_runtime('Loading news from local cache')
        if os.path.exists(script_root + '/cache/rss_cache.json'):
            with open(script_root + '/cache/rss_cache.json', 'r') as rss_cache:
                return json.load(rss_cache)
        else:
            RssReader.log_runtime('No local cache found')
            return {}

    @staticmethod
    def save_to_local_cache(news_cache: dict):
        """
        Method saves a dictionary of news to local cache in form of JSON object.
        Saving is done to a directory 'cache' in root directory of script, if such directory doesn't exist,
        it is created.
        :param news_cache:
        :return: None
        """
        RssReader.log_runtime('Saving news to local cache')
        if not os.path.exists(script_root+'/cache/'):
            os.mkdir(script_root+'/cache/')
        with open(script_root + '/cache/rss_cache.json', 'w') as rss_cache:
            json.dump(news_cache, rss_cache, indent=4)
        RssReader.log_runtime('Successfully saved news to local cache')

    @staticmethod
    def update_local_cache(url: str, url_news_cache: dict):
        """
        Method updates existing local cache with news dictionary from current processed URL.
        :param url:
        :param url_news_cache:
        :return:
        """
        news_cache = RssReader.load_from_local_cache()
        news_cache[url] = url_news_cache
        RssReader.save_to_local_cache(news_cache)

    def return_news_default(self):
        """
        Method makes a pretty print of the dictionary formed from the news feed to stdout using dict.get() method
        to prevent KeyErrors
        :return: None
        """
        print('=' * 120)
        print(f'Feed title: {self.news_dict.get("feed_title", "No title provided")}')
        print(f'Feed description: {self.news_dict.get("feed_description", "No description provided")}')
        print(f'Feed URL: {self.news_dict.get("feed_link", "No link provided")}')
        print(f'Last update: {self.news_dict.get("feed_pubDate", "Not specified")}')
        print('=' * 120)
        for item in sorted(self.news_dict['feed_items'], reverse=True):
            print(f'Title: {self.news_dict["feed_items"][item].get("title", "No title provided")}')
            print(f'Link: '
                  f'{self.news_dict["feed_items"][item].get("link", "No link provided")}')
            print(f'Publication date: '
                  f'{self.news_dict["feed_items"][item].get("pubDate", "No publication date provided")}')
            print()
            print(f'{self.news_dict["feed_items"][item].get("description", "No description provided")}')
            print()
            if 'media' in self.news_dict["feed_items"][item]:
                if 'type' in self.news_dict["feed_items"][item]['media']:
                    media_type = self.news_dict["feed_items"][item]['media']['type']
                else:
                    media_type = "image"
                print(f'Media ({media_type}) link:\n '
                      f'{self.news_dict["feed_items"][item]["media"].get("url", "No link provided")}')
            print('-' * 120)

    def return_news_json(self):
        """
        Method makes a pretty print of JSON data to stdout, sort_dicts is set as False to prevent sorting
        :return: None
        """
        pprint(json.loads(self.news_dict_json), sort_dicts=False)


class RssReaderCached(RssReader):

    def __init__(self, url: str):
        self.url = url
        self.news_cache = RssReaderCached.load_from_local_cache()
        if self.news_cache:
            self.news_dict = RssReaderCached.limit_news_dict(self.news_cache, news_limit, self.url)
            if to_json:
                self.news_dict_json = RssReaderCached.convert_dict_to_json(self.news_dict)
        else:
            raise rss_exceptions.NoDataInCache('No news found in cache')

    @staticmethod
    def limit_news_dict(news_cache: dict, limit=None, news_url: str = '') -> dict:
        """
        Method prepares news_dict loaded from local cache for output. Only news from given in arguments date are chosen
        for later processing.
        If news_url is specified, method chooses news only from that particular URL and saves its feed information for
        later output in title
        If no news_url is specified, method chooses news from all sources available in cache and creates a set of
        standard tags for later output in title
        Method uses the same named method of parent class to make a single processing standard for news after they have
        been chosen from cache
        :param news_cache: dictionary with required data cached
        :param limit: limit of news to output
        :param news_url: link to news feed of news to output
        :return: dictionary with a limited number of news
        """
        if news_url and RssReaderCached.validate_url(news_url):
            RssReader.log_runtime(f'Choosing news according to set url: {news_url}')
            news_cache = {url: feed for url, feed in news_cache.items() if url == news_url}
            if len(news_cache) == 0:
                raise rss_exceptions.NoDataInCache('No news from such URL in cache or not a valid rss URL')
        RssReader.log_runtime(f'Choosing news according to set date: {news_date}')
        if news_url:
            temp_news_dict = {key: value for url in news_cache.values() for key, value in url.items()
                              if key != 'feed_items'}
            temp_news_dict['feed_items'] = {}
        else:
            temp_news_dict = {'feed_title': f'Cached news of {news_date}',
                              'feed_description': f'Best news gathered for you and cached by our service',
                              'feed_link': f'News sources can be reached through links listed in news',
                              'feed_items': {},
                              }
        for url, feed in news_cache.items():
            for key, value in feed.items():
                if key == 'feed_items':
                    for news_tag, tag_text in value.items():
                        if news_date in news_tag:
                            temp_news_dict['feed_items'][news_tag] = tag_text
        if len(temp_news_dict['feed_items']) == 0:
            raise rss_exceptions.NoDataInCache('No news of the set date found in cache')
        news_dict = RssReader.limit_news_dict(temp_news_dict, limit)
        return news_dict


def parse_command_line(args=None):
    """
    The function parses command line arguments to provide Command Line Interface to user and returns the arguments
    passed on python script call
    Exit_on_error is set as False to allow handling exceptions where possible during function runtime.
    :param args: if None - is taken from sys.argv
    :return: arguments passed on command line script call
    """
    parser = argparse.ArgumentParser(description="Python command-line RSS reader.", exit_on_error=False)
    parser.add_argument("--version", help="Print version info and exit", action="version",
                        version="You are using %(prog)s version 1.2")
    parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_true")
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    parser.add_argument("--date", type=str, help="Date for news selection, must be in %%Y%%m%%d format (YYYYMMDD)")
    parser.add_argument("source", type=str, nargs='?', default='', help="RSS-feed URL")
    return parser.parse_args(args)


def main():
    """
    The function combines the rss-reader with argparse module functionality.
    It also is used to prevent errors while testing (caused by unittest module also parsing the CLI during execution)
    by calling argparse.ArgumentParser from a separate function instead of global namespace
    :return:None
    """
    try:
        args = parse_command_line()
    except argparse.ArgumentError as exc:
        print(f'Incorrect argument value passed in command line: {exc}')
    else:
        if args.verbose:
            global verbose
            verbose = True
            RssReader.log_runtime("Verbose mode turned on")
        if args.json:
            global to_json
            to_json = True
            RssReader.log_runtime('Output format is set to JSON')
        if args.limit:
            global news_limit
            news_limit = args.limit if args.limit > 0 else None
            RssReader.log_runtime(f'News output limit is set to {news_limit}')
        try:
            if args.date:
                date_time = datetime.datetime.strptime(args.date, "%Y%m%d")
                global news_date
                news_date = f'{date_time:%Y:%m:%d}'
                news = RssReaderCached(args.source)
            else:
                news = RssReader(args.source)
        except ValueError as exc:
            print(f'Wrong --date attribute format: {exc}')
        except rss_exceptions.NoDataInCache as exc:
            print(f'Error while loading cached news: {exc}')
        except Exception as exc:
            print(f'Unexpected error while preparing news: {exc}')
        else:  # print only if news were generated w/o errors
            if 'news_dict' in news.__dict__ and news.news_dict:
                if args.json:
                    try:
                        RssReader.log_runtime('Printing news in JSON format for the user\n')
                        news.return_news_json()
                    except json.JSONDecodeError as exc:
                        print(f'Error while reading JSON object: {exc}')
                else:
                    try:
                        RssReader.log_runtime('Printing news for the user\n')
                        news.return_news_default()
                    except KeyError as exc:
                        print(f'Error while printing news: {exc}')
                    except Exception as exc:
                        print(f'Unexpected error while printing news: {exc}')


if __name__ == '__main__':
    main()
