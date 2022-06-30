from loguru import logger
import requests
from bs4 import BeautifulSoup
import re
import sys


class Reader:
    """Parse data from URL"""

    def __init__(self, source: str, limit=-1) -> None:
        self.version = '4.0'
        self.source = source
        self.name = self.get_acces()[0]
        self.items = self.get_acces()[1]
        logger.info("Acces is available (info)!")
        self.limit = len(self.items) if limit == -1 or limit > len(self.items) else limit
        self.title = self.get_title()
        logger.info("Title is available (info)!")
        self.pubDate = self.get_pubDate()
        logger.info("PubDate is available (info)!")
        self.link = self.get_link()
        logger.info("Link is available (info)!")
        self.clear_description = list()
        self.description = self.get_description()
        logger.info("Description is available (info)!")

    def get_acces(self) -> list:
        logger.debug("Get access (debug)!")
        try:
            url = requests.get(self.source)
        except Exception:
            logger.info(f"Invalid url.{self.source}(info)!")
            print('Could not fetch the URL. Input valid URL.')
            sys.exit()
        try:
            soup = BeautifulSoup(url.content, 'xml')
            name = soup.find().title.text
            items = soup.find_all('item')
            if len(items) == 0:
                raise Exception
        except Exception as e:
            logger.info(f"Invalid url.{self.source}(info)!")
            print('Could not read feed. Input xml-format URL.')
            sys.exit()
        return name, items

    def get_title(self) -> list:
        logger.debug("Get title from xml (debug)!")
        return [self.items[i].title.text for i in range(self.limit)]

    def get_pubDate(self) -> list:
        logger.debug("Get pubDate from xml (debug)!")
        print([self.items[i].pubDate.text for i in range(self.limit)])
        return [self.items[i].pubDate.text for i in range(self.limit)]

    def get_link(self) -> list:
        logger.debug("Get link from xml (debug)!")
        return [self.items[i].link.text for i in range(self.limit)]

    def get_description(self) -> list:
        logger.debug("Get description from xml (debug)!")
        des = []
        for i in range(self.limit):
            if self.items[i].description:
                des.append(self.items[i].description.text)
                self.clear_description.append(re.sub(r'\<[^>]*\>|(&rsaquo)', '', self.items[i].description.text))
            else:
                des.append('No description here')
                self.clear_description.append('No description here')
        return des
