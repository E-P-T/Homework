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

    def __init__(self, title: str, date: datetime, link: str, images: list[str]):
        self.title = title
        self.date = date
        self.link = link
        self.images = images

    @staticmethod
    def parse(element: Element) -> 'Item':
        """
        Parse an XML element into a news item.
        """
        title = element.find('title').text
        date = parse_date(element.find('pubDate').text)
        link = element.find('link').text
        images = [
            image.attrib['url'] for image in
            element.findall('*[@width][@height]')
        ]

        return Item(title, date, link, images)

    @staticmethod
    def parse_dict(item_dict: dict) -> 'Item':
        """
        Parse a dictionary into a news item.
        """

        title = item_dict.get('title')
        date = parse_date(item_dict.get('date'))
        link = item_dict.get('link')
        images = item_dict.get('images')

        return Item(title, date, link, images)

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__

    def to_html(self) -> str:
        images = '\n'.join(list(map(lambda image: f'<img src="{image}" class="w-100">', self.images)))

        return f'''
        <div class="fs-4">
            <hr>
            <div><span class="fw-semibold">Title: </span>{self.title}</div>
            <div><span class="fw-semibold">Date: </span>{self.date}</div>
            <div><span class="fw-semibold">Link: </span>{self.link}</div>
            {images}
        </div>
        '''
