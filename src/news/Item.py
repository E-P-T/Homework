from datetime import datetime
from xml.etree.ElementTree import Element

from dateutil.parser import parse as parse_date

from Util import Util


class Item:
    title: str
    date: datetime
    link: str
    images: list[str]

    @classmethod
    def parse_element(cls, element: Element) -> 'Item':
        item = cls()

        item.title = element.find('title').text
        item.date = parse_date(element.find('pubDate').text)
        item.link = element.find('link').text
        item.images = [
            image.attrib['url'] for image in
            element.findall('*[@width][@height]')
        ]

        return item

    @classmethod
    def parse_json(cls, obj: dict) -> 'Item':
        item = cls()
        item.title = obj['title']
        item.date = parse_date(obj['date'])
        item.link = obj['link']
        item.images = obj['images']

        return item

    def __str__(self) -> str:
        items = [Util.vars_to_string(self), 'Images:',
                 Util.make_indent('\n'.join(self.images))]

        return '\n'.join(items)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Item) and \
               Util.vars_to_string(self) \
               == Util.vars_to_string(o)

    def to_fb2(self, images_id: str) -> str:
        content = '<section>' \
                  '<title>' \
                  f'<p>{self.title}</p>' \
                  '</title>' \
                  f'<p>{self.date}</p>' \
                  f'<p>{self.link}</p>'
        for i in range(len(self.images)):
            image_id = f'{images_id}{i}'
            content += f'<p><image l:href="#{image_id}"/></p>'
        content += '</section>'

        return content

    def to_fb2_images(self, images_id: str) -> str:
        content = ''
        i = 0
        for image in self.images:
            image_id = f'{images_id}{i}'
            content += f'<binary id="{image_id}" content-type="image/png">' \
                       f'{Util.to_base64(image)}' \
                       '</binary>'
            i += 1

        return content

    def to_html(self) -> str:
        content = '<div>' \
                  '<hr>' \
                  f'<h1 class="title">{self.title}</h1>' \
                  f'<h1 class="title">{self.date}</h1>' \
                  '<div class="columns is-align-items-center">'
        for image in self.images:
            content += '<div class="column">' \
                       f'<img src="{image}">' \
                       '</div>'
        content += '</div>' \
                   '<hr>' \
                   '</div>'

        return content
