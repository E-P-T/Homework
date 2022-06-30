import argparse
import sys

from rss_parse import __version__
from rss_parse.exceptions.exceptions import ProcessingException
from rss_parse.parse.params import Params
from rss_parse.parse.rss_parser import ParsingException
from rss_parse.parse.rss_parser_factory import get_parser
from rss_parse.preprocessor.rss_preprocessor_factory import get_preprocessors
from rss_parse.processor.rss_html_converter import RssToHtmlConverter
from rss_parse.processor.rss_pdf_converter import RssToPdfConverter
from rss_parse.processor.rss_processor_factory import get_processors
from rss_parse.utils.arg_parse_types import date_YYYYMMDD, dir_path
from rss_parse.utils.messaging_utils import get_message_consumer
from rss_parse.utils.messaging_utils import print_error


def parse_params_from_arguments():
    parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    parser.add_argument("source", help="RSS URL", nargs='?' if '--date' in sys.argv else None)
    parser.add_argument("--version", help="Print version info", action="version",
                        version=f"Version {__version__}")
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--verbose", help="Output verbose status messages", action="store_true")
    parser.add_argument("--limit", help="Limit news topics if this parameter provided", type=int, default=-1)
    parser.add_argument("--date", help="Limit the feed by publication date - format YYYYMMDD", type=date_YYYYMMDD)
    parser.add_argument("--to-html",
                        help=f"Directory to store generated html file. "
                             f"File name will be {RssToHtmlConverter.HTML_FILE_NAME}",
                        type=dir_path)
    parser.add_argument("--to-pdf",
                        help=f"Directory to store generated pdf file. "
                             f"File name will be {RssToPdfConverter.PDF_FILE_NAME}",
                        type=dir_path)
    args = parser.parse_args()

    return Params.from_args(args)


def main():
    # Parse arguments from console
    params = parse_params_from_arguments()
    mc = get_message_consumer(params.is_verbose)

    mc.add_message("Program started")

    mc.add_message("Initializing parser...")
    parser = get_parser(params, mc)
    mc.add_message("Parser initialized")

    rss_feed = None
    try:
        # parse RSS from different sources (cache, URL, XML file, etc.)
        rss_feed = parser.parse()
    except ParsingException as ex:
        mc.add_message("Encountered an error during parsing")
        print_error(str(ex))
        mc.add_message("Exiting the program")
        exit(2)

    # modify original feed based on some needs (sorting, limit, etc)
    preprocessors = get_preprocessors(params, mc)
    for preprocessor in preprocessors:
        rss_feed = preprocessor.preprocess(rss_feed)

    # do something with the feed (print, convert, save as file)
    try:
        processors = get_processors(rss_feed, params, mc)
        for processor in processors:
            processor.process()
    except ProcessingException as ex:
        print_error(str(ex))


def main_wrapper():
    try:
        main()
        exit(0)
    except Exception:
        print_error("Unknown error, please rerun the application")
        exit(1)


if __name__ == '__main__':
    main_wrapper()
