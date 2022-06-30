import unittest
from rss_reader_package.mocks.raw_feed_mock import mock_feed_raw
from rss_reader_package.feed import Feed


class TestFeed(unittest.TestCase):
    parsed_feed = Feed.json_to_feed(mock_feed_raw)

    def test_process_feed(self):
        self.assertEqual(TestFeed.parsed_feed.source_title, "The Daily")
        self.assertEqual(TestFeed.parsed_feed.title, "Why Is It So Hard to Buy a House in America Right Now?")
        self.assertEqual(TestFeed.parsed_feed.date, "Tue, 21 Jun 2022 09:50:00 +0000")
        self.assertEqual(TestFeed.parsed_feed.link,
                         "https://www.nytimes.com/the-daily")
        self.assertEqual(len(TestFeed.parsed_feed.content), 1139)
        self.assertEqual(len(TestFeed.parsed_feed.non_media_links), 3)
        self.assertEqual(TestFeed.parsed_feed.media_links[0].href,
                         "https://dts.podtrac.com/redirect.mp3/chrt.fm/track/8DB4DB/pdst.fm/e/nyt.simplecastaudio.com/"
                         "03d8b493-87fc-4bd1-931f-8a8e9b945d8a/episodes/230797bf-6d47-4648-81b5-79750b8d8023/audio/"
                         "128/default.mp3?aid=rss_feed&awCollectionId=03d8b493-87fc-4bd1-931f-8a8e9b945d8a&awEpisodeId="
                         "230797bf-6d47-4648-81b5-79750b8d8023&feed=54nAGcIl")

    def test_to_json(self):
        self.assertEqual(type(TestFeed.parsed_feed.to_json()), str)

    def test_to_readable(self):
        self.assertEqual(type(TestFeed.parsed_feed.to_json()), str)


unittest.main()
