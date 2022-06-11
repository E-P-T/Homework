from datetime import datetime
from xml.etree.ElementTree import Element

from .Item import Item


class News:
    """
    News class
    """
    feed: str
    items: list[Item]

    def __init__(self, feed: str, items: list[Item]):
        self.feed = feed
        self.items = items

    @staticmethod
    def parse(element: Element, limit: int = None, date: datetime = None) -> 'News':
        """
        Parse XML element to News object
        """
        feed = element.find('title').text
        items = [Item.parse(item) for item in element.findall('item')]
        if date is not None:
            items = list(filter(lambda item: item.date.date() == date.date(), news.items))
        items = items[:limit]

        return News(feed, items)

    @staticmethod
    def parse_dict(news_dict: dict) -> 'News':
        """
        Parse a dictionary to News object
        """
        feed = news_dict.get('feed')

        items = news_dict.get('items')
        items = [Item.parse_dict(item) for item in items]

        return News(feed, items)
