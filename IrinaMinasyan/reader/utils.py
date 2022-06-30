import json
import sys

from reader.add_args import args
from reader import channel
from reader.exceptions import MissingHTTP, NotRssFormat, URLError


def date_verification(channel_xml):
    """Date attribute verification."""
    try:
        return channel_xml.find('channel').find('pubDate').text
    except AttributeError:
        pass


def description_verification(item_xml):
    """Description attribute verification"""
    try:
        return item_xml.find('description').text
    except AttributeError:
        pass


def media_content_verification(item_xml):
    """Media attribute verification"""
    try:
        namespaces = {'media': "http://search.yahoo.com/mrss/"}
        media_content = item_xml.find("{%s}content" % namespaces['media'])
        return {'url': media_content.get('url')}
    except AttributeError:
        pass


def image_verification(item_xml):
    """Image attribute verification"""
    try:
        return item_xml.find('image').text
    except AttributeError:
        pass


def verification():
    """Create a channel object """
    try:
        instance = channel.Channel(args.source)
        return instance
    except NotRssFormat:
        print(NotRssFormat.__doc__)
        sys.exit()
    except MissingHTTP:
        print(MissingHTTP.__doc__)
        sys.exit()
    except Exception:
        raise URLError


def dump_news_to_json(news_item):
    """Prints json format news as title-instance"""
    json_news = json.loads(news_item.get_json())
    for key, value in json_news.items():
        print(f'{key}:{value}')
