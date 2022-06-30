from rss_parse.parse.rss_cache import CacheJsonParser
from rss_parse.parse.rss_parser import RssUrlParser
from rss_parse.utils.messaging_utils import MESSAGE_CONSUMER_NOOP


def get_parser(params, mc=MESSAGE_CONSUMER_NOOP):
    """
    Fetch correct implementation of RssParser based on input parameters
    """
    if params.pub_date:
        return CacheJsonParser(params.pub_date, params.source, mc=mc)
    return RssUrlParser(params.source, mc=mc)
