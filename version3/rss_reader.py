import argparse
import datetime
import json
import pickle
import xml.etree.ElementTree as ET
from os.path import exists
from typing import Optional

import httpx

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DATE_FORMAT = "%Y-%m-%d"

PARSER = argparse.ArgumentParser(description='Pure Python command-line RSS reader.', prog="RSS Reader")
PARSER.add_argument('source', nargs='?', type=str, help="RSS URL")
PARSER.add_argument('--limit', type=int, help="Limit news topics if this parameter provided")
PARSER.add_argument('--version', action='version', version='%(prog)s 1.1')
PARSER.add_argument('--json', action='count', default=0, help="Print result as JSON in stdout")
PARSER.add_argument('--verbose', action='count', default=0, help="Outputs verbose status messages")
PARSER.add_argument(
    '--date', type=datetime.date.fromisoformat, dest="date",
    help=f"Get news from specific date from archives in format {DATE_FORMAT}"
)

CACHE_OBJECT = "local_cache.pickle"


class RSSNews:

    def __init__(
            self,
            title: str,
            link: str,
            pubDate: str,
            source: str,
            channel: str,
            *args, **kwargs,
    ):
        self.pubDate = datetime.datetime.strptime(pubDate, DATETIME_FORMAT)
        self.title = title
        self.link = link
        self.source = source
        self.channel = channel

    def to_dict(self) -> dict:
        return {
            "pubDate": self.pubDate.strftime(DATETIME_FORMAT),
            "title": self.title,
            "link": self.link,
            "source": self.source,
            "channel": self.channel,
        }


class RSS20Parser:

    def __init__(self, xml_tree: ET.Element, limit: int, verbose: bool):
        self.xml_tree = xml_tree
        self.limit = limit
        self.verbose = verbose

    def parse(self) -> list[RSSNews]:
        if self.verbose:
            print("LOG: Parsing the data of the RSS 2.0 format")
        news = []
        channel = self.xml_tree.find("channel/title").text
        for i, item in enumerate(self.xml_tree.findall("./channel/item")):
            if self.limit and i == self.limit - 1:
                return news
            single_news = {}
            for elem in item:
                try:
                    single_news[elem.tag] = elem.text
                except AttributeError:
                    pass

            news.append(RSSNews(**single_news, channel=channel))
        if self.verbose:
            print("LOG: Finished parsing")

        return news


def save_news_to_local_cache(news: list[RSSNews], verbose: bool):
    file_exists = exists(CACHE_OBJECT)
    if verbose:
        print("LOG: Saving data to local cache")
    if file_exists:
        if verbose:
            print("LOG: Local cache file exists, opening")
        with open(CACHE_OBJECT, 'rb+') as cache_file:
            try:
                cache_data: dict = pickle.load(cache_file)
            except EOFError:
                cache_data = {}
            data = append_to_existing_data(cache_data, news)
            pickle.dump(data, cache_file)
    else:
        if verbose:
            print("LOG: Local cache doesn't exists, creating")
        with open(CACHE_OBJECT, 'xb+') as cache_file:
            data = append_to_existing_data({}, news)
            pickle.dump(data, cache_file)
    if verbose:
        print("LOG: Saved data to file")


def append_to_existing_data(data: dict, news: list[RSSNews]) -> dict[str, list]:
    for i in news:
        news_dict = i.to_dict()
        pub_date = i.pubDate.strftime(DATE_FORMAT)
        if pub_date in data:
            data[pub_date].append(news_dict)
        else:
            data[pub_date] = [news_dict]

    return data


def get_xml_response(url: str, verbose: bool):
    if verbose:
        print(f"LOG: Querying data from source: {url}")
    response = httpx.get(url)
    if verbose:
        print(f"LOG: Queried data from source: {url}")
    return response.text


def parse_xml(xml_data: str | bytes, verbose: bool, limit: Optional[int] = None) -> list[RSSNews]:
    root = ET.fromstring(xml_data)
    if verbose:
        print("LOG: Starting parser block")
    match root.attrib['version']:
        case '2.0':
            parser = RSS20Parser(root, limit, verbose)
            data = parser.parse()
            return data
        case _:
            print("Not a valid or supported xml RSS feed!")


def format_console_text(news: list[RSSNews]):
    for i in news:
        result = f"""\nFeed: {i.channel}\n\nTitle: {i.title}\nDate: {i.pubDate}\nLink: {i.link}\n"""
        print(result)


def format_json(news: list[RSSNews]):
    return json.dumps([i.to_dict() for i in news])


def get_news_from_archive(date: datetime.date, limit: int, verbose: bool):
    if verbose:
        print("LOG: Loading data from local cache")
    news = []
    try:
        with open(CACHE_OBJECT, "rb") as cache_file:
            local_data = pickle.load(cache_file)
            date_str = date.strftime(DATE_FORMAT)
            if date_str not in local_data:
                print("No news for given date")
            else:
                for i, val in enumerate(local_data[date_str]):
                    if limit and i == limit - 1:
                        break
                    news.append(RSSNews(**val))
    except FileNotFoundError:
        if verbose:
            print("WARNING: Local cache file was not created, means no news been loaded")
        print("No news in local cache")
    return news


def main():
    args = PARSER.parse_args()
    source = args.source
    verbose = args.verbose
    json_output = args.json
    date = args.date
    if not source and not date:
        print("Source must be specified")
        return
    if date:
        news = get_news_from_archive(date=date, limit=args.limit, verbose=bool(verbose))
    else:
        result = get_xml_response(args.source, verbose)
        news = parse_xml(xml_data=result, limit=args.limit, verbose=verbose)
        save_news_to_local_cache(news=news, verbose=verbose)
    if not news:
        return
    if not json_output:
        if verbose:
            print("LOG: Preparing text formatted output")
        format_console_text(news)
    else:
        if verbose:
            print("LOG: Preparing json formatted output")
        print(format_json(news))


if __name__ == '__main__':
    main()
