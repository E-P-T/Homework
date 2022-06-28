import logging
import logging.config

from args import get_args
from rss.rss_classes import Feed
from rss.rss_parser import RSSParser

CURRENT_VERSION = 'Version 1.0'
logging.basicConfig(level=logging.ERROR, format='[%(asctime)s]-[%(levelname)s]: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


def main():
    args = get_args()
    if args.version:
        print(CURRENT_VERSION)
        exit(0)
    if args.verbose:
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s]-[%(levelname)s]: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')
    rss_parser = RSSParser()
    rss_parser.request_soup(args.source)
    items = rss_parser.items(args.limit)
    rss_parser.parse_items(items)
    if args.json:
        print(rss_parser.json_results())
    else:
        feed = Feed(rss_parser.feed_title, rss_parser.parsed_items)
        print(feed)


if __name__ == '__main__':
    main()
