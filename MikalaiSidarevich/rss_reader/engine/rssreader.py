"""
RssReader - pure Python command-line RSS reader.
"""

from engine.converter import Converter
from engine.rsscacher import RssCacher
from engine.rssparser import RssParser


class RssReader:
    """Pure Python command-line RSS reader."""

    def __init__(self, verbose=False, dbname="storage.db"):
        """
        Initialize reader with `verbose` ability, storage `dbname`.
        """
        self._verbose = verbose
        self._dbname = dbname

    def read_rss(self, url, limit, json, date):
        """
        Get RSS entries from `url` and output them to the stdout.
        Limit number of entries with `limit`.
        Output all the entries if `limit` is not specified.
        Read news from cache by `date` if specified.
        """
        try:
            with RssCacher(self._dbname, self._verbose) as cacher:
                parser = RssParser(cacher, self._verbose)

                if date is None:
                    feed_list = parser.feed(url, limit)
                else:
                    feed_list = cacher.feed(url, limit, date)
        except Exception:
            raise

        if json:
            rss_content = Converter.to_json(feed_list)
        else:
            rss_content = Converter.to_text(feed_list)

        return rss_content
