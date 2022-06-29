import datetime
import unittest
from unittest.mock import patch
from dateutil.tz import tzutc
from rss_reader.parsing import parse_rss
from rss_reader.exceptions import ParserError

test_content = {
    'http://example.com/rss/': '''
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:media='http://example.com/rss/' version='2.0'>
   <channel>
      <title>Feed title</title>
      <link>http://example.com/</link>
      <item>
         <title>Item title 1</title>
         <link>http://example.com/item_1.html</link>
         <pubDate>2022-06-22T12:12:12Z</pubDate>
         <media:content url='http://example.com/item_1.jpg' medium='image'/>
         <description>
            <![CDATA[<img alt='Image comment' src='http://example.com/files/item_1.jpg'/>Item description 1<a href='http://example.com/item_1.html'>Link comment</a>]]>
         </description>
      </item>
      <item>
         <title>Item title 2</title>
         <link>http://example.com/item_2.html</link>
         <pubDate>Fri, 24 Jun 2022 12:12:12 +0000</pubDate>
      </item>
   </channel>
</rss>'''}


class MockResponse:
    def __init__(self, url):
        self.content = test_content.get(url, '')


def mock_requests_get(url):
    return MockResponse(url)


class TestParsing(unittest.TestCase):
    @patch('rss_reader.parsing.requests.get', side_effect=mock_requests_get)
    def test_parse_rss(self, *args):
        feed = parse_rss('http://example.com/rss/')
        self.assertDictEqual(feed, {'http://example.com/rss/': {'feed_title': 'Feed title', 'feed_items': [
            {'item_title': 'Item title 1',
             'item_pub_date': datetime.datetime(2022, 6, 22, 12, 12, 12, tzinfo=tzutc()),
             'item_url': 'http://example.com/item_1.html',
             'item_desc_text': '[1 Image comment]Item description 1[2 Link comment]',
             'item_desc_links': [
                 {'link_pos': 1,
                  'link_url': 'http://example.com/files/item_1.jpg',
                  'link_type': 'image'},
                 {'link_pos': 2,
                  'link_url': 'http://example.com/item_1.html',
                  'link_type': 'link'}],
             'item_image_url': 'http://example.com/item_1.jpg'},
            {'item_title': 'Item title 2',
             'item_pub_date': datetime.datetime(2022, 6, 24, 12, 12, 12, tzinfo=tzutc()),
             'item_url': 'http://example.com/item_2.html',
             'item_desc_text': '',
             'item_desc_links': [],
             'item_image_url': ''}]}})
        self.assertRaises(ParserError, parse_rss, 'not a valid url')


if __name__ == '__main__':
    unittest.main()
