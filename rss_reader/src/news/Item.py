from datetime import datetime
from xml.etree.ElementTree import Element

from dateutil.parser import parse as parse_date


class Item:
    """
    Class for a news item.
    """
    title: str
    date: datetime
    link: str
    images: list[str]

    @staticmethod
    def parse(element: Element) -> 'Item':
        """
        Parse an XML element into a news item.
        """
        item = Item()
        item.title = element.find('title').text
        item.date = parse_date(element.find('pubDate').text)
        item.link = element.find('link').text
        item.images = [
            image.attrib['url'] for image in
            element.findall('*[@width][@height]')
        ]

        return item
