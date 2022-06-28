from rss_parse.parse.rss_feed_cache import CacheJsonParser
from rss_parse.parse.rss_parser import RssUrlParser
from rss_parse.utils.message_consumer import MESSAGE_CONSUMER_NOOP


def get_parser(date, source, mc=MESSAGE_CONSUMER_NOOP):
    if date:
        return CacheJsonParser(date, source, mc=mc)
    return RssUrlParser(source, mc=mc)
