import json
from datetime import timezone, datetime

from rss_parse.parse.rss_feed import RssFeed, RssItem
from rss_parse.parse.rss_keys import *
from rss_parse.utils.formatting_utils import format_date_pretty, get_description_plain


class RssJsonMapper:
    """
    Class to do a conversion of RSS Feed TO and FROM json
    """
    __DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def to_json(self, rss_feed: RssFeed, indent=None, pretty=False):
        res = {
            RSS_ITEMS: [self.__item_to_json(item, pretty) for item in rss_feed.rss_items]
        }

        return json.dumps(res, indent=indent, ensure_ascii=False)

    def __item_to_json(self, item: RssItem, pretty):
        res = {
            RSS_ITEM_TITLE: item.title,
            RSS_ITEM_LINK: item.link,
        }
        # Store as UTC
        publication_date = item.publication_date.astimezone(timezone.utc) \
            .strftime(RssJsonMapper.__DATE_TIME_FORMAT)
        description = item.description
        if pretty:
            publication_date = format_date_pretty(item.publication_date)
            description = get_description_plain(description)

        res[RSS_ITEM_PUB_DATE] = publication_date

        if description:
            res[RSS_ITEM_DESCRIPTION] = description

        if item.image_url:
            res[RSS_IMAGE_ROOT] = item.image_url

        if item.source:
            res[RSS_SOURCE] = item.source

        return res

    def from_json(self, rss_feed_json):
        rss_dict = json.loads(rss_feed_json)
        items = [self.__parse_item(item) for item in rss_dict[RSS_ITEMS]]
        return RssFeed(items)

    def __parse_item(self, item):
        title = item[RSS_ITEM_TITLE]
        description = item.get(RSS_ITEM_DESCRIPTION, None)
        publication_date = datetime.strptime(item[RSS_ITEM_PUB_DATE], RssJsonMapper.__DATE_TIME_FORMAT) \
            .replace(tzinfo=timezone.utc).astimezone()
        link = item[RSS_ITEM_LINK]
        image_url = item.get(RSS_IMAGE_ROOT, None)
        source = item.get(RSS_SOURCE, None)
        return RssItem(title, description, publication_date, link, image_url, source)


RSS_FEED_JSON_MAPPER = RssJsonMapper()
