import argparse
import logging
import sys
from . import *
from datetime import datetime, timezone
from .caching import cache_feed, get_feed_by_date
from .parsing import parse_rss
from .exceptions import NotFoundError, LimitError
from .converting import feed_to_json, feed_to_epub, feed_to_html

logger = logging.getLogger(__name__)


def run():
    '''The main function of the application

    Raises:
        LimitError: if the limit option was defined under zero
        NotFoundError: if the URL feed is not in the cache
    '''
    sys.tracebacklimit = -1
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader', prog='rss_reader')
    parser.add_argument('source', help='RSS URL')
    parser.add_argument('--version', action='version', help='Print version info', version=f'Version {__version__}')
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--to-html', help='Convert RSS feed into html and save as a file to the path', metavar='FILE')
    parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
    parser.add_argument(
        '--to-epub', help='Convert RSS feed into epub and save as a file in the directory', metavar='DIRECTORY')
    parser.add_argument('--limit', type=int, default=0, help='Limit news topics if this parameter provided')
    parser.add_argument('--date', help='Extract news from archive. Take a start publish date in format YYYYMMDD')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG, format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s', stream=sys.stdout)
    
    if args.limit == 0:
        logger.debug('Limit of items was not specified. All items will be displayed.')
    elif args.limit > 0:
        logger.debug(f'{args.limit} items will be displayed.')
    else:
        raise LimitError('Limit of items must be greater than 1')

    if args.date:
        feed = get_feed_by_date(datetime.strptime(args.date, '%Y%m%d').replace(
            tzinfo=timezone.utc), args.source, args.limit)
        if not feed:
            raise NotFoundError('News not found')
    else:
        feed = parse_rss(args.source, args.limit)
        cache_feed(feed)

    if args.json:
        print(feed_to_json(feed[args.source], indent=2))
    else:
        print(f'Feed: {feed[args.source]["feed_title"]}\n')
        for item in feed[args.source]['feed_items']:
            print(f'Title: {item["item_title"]}\nDate: {item["item_pub_date"]}\nLink: {item["item_url"]}\
                \n\n{item["item_desc_text"]}\n')
            if item['item_desc_links']:
                print('Links:')
                for link in item['item_desc_links']:
                    print(f'[{link["link_pos"]}]: {link["link_url"]} {link["link_type"]}')
            print('\n')

    if args.to_html:
        with open(args.to_html, 'w', encoding='UTF-8') as f:
            f.write(feed_to_html(feed[args.source]))

    if args.to_epub:
        feed_to_epub(feed[args.source], args.to_epub)
