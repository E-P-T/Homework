"""
RssReader - pure Python command-line RSS reader.
"""

from engine.converter import Converter
from engine.rssparser import RssParser


class RssReader:
    """Pure Python command-line RSS reader."""

    def __init__(self, verbose):
        """
        Initialize reader with `verbose` ability.
        """
        self._verbose = verbose

    def read_rss(self, url, limit, json):
        """
        Get RSS entries from `url` and output them to the stdout.
        Limit number of entries with `limit`.
        Output all the entries if `limit` is not specified.
        """
        try:
            parser = RssParser(self._verbose)
            feed = parser.feed(url, limit)
        except Exception:
            raise

        if json:
            rss_content = Converter.to_json(feed)
        else:
            rss_content = Converter.to_text(feed)

        return rss_content
