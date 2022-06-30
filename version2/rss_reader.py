import argparse
import datetime
import json
import xml.etree.ElementTree as ET
from typing import Optional

import httpx

PARSER = argparse.ArgumentParser(description='Pure Python command-line RSS reader.', prog="RSS Reader")
PARSER.add_argument('source', type=str, help="RSS URL")
PARSER.add_argument('--limit', type=int, help="Limit news topics if this parameter provided")
PARSER.add_argument('--version', action='version', version='%(prog)s 1.1')
PARSER.add_argument('--json', action='count', default=0, help="Print result as JSON in stdout")
PARSER.add_argument('--verbose', action='count', default=0, help="Outputs verbose status messages")

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


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

    def to_dict(self):
        return {
            "pub_date": self.pubDate.strftime(DATETIME_FORMAT),
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
            if self.limit and i == self.limit:
                return news
            single_news = {}
            for elem in item:
                try:
                    single_news[elem.tag] = elem.text.encode('utf8')
                except AttributeError:
                    pass

            news.append(RSSNews(**single_news, channel=channel))
        print("LOG: Finished parsing")
        return news


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


def main():
    args = PARSER.parse_args()
    verbose = args.verbose
    json_output = args.json
    result = get_xml_response(args.source, verbose)
    news = parse_xml(xml_data=result, limit=args.limit, verbose=verbose)
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
