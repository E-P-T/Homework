import datetime
import html
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib import error
from email.utils import parsedate_to_datetime
import rss_exceptions

rss_feed403 = 'http://www.ixbt.com/export/utf8/news.rss'
rss_feed404 = 'http://www.onliner.by/rss/news.rss'
rss_feederr = 'https://www.google.com/'
rss_feed_unex_err = 'http://www.itogi.ru/WebExport.nsf/Anons/itogi.xml'

rss_feed1 = 'https://www.latimes.com/local/rss2.0.xml'
rss_feed2 = 'https://www.usda.gov/rss/latest-releases.xml'
rss_feed3 = 'https://www.yahoo.com/news/rss'
rss_feed4 = 'https://cdn.feedcontrol.net/8/1114-wioSIX3uu8MEj.xml'
rss_feed5 = 'https://moxie.foxnews.com/feedburner/latest.xml'
rss_feed6 = 'https://feeds.simplecast.com/54nAGcIl'
rss_feed7 = 'http://news.rambler.ru/rss/politics/'
rss_feed8 = 'https://www.goha.ru/rss/mmorpg'
rss_feed9 = 'https://money.onliner.by/feed'
rss_feed10 = 'http://www.gazeta.ru/export/gazeta_rss.xml'

rss_feed31 = 'https://vse.sale/news/rss'
rss_feed32 = 'https://news.google.com/rss/'
rss_feed33 = 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml'
rss_feed34 = 'https://www.cnbc.com/id/100727362/device/rss/rss.html'
rss_feed35 = 'https://www.cbsnews.com/latest/rss/world'
rss_feed36 = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
rss_feed37 = 'https://auto.onliner.by/feed'
rss_feed38 = 'http://feeds.bbci.co.uk/news/world/rss.xml'
rss_feed39 = 'https://www.buzzfeed.com/world.xml'


def process_string(string: str) -> str:
    """
    The function is used to guarantee human readability for parsed text data.
    1. html.unescape() is used to convert all named and numeric character references (e.g. &gt;, &#62;, &#x3e;)
    in string to the corresponding Unicode characters.
    2. re.sub() is used to remove xml tags and replace non-breakable space Unicode characters (\xa0) with whitespaces

    :param string: a string of text
    :return: a processed string
    """
    processed_string = re.sub('<[^<]+>', '', html.unescape(string))
    processed_string = re.sub('\xa0', ' ', processed_string).strip()
    return processed_string


def unify_pubdate(pubdate: str) -> str:
    """
    Function is used to unify most common variants of XML pubDate formats to a datetime.datetime object and then return
    a string representation of the object in preset format
    Function can process RFC-822 date-time format and ISO 8601 date-time format with time offset (also called 'TZ')

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


def validate_url(url: str = ''):
    """
    The function checks input for being a valid URL by parsing a request with builtin urlparse package and checking it
    for having two attributes: netloc and scheme

    :param url: URL given for validation
    :return: True if given URL is a valid URL
    :raise rss_exceptions.EmptyUrlException if passed an empty argument
    :raise rss_exceptions.InvalidUrlError if passed an incorrect URL
    """
    url = url.strip()
    if not url:
        raise rss_exceptions.EmptyUrlError('Empty argument passed, please pass an URL to proceed')
    if len(url) > 2048:
        raise rss_exceptions.InvalidUrlError(f"URL exceeds maximum length of 2048 characters (given length={len(url)})")
    result = urlparse(url)
    if all([result.netloc, result.scheme]):
        return True
    elif not any([result.netloc, result.scheme]):
        raise rss_exceptions.InvalidUrlError('Invalid URL: URL must contain scheme and network location')
    elif not result.scheme:
        raise rss_exceptions.InvalidUrlError('Invalid URL: No scheme specified in URL')
    elif not result.netloc:
        raise rss_exceptions.InvalidUrlError('Invalid URL: No network location specified in URL')


def get_rss_data(url: str) -> str:
    """
    The function takes a URL as an argument and returns request response in form of a string.
    To prevent some of http error 403: forbidden, headers parameter of urllib.request.urlopen is specified
    to mimic a web-browser and timeout is set to 10.
    \nFunc decodes response data from byte string to a string to handle encoding issues with non-utf-8 encoded symbols
    (e.g. converting "\xe2\x80\x93" to "–"(en-dash)).

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
        rss_data = response.read().decode('utf-8')
        print(rss_data, file=open('rss_data.txt', 'w', encoding='utf-8'))
    return rss_data


def convert_rss_data_to_root(rss_data: str) -> ET.Element:
    """
    The function takes a string of XML data and uses ElementTree.fromstring function to parse XML from a string
    directly into an Element, which is the root element of the parsed tree.

    :param rss_data: string, containing rss data
    :return: ElementTree.Element object
    """
    root = ET.fromstring(rss_data)
    return root


def convert_root_to_dict(root: ET.Element) -> dict:
    """
    The function takes an ElementTree.Element object and returns a dictionary with required data structured for output.
    Tags that are required for the structure of the dictionary are set in required_data dict.
    Correct tags in which media data should be stored according to rss 2.0 standard are set in media_data dicts.
    1. iteration over root.iter() is done till the first 'item' tag is met to create rss-feed information pairs
    2. iteration over root.iter('item') is done to create rss-items information pairs and find items-media URLs.
    Rss-item date pairs are grouped using unified format datetime information as a key.
    \nThe function looks for media URLs in:
    1. text of sub-elements of elements, listed in media_dict
    2. attributes of elements, listed in media_dict
    3. text of elements, listed in media_dict
    4. attributes of elements <{.*}content>, <{.*}thumbnail> and <thumbnail>
    5. <img src> tags in text of elements (mostly <description>)

    :param root: an ET.Element object
    :return: dictionary with required data
    """
    feed_items = {}
    news_dict = {}
    required_data = ('title', 'description', 'link', 'pubDate')
    media_data = ('image', 'enclosure')

    for element in root.iter():  # Creating separate key-value pairs for <channel> tags
        if element.tag == 'item':
            break
        elif element.tag in media_data:
            media_dict = {subelement.tag: process_string(subelement.text) for subelement in element
                          if subelement.tag in ('url', 'type') and subelement.text}
            news_dict['feed_media'] = media_dict
        elif element.tag in required_data:
            news_dict['feed_' + element.tag] = process_string(element.text) if element.text else None

    for item in root.iter('item'):  # Creating separate key-value pairs for <item> tags
        temporary_item_dict = {}
        for element in item:
            if element.tag in media_data or re.search('{.+}content|{.+}thumbnail|thumbnail', element.tag):
                media_dict = {subelement.tag: subelement.text for subelement in element  # if no text - attribute text
                              if subelement.tag in ('url', 'type') and subelement.text}  # is either None or empty str
                if 'url' not in media_dict and 'url' in element.attrib:
                    media_dict['url'] = element.attrib['url']
                    if 'type' in element.attrib:  # to specify images from audio and video
                        media_dict['type'] = element.attrib['type']
                elif 'url' not in media_dict and element.text and re.search('http.?://', element.text):
                    media_dict['url'] = re.search('http.?://[^\\s<>]+', element.text)[0]
                temporary_item_dict['media'] = media_dict
            elif element.tag in required_data:
                temporary_item_dict[element.tag] = process_string(element.text) if element.text else None
                if element.text and re.search('img.*src=', element.text) and 'media' not in temporary_item_dict:
                    temporary_item_dict['media'] = {'url': re.search('src="[^"]+', element.text)[0][5:]}
        if temporary_item_dict.get('pubDate', None):
            feed_items[unify_pubdate(temporary_item_dict['pubDate'])] = temporary_item_dict
        else:
            feed_items[temporary_item_dict['title']] = temporary_item_dict
        news_dict['feed_items'] = feed_items
    return news_dict


def main(url: str) -> dict:
    """
    The function combines parts of the rss reader into a single script while handling exceptions
    :param url: URL of rss-feed
    :return: dictionary with required data
    """
    try:
        if validate_url(url):
            rss_data = get_rss_data(url)
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
            root = convert_rss_data_to_root(rss_data)
        except ET.ParseError as exc:
            print(f'Error while parsing rss data, possibly not an rss URL passed: ParseError code:{exc.code} {exc}')
        except Exception as exc:
            print(f'An unexpected error occurred while parsing rss data: {exc}')
        else:
            try:
                news_dict = convert_root_to_dict(root)
            except rss_exceptions.DateUnifyError as exc:
                print(f'Error occurred while converting datetime: {exc}')
            except TypeError as exc:
                print(f'Incorrect argument type while forming a news dictionary: {exc}')
            except ValueError as exc:
                print(f'Incorrect argument value while forming a news dictionary: {exc}')
            except KeyError as exc:
                print(f'An unexpected error occurred while forming a news dictionary: {exc}')
            except Exception as exc:
                print(f'An unexpected error occurred while forming a news dictionary: {exc}')
            else:
                return news_dict


if __name__ == '__main__':
    pass
    res_dict = main(rss_feed35)
    if res_dict:
        print(res_dict, file=open('res_dict.txt', 'w', encoding='utf-8'))
        news_date = None
        for date in res_dict['feed_items']:
            if news_date:
                if news_date in date:
                    for tag in res_dict['feed_items'][date]:
                        with open('result_rss_feed.txt', 'a', encoding='utf-8') as out:
                            print(date, tag, res_dict['feed_items'][date][tag], sep=' === ')
            else:
                for tag in res_dict['feed_items'][date]:
                    with open('result_rss_feed.txt', 'a', encoding='utf-8') as out:
                        print(date, tag, res_dict['feed_items'][date][tag], sep=' === ')
