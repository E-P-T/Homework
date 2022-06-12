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
            items = list(filter(lambda item: item.date.date() == date.date(), items))
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

    def to_html(self) -> str:
        items = '\n'.join(list(map(Item.to_html, self.items)))
        html = f'''
        <!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>News</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" 
                integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
            </head>
            <body>
                <div class="container">
                <h1 class="text-center">Feed: {self.feed}</h1>
                {items}
                </div>
            </body>
        </html>
        '''

        return html
