"""This class implements RSS channel news items"""
import json
import requests

from bs4 import BeautifulSoup
from html2text import HTML2Text
from reader.exceptions import NoImgFound
from reader import utils


class NewsItem:
    """Class which definite characteristics of the News item.
    Attributes
    _title : str
        The headline for the item’s content.
    _link : str
        The URL for the webpage, or for the section of a webpage,
        that contains the item’s full content.
    _date : str
        The date and time when the item is to be made available.
    """

    def __init__(self, item_xml):
        """Initialise class NewItem _title, _link
        and _date variables"""
        self._title = item_xml.find('title').text
        self._link = item_xml.find('link').text
        self._date = item_xml.find('pubDate').text
        self._description = utils.description_verification(item_xml)
        self._media_content = utils.media_content_verification(item_xml)
        self._image = utils.image_verification(item_xml)

    def get_title(self):
        """Get title of the news item"""
        return self._title

    def get_link(self):
        """Get link of the news item"""
        return self._link

    def get_date(self):
        """Get date to create of the news item"""
        return self._date

    def get_news(self):
        """Get the first piece of the news item"""
        news_url = requests.get(self.get_link())
        soup = BeautifulSoup(news_url.content, 'html.parser')
        all_news = soup.find_all('p')
        to_text = HTML2Text()
        to_text.ignore_links = True
        return to_text.handle(''.join(str(all_news[i]) for i in range(min(len(all_news), 3))))

    def find_image_link(self):
        """Find image link from the parsed page."""
        if self._image:
            return self._image
        if self._media_content:
            return self._media_content['url']
        if self._description:
            desc_soup = BeautifulSoup(self._description, 'html.parser')
            try:
                image_item = desc_soup.find('img')
                image = image_item.get('src')
                return image
            except Exception:
                raise NoImgFound

    def get_image(self):
        """Get news item image link """
        try:
            image = self.find_image_link()
            return image
        except NoImgFound:
            print(NoImgFound.__doc__)
            pass

    def get_json(self):
        """Get JSON representation of the news item"""
        return json.dumps({"Title": self.get_title(),
                           "Date": self.get_date(),
                           "Link": self.get_link(),
                           "Image link": self.get_image()}, ensure_ascii=False)

    def print_news(self):
        """Prints title, link, date and the first piece of the news item"""
        print(self.get_title())
        print(self.get_date())
        print(self.get_link())
        print(self.get_image())

