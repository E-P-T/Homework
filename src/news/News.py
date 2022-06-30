from datetime import datetime
from xml.etree.ElementTree import Element

from Util import Util
from news.Item import Item


class News:
    feed: str
    items: list[Item]

    @classmethod
    def parse_element(cls, element: Element, limit: int, date: datetime) -> 'News':
        news = cls()
        news.feed = element.find('title').text

        items = [Item.parse_element(item) for item in element.findall('item')]
        if date is not None:
            items = cls.date_filter(items, date)

        news.items = items[:limit]

        return news

    @classmethod
    def parse_json(cls, obj: dict) -> 'News':
        news = cls()
        news.feed = obj['feed']
        news.items = list(map(
            lambda item: Item.parse_json(item),
            obj['items']
        ))

        return news

    def __str__(self) -> str:
        items = [Util.vars_to_string(self), 'Items:',
                 Util.make_indent('\n\n'.join(map(str, self.items)))]
        return '\n'.join(items)

    @classmethod
    def date_filter(cls, items: list[Item], date: datetime) -> list[Item]:
        date_format = '%Y-%m-%d'
        return list(filter(
            lambda item:
            item.date.strftime(date_format) == date.strftime(date_format),
            items
        ))

    def to_fb2(self) -> str:
        content = '<?xml version="1.0" encoding="UTF-8"?>' \
                  '<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" ' \
                  'xmlns:l="http://www.w3.org/1999/xlink">' \
                  '<description>' \
                  '<title-info>' \
                  f'<book-title>{self.feed}</book-title>' \
                  '</title-info>' \
                  '</description>' \
                  '<body>'
        i = 0
        for item in self.items:
            content += item.to_fb2(i)
            i += 1
        content += '</body>'
        i = 0
        for item in self.items:
            content += item.to_fb2_images(i)
            i += 1
        content += '</FictionBook>'

        return content

    def to_html(self) -> str:
        content = '<!DOCTYPE html>' \
                  '<html>' \
                  '<head>' \
                  '<meta charset="utf-8">' \
                  '<meta name="viewport" content="width=device-width, initial-scale=1">' \
                  '<title>News</title>' \
                  '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">' \
                  '</head>' \
                  '<body>' \
                  '<section class="section">' \
                  '<div class="container">' \
                  f'<h1 class="has-text-centered title">{self.feed}</h1>'
        for item in self.items:
            content += item.to_html()
        content += '</div>' \
                   '</section>' \
                   '</body>' \
                   '</html>'

        return content
