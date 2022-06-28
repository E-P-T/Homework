import sys

from rss_parse.processor.rss_processor import RssPrinter, RssJsonPrinter
from rss_parse.utils.message_consumer import MESSAGE_CONSUMER_NOOP


def get_processor(rss_feed, is_json=False, mc=MESSAGE_CONSUMER_NOOP):
    if is_json:
        return RssJsonPrinter(rss_feed, mc=mc)
    return RssPrinter(rss_feed, sys.stdout, mc=mc)
