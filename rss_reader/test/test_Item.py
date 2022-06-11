from unittest import TestCase
from xml.etree.ElementTree import fromstring

from dateutil.parser import parse as parse_date

from rss_reader.src.news.Item import Item


class TestItem(TestCase):
    def test_parse(self):
        title = 'Title'
        link = 'https://example.com'
        date = 'Mon, 1 Jan 2000 12:00:00 GMT'

        rss = f'''
        <item>
            <title>{title}</title>
            <link>{link}</link>
            <pubDate>{date}</pubDate>
        </item>
        '''

        item = Item.parse(fromstring(rss))

        self.assertEqual(item.title, title)
        self.assertEqual(item.link, link)
        self.assertEqual(item.date, parse_date(date))

    def test_parse_dict(self):
        title = 'Title'
        link = 'https://example.com'
        date = 'Mon, 1 Jan 2000 12:00:00 GMT'

        dict = {
            'title': title,
            'link': link,
            'date': date
        }

        item = Item.parse_dict(dict)

        self.assertEqual(item.title, title)
        self.assertEqual(item.link, link)
        self.assertEqual(item.date, parse_date(date))
