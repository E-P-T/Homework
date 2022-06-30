import unittest

from rss_reader import RSSNews, format_console_text, parse_xml


def get_sample_news_object():
    return RSSNews(
        title="test",
        link="test",
        pubDate="2022-06-28T22:01:51Z",
        source="test",
        channel="test"
    )


class RssReaderTestCase(unittest.TestCase):

    def test_to_dict_return_dict_of_the_class(self):
        news = get_sample_news_object()

        self.assertEqual(
            news.to_dict(), {
                "title": "test",
                "link": "test",
                "pubDate": "2022-06-28T22:01:51Z",
                "source": "test",
                "channel": "test",
                "image": None,
            }
        )

    def test_formatted_output_is_correct(self):
        news = get_sample_news_object()

        result = format_console_text([news])
        expected_string = f"\nFeed: {news.channel}\n\nTitle: {news.title}\nDate: {news.pubDate}\nLink: {news.link}\n"

        self.assertEqual(result, expected_string)

    def test_xml_parser_chooses_proper_rss_format(self):
        xml_string = """<rss version="2.0">
            <channel>
            <title>Yahoo News - Latest News  Headlines</title>
            <link>https://www.yahoo.com/news</link>
            <description>
            The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
            </description>
            <language>en-US</language>
            <copyright>Copyright (c) 2022 Yahoo! Inc. All rights reserved</copyright>
            <pubDate>Thu, 30 Jun 2022 07:45:03 -0400</pubDate>
            <ttl>5</ttl>
            <image>
            <title>Yahoo News - Latest News  Headlines</title>
            <link>https://www.yahoo.com/news</link>
            <url>
            http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png
            </url>
            </image>
            <item>
            <title>Spit, 'disrespect' arrive at Wimbledon as tennis turns ugly</title>
            <link>https://news.yahoo.com/spit-disrespect-arrive-wimbledon-tennis-220151441.html</link>
            <pubDate>2022-06-28T22:01:51Z</pubDate>
            <source url="http://www.ap.org/">Associated Press</source>
            <guid isPermaLink="false">
                spit-disrespect-arrive-wimbledon-tennis-220151441.html
            </guid>
            </item>
            </channel>
            </rss>
            """
        news = parse_xml(xml_data=xml_string, verbose=False, limit=0)

        self.assertEqual(news[0].to_dict(), RSSNews(pubDate="2022-06-28T22:01:51Z",
                                                    title="Spit, 'disrespect' arrive at Wimbledon as tennis turns ugly",
                                                    link="https://news.yahoo.com/spit-disrespect-arrive-wimbledon-tennis-220151441.html",
                                                    source="Associated Press",
                                                    channel="Yahoo News - Latest News  Headlines"
                                                    ).to_dict())
