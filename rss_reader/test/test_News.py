from unittest import TestCase
from xml.etree.ElementTree import fromstring

from dateutil.parser import parse as parse_date

from rss_reader.src.news.News import News


class TestNews(TestCase):
    def test_parse(self):
        feed = 'RSS Title'
        title = 'Title'
        link = 'https://example.com'
        date = 'Mon, 1 Jan 2000 12:00:00 GMT'

        rss = f'''
        <channel>
            <title>{feed}</title>
            <item>
                <title>{title}</title>
                <link>{link}</link>
                <pubDate>{date}</pubDate>
            </item>
        </channel>
        '''

        news = News.parse(fromstring(rss))
        self.assertEqual(news.feed, feed)
        self.assertEqual(len(news.items), 1)

        item = news.items[0]
        self.assertEqual(item.title, title)
        self.assertEqual(item.link, link)
        self.assertEqual(item.date, parse_date(date))
