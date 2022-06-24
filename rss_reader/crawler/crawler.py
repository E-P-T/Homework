

from rss_reader.interfaces.icrawler.icrawler import ICrawler


class SuperCrawler(ICrawler):
    def __init__(self, url: str) -> None:
        self._url = url
