"""
Main module of rss_reader

It handles parsing arguments, prints version, sets verbose mode, initializes FeedFetcher and fetches feeds
"""
import os
import argparse
from utils import config
from utils.config import print
from utils.version import __version__
from feed_fetcher import FeedFetcher
from cache_worker import CacheWorker
from format_converter import FormatConverter
from date import valid_date
from utils.exceptions import WrongLimitError,\
    ConvertJSONError,\
    WrongUrlError,\
    LinkWithNoSourceError,\
    NotSupportedConversionFormat


my_parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

my_parser.add_argument('source',
                       metavar='source',
                       nargs='?',
                       type=str,
                       help='RSS URL')
my_parser.add_argument("--version",
                       help="Prints version info",
                       action="store_true")
my_parser.add_argument("--date",
                       action="store",
                       type=valid_date,
                       help="Fetches feeds from cache by specified date")
my_parser.add_argument("--limit",
                       action="store",
                       type=int,
                       help="Limits news topics if this parameter is provided")
my_parser.add_argument("--json",
                       action="store_true",
                       help="Prints result as JSON in stdout")
my_parser.add_argument("--to-html",
                       action="store",
                       type=str,
                       help="Converts feeds to html format in specified directory. \
                       If specified directory does not exist, file will be created in application's data directory. \
                       See DOCS for further info")
my_parser.add_argument("--to-epub",
                       action="store",
                       type=str,
                       help="Converts feeds to epub format in specified directory. \
                       If specified directory does not exist, file will be created in application's data directory. \
                       See DOCS for further info")
my_parser.add_argument("--verbose",
                       action="store_true",
                       help="Outputs verbose status messages")
my_parser.add_argument("--colorize",
                       action="store_true",
                       help="Enables colorized output for stdout")

args = my_parser.parse_args()

if args.verbose:
    config.verbose_print = print
if args.colorize:
    config.COLORIZED_MODE = True


def rss_reader_func():
    if args.version:
        print(f"Version {__version__}", "pink")
        return
    convert_dir = args.to_html
    if args.to_html and not os.path.isdir(args.to_html) or args.to_epub and not os.path.isdir(args.to_epub):
        convert_dir = None
    if args.date:
        cached_feeds = CacheWorker.read_feed_from_cache(args.date, args.source, args.limit)
        if args.to_html or args.to_epub:
            if args.to_html:
                FormatConverter.convert_feeds(cached_feeds, "html", convert_dir, args.json)
            if args.to_epub:
                FormatConverter.convert_feeds(cached_feeds, "epub", convert_dir, args.json)
            return
        for feed in cached_feeds:
            if args.json:
                print(feed.to_json())
            else:
                print(feed.to_readable())
        return
    config.verbose_print("Initializing url and limit", "pink")
    try:
        feed_fetcher = FeedFetcher(args.source, args.limit)
        config.verbose_print("Fetching feeds...", "bold")
        feed_fetcher.fetch_feeds()
        if args.to_html or args.to_epub:
            if args.to_html:
                FormatConverter.convert_feeds(feed_fetcher.feeds_formatted, "html", convert_dir, args.json)
            if args.to_epub:
                FormatConverter.convert_feeds(feed_fetcher.feeds_formatted, "epub", convert_dir, args.json)
            return
        for feed in feed_fetcher.feeds_formatted:
            if args.json:
                print(feed.to_json())
            else:
                print(feed.to_readable())
    except WrongLimitError as message:
        print(str(message), "err")
    except WrongUrlError as message:
        print(str(message), "err")
    except ConvertJSONError as message:
        print(str(message), "err")
    except LinkWithNoSourceError as message:
        print(str(message), "err")
    except NotSupportedConversionFormat as message:
        print(str(message), "err")
    except Exception as e:
        print(f"Error ({e})", "err")


if __name__ == "__main__":
    rss_reader_func()
