"""Parsers (args and feed) """
import logging
import argparse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError as ConnError, ReadTimeout
from ..storage import Storage
from ..rss import RssFeed
from ..converter import Converter


class Parser:
    """ArgumentParser wrapper """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="rss_parser")
        self.__append_args_params()

    def __append_args_params(self) -> None:
        """
        Method initialized its own arguments
        :return: None
        """
        self.parser.add_argument("--version", help="Print version info", action='store_true')
        self.parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
        self.parser.add_argument('--verbose', help="Outputs verbose status messages", action="store_true")
        self.parser.add_argument("--limit", help="Limit news topics if this parameter provided", default=None, type=int)
        self.parser.add_argument("--date", help="Print result with actual publishing date of the news", default=None,
                                 type=str)
        self.parser.add_argument("--to-html", metavar="PATH", nargs="?", help="Prints RSS items into HTML format",
                                 default=argparse.SUPPRESS, const="", type=str)
        self.parser.add_argument("--to-pdf", metavar="PATH", nargs="?", help="Prints RSS items into PDF format",
                                 default=argparse.SUPPRESS, const="", type=str)
        self.parser.add_argument("source", nargs="?", help="RSS URL", type=str)

    @property
    def args(self) -> argparse.Namespace:
        """
        Returns self own arguments as Namespace object
        :return: Namespace
        """
        return self.parser.parse_args()

    def args_as_dict(self) -> dict:
        """
        Takes self own arguments and transforms them into dictionary
        :return: dictionary of self own arguments
        """
        return vars(self.args)

    def start_parse(self):
        """
        Creates RSS Parser object from a dictionary of self own arguments (params) and returns human-readable data
        (depends on params like a json and date)
        :return: human-readable data (Optional[str|json])
        """
        rss = RssParser(**self.args_as_dict())
        output_data = rss.get_data()
        return output_data


class RssParser:
    """
    RSS Parser
    """

    def __init__(self, source: str, limit: int, verbose: bool, json: bool, version: bool, date: str, **kwargs):
        self.feed = None
        self.url = source
        self.limit = limit
        self.version = version
        self.is_json = json
        self.is_verbose = verbose
        self.date = date
        self.to_pdf = kwargs.get("to_pdf", None)
        self.to_html = kwargs.get("to_html", None)
        self.storage = Storage()

    def get_data(self):
        """
        Main parsing method of RSS Feed

        Returns a result that depends on inputted params (self own arguments).
        Result can be limited by limit parameter (self.limit)
        After successful parsing saves data to local storage

        Also, if parser has a date argument, result will be loaded from local storage
        (which contains all entries from the previous parse).If the parser has date and source arguments,
        the result will also be loaded from local storage, but will be limited to the source only

        :returns:
         - version (if self.version is True)
         - feed (depends on json and date args)
        :exception: raises base Exception if inputted limit has negative value

        (base exception can be replaced by custom exception or will be replaced soon)


        """
        if self.is_verbose:
            logging.basicConfig(level=logging.DEBUG,
                                format="%(levelname)s: %(asctime)s - %(message)s",
                                datefmt="%d.%m.%Y %H:%M:%S")
        if self.version:
            logging.info("Current version")
            return 1.4
        if self.limit is not None and self.limit <= 0:
            logging.info(f"Fail! Limit must be more than zero (Your value is {self.limit})")
            raise Exception("Limit must be more that zero")
        if not self.date:
            logging.info("Trying to get RSS feed without date")
            if not self.url:
                logging.info("Fail! URL cannot be empty")
                raise Exception("URL cannot be empty")
            logging.info("Parsing started")
            text = self.get_response_data_or_exc()
            self.feed = self.get_feed(text)
            self.storage.save(self.url, self.feed.items)
        elif self.date:
            logging.info("Trying to get rss feed by date")
            storage_data = self.storage.load_by_date(self.date, self.url)
            self.feed = RssFeed(storage_data, self.limit)
        if self.to_html is not None:
            logging.info("Trying to converting feed to HTML format")
            converter = Converter(self.feed.to_json(), self.to_html)
            converter.to_html()
        if self.to_pdf is not None:
            logging.info("Trying to converting feed to PDF format")
            converter = Converter(self.feed.to_json(), self.to_pdf)
            converter.to_pdf()
        if self.is_json:
            logging.info("Transformation RSS feed into JSON format")
            return self.feed.to_json()

        return self.feed

    def get_feed(self, text):
        """
        Method which parses received text and splits it into tags (html)

        :param text: Response text (request.response)
        :return: RSSFeed object which contains rss title and items
        :exception: raises base Exception if received text don't have rss element
         -
        """
        soup = BeautifulSoup(text, features="html.parser")
        feed = soup.find("rss")
        if not feed:
            logging.info("Fail! URL does not contain RSS elements")
            raise Exception("URL is not an RSS feed")
        return RssFeed(feed, self.limit)

    def get_response_data_or_exc(self):
        """
        Method which check connection to inputted url

        :return: content for further parsing
        :exception: base Exception if url don't start with 'http'
        :exception: ConnectionError if request lib cannot connect to inputted url
        """
        if not self.url.startswith("http"):
            logging.info(f"Fail! Invalid URL")
            raise Exception("Fail! Invalid URL")
        try:
            with requests.get(self.url, timeout=5) as response:
                return response.content
        except (ConnError, ReadTimeout):
            logging.info(f"Fail! Cannot connect to {self.url}")
            raise ConnError(f"Failed Connect to {self.url}")
