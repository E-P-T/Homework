import argparse
import requests
from requests.exceptions import ConnectionError, MissingSchema
import logging
from bs4 import BeautifulSoup
from rss_parser.rss import RssFeed


class Parser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="rss_parser")
        self.__append_args_params()

    def __append_args_params(self) -> None:
        self.parser.add_argument("--version", help="Print version info", action='store_true')
        self.parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
        self.parser.add_argument('--verbose', help="Outputs verbose status messages", action="store_true")
        self.parser.add_argument("--limit", help="Limit news topics if this parameter provided", default=None, type=int)
        self.parser.add_argument("source", nargs="?", help="RSS URL", type=str)

    @property
    def args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def args_as_dict(self) -> dict:
        return vars(self.args)

    def start_parse(self):
        rss = RssParser(**self.args_as_dict())
        output_data = rss.get_data()
        return output_data


class RssParser:
    def __init__(self, source, limit, verbose, json, version):
        self.feed = None
        self.url = source
        self.limit = limit
        self.version = version
        self.is_json = json
        self.is_verbose = verbose

    def get_data(self):
        if self.is_verbose:
            logging.basicConfig(level=logging.DEBUG,
                                format="%(levelname)s: %(asctime)s - %(message)s",
                                datefmt="%d.%m.%Y %H:%M:%S")
        if self.version:
            logging.info("Current version")
            return 1.2
        if not self.url:
            logging.info("Fail! URL cannot be empty")
            raise Exception("URL cannot be empty")
        if self.limit is not None and self.limit <= 0:
            logging.info(f"Fail! Limit must be more than zero (Your value is {self.limit})")
            raise Exception("Limit must be more that zero")
        logging.info("Parsing started")
        text = self.get_response_data_or_exc()
        self.feed = self.get_feed(text)
        if self.is_json:
            logging.info("Transformation RSS feed into JSON format")
            return self.feed.to_json()
        return self.feed

    def get_feed(self, text):
        soup = BeautifulSoup(text, features="html.parser")
        feed = soup.find("rss")
        if not feed:
            logging.info("Fail! URL does not contain RSS elements")
            raise Exception("URL is not an RSS feed")
        return RssFeed(feed, self.limit)

    def get_response_data_or_exc(self):
        if not self.url.startswith("http"):
            logging.info(f"Fail! Invalid URL")
            raise Exception("Fail! Invalid URL")
        try:
            with requests.get(self.url) as response:
                return response.content
        except ConnectionError:
            logging.info(f"Fail! Cannot connect to {self.url}")
            raise Exception(f"Failed Connect to {self.url}")
