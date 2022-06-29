import logging
import logging.config

from rss_reader_pckg.rss import RSSParser
from rss_reader_pckg.args import get_args

CURRENT_VERSION = 'Version 1.2'
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
    # try:
    rss_parser = RSSParser()
    if args.date:
        rss_parser.parse_items_by_date(args.date, args.source, args.limit)
    else:
        rss_parser.request_soup(args.source)
        items = rss_parser.items(args.limit)
        rss_parser.parse_items(items)
    if args.json:
        print(rss_parser.json_results())
    else:
        feed = rss_parser.feed
        print(feed)
    # except Exception as e:
    #     if not (hasattr(e, 'is_logged') and e.is_logged):
    #         print(f'During operation of the program the following error occurred: {e}')


if __name__ == '__main__':
    main()
