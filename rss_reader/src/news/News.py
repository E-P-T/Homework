from xml.etree.ElementTree import Element

from .Item import Item


class News:
    """
    News class
    """
    feed: str
    items: list[Item]

    @staticmethod
    def parse(element: Element, limit: int = None) -> 'News':
        """
        Parse XML element to News object
        """
        news = News()
        news.feed = element.find('title').text
        news.items = [Item.parse(item) for item in element.findall('item')[:limit]]

        return news
