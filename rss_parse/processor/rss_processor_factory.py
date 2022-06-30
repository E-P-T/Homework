import sys

from rss_parse.processor.rss_html_converter import RssToHtmlConverter
from rss_parse.processor.rss_pdf_converter import RssToPdfConverter
from rss_parse.processor.rss_processor import RssPrinter, RssJsonPrinter
from rss_parse.utils.messaging_utils import MESSAGE_CONSUMER_NOOP


def get_processors(rss_feed, params, mc=MESSAGE_CONSUMER_NOOP):
    """
    Fetch correct implementation of RssProcessor based on input parameters
    """
    processors = []

    if params.is_json:
        processors.append(RssJsonPrinter(rss_feed, mc=mc))
    else:
        processors.append(RssPrinter(rss_feed, sys.stdout, mc=mc))

    if params.html_dir:
        processors.append(RssToHtmlConverter(rss_feed, params.html_dir, mc=mc))

    if params.pdf_dir:
        processors.append(RssToPdfConverter(rss_feed, params.pdf_dir, mc=mc))

    return processors
