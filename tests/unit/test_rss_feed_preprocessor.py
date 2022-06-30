from datetime import datetime

from rss_parse.parse.rss_feed import RssFeed, RssItem
from rss_parse.preprocessor.rss_preprocessor import RssSortPreprocessor, RssLimitPreprocessor


def rss_item(pub_date):
    return RssItem("", "", pub_date, "", "")


def test_rss_sort_preprocessor():
    d1 = rss_item(datetime(2019, 10, 28))
    d2 = rss_item(datetime(2018, 10, 28))
    d3 = rss_item(datetime(2020, 8, 12, 12, 12, 14))
    d4 = rss_item(datetime(2020, 8, 12, 11, 12, 14))
    rss_feed = RssFeed([d1, d2, d3, d4])
    preprocessor = RssSortPreprocessor()
    actual = preprocessor.preprocess(rss_feed)
    assert actual == RssFeed([d3, d4, d1, d2])


def test_rss_limit_preprocessor_shrink():
    d1 = rss_item(datetime(2019, 10, 28))
    d2 = rss_item(datetime(2018, 10, 28))
    d3 = rss_item(datetime(2020, 8, 12, 12, 12, 14))
    d4 = rss_item(datetime(2020, 8, 12, 11, 12, 14))
    rss_feed = RssFeed([d1, d2, d3, d4])
    preprocessor = RssLimitPreprocessor(2)
    actual = preprocessor.preprocess(rss_feed)
    assert actual == RssFeed([d1, d2])


def test_rss_limit_preprocessor_more_than_max_all():
    d1 = rss_item(datetime(2019, 10, 28))
    d2 = rss_item(datetime(2018, 10, 28))
    d3 = rss_item(datetime(2020, 8, 12, 12, 12, 14))
    d4 = rss_item(datetime(2020, 8, 12, 11, 12, 14))
    rss_feed = RssFeed([d1, d2, d3, d4])
    preprocessor = RssLimitPreprocessor(20)
    actual = preprocessor.preprocess(rss_feed)
    assert actual == rss_feed
