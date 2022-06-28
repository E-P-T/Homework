from rss_parse.parse.rss_parser import RssUrlParser
from rss_parse.utils.message_consumer import MESSAGE_CONSUMER_NOOP


def get_parser(source, mc=MESSAGE_CONSUMER_NOOP):
    return RssUrlParser(source, mc=mc)
