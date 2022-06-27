import datetime
from unittest import TestCase
from news.News import News


class TestNews(TestCase):
    def test_parse_json(self):
        feed = 'test_feed'
        title = 'test_title'
        date = datetime.datetime.today()
        link = 'test_link'
        images = ['test_image']
        obj = {
            'feed': feed,
            'items': [{
                'title': title,
                'date': str(date),
                'link': link,
                'images': images
            }]
        }

        news = News.parse_json(obj)
        self.assertEqual(news.feed, feed)
        self.assertEqual(len(news.items), 1)

        item = news.items[0]
        self.assertEqual(item.title, title)
        self.assertEqual(item.date, date)
        self.assertEqual(item.link, link)
        self.assertEqual(item.images, images)

