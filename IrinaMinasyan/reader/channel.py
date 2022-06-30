"""This class implements RSS channel"""
import requests
import xml.etree.ElementTree as ET

from reader import item
from reader.exceptions import NotRssFormat, MissingHTTP
from reader import utils


class Channel:
    """Class which definite characteristics of the News Channel.
    Attributes
    _title : str
        The name for the feed.
    _link : str
        The url for the webpage containing information
        that directly relates to the feed.
    _date : str
        The date and time when the feed’s content is
        to be published.
    _description : str
        A phase or sentence that describes the feed.
    _items : list
        Each feed must contain at least one valid item entry(news).
    """

    def __init__(self, rss_url):
        """Initialise class Channel _title, _link,
        _description, _date and _item variables
        """
        try:
            response = requests.get(rss_url)
        except Exception:
            raise MissingHTTP
        try:
            channel_xml = ET.fromstring(response.text)
        except Exception:
            raise NotRssFormat
        self._title = channel_xml.find('channel').find('title').text
        self._link = channel_xml.find('channel').find('link').text
        self._description = channel_xml.find('channel').find('description').text
        self._date = utils.date_verification(channel_xml)
        self._items = [item.NewsItem(item_xml) for item_xml in channel_xml.iter('item')]

    def get_channel_title(self):
        """Get title of the channel"""
        return self._title

    def get_channel_link(self):
        """Get link of the channel"""
        return self._link

    def get_channel_description(self):
        """Get description of the channel"""
        return self._description

    def get_channel_date(self):
        """Get last update date of the channel"""
        return self._date

    def get_channel_news(self, limit=None):
        """Get all news or part of the news (if a limit is set) from the channel"""
        if (limit is None) or (limit > len(self._items)):
            return self._items
        else:
            limit_news = self._items[:limit]
            return limit_news
