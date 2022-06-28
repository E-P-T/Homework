import argparse
import sys

from rss_parse import __version__
from rss_parse.parse.params import Params
from rss_parse.parse.rss_feed import RssFeed
from rss_parse.parse.rss_parser import ParsingException
from rss_parse.parse.rss_parser_factory import get_parser
from rss_parse.processor.rss_processor_factory import get_processor
from rss_parse.utils.message_consumer import get_message_consumer
from rss_parse.utils.printing_utils import print_error


def parse_params_from_arguments():
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    # FIXME: Doesn't work with parse_args([*]). Look at action
    parser.add_argument("source", help="RSS URL", nargs='?' if '--date' in sys.argv else None)
    parser.add_argument("--version", help="Print version info", action="version",
                        version=f"Version {__version__}")
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--verbose", help="Output verbose status messages", action="store_true")
    parser.add_argument("--limit", help="Limit news topics if this parameter provided", type=int, default=-1)
    args = parser.parse_args()

    return Params.from_args(args)


def main():
    """
    Add args, which will be available, when you will work with console.
    """
    params = parse_params_from_arguments()
    mc = get_message_consumer(params.is_verbose)

    mc.add_message("Program started")

    mc.add_message("Initializing parser...")
    parser = get_parser(params.source, mc)
    mc.add_message("Parser initialized")

    rss_feed = None
    try:
        rss_feed = parser.parse()
    except ParsingException as ex:
        mc.add_message("Encountered an error during parsing")
        print_error(str(ex))
        mc.add_message("Exiting the program")
        # FIXME: Map Exceptions to errors or something like this
        exit(2)

    # Fixme: move to preprocessor
    rss_items = sorted(rss_feed.rss_items, key=lambda item: item.publication_date, reverse=True)
    if params.limit > 0:
        mc.add_message("Applying limit option")
        rss_items = rss_items[:params.limit]
    rss_feed = RssFeed(rss_items)

    processor = get_processor(rss_feed, params.is_json, mc)
    processor.process()


# FIXME: REMOVE
import traceback


def main_wrapper():
    try:
        main()
        exit(0)
    except Exception as e:
        # FIXME: REMOVE IN LATEST VERSION
        print(traceback.format_exc())
        print_error("Unknown error, please rerun the application")
        # TODO: logging
        exit(1)


if __name__ == '__main__':
    main_wrapper()
