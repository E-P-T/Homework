from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class RssItem:
    title: str
    description: str
    publication_date: datetime
    link: str
    image_url: str
    source: str = None

    def key(self):
        return self.link, self.publication_date


@dataclass
class RssFeed:
    rss_items: List[RssItem]
