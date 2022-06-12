import argparse
import logging
import rss_reader


# link = "https://news.yahoo.com/rss"
# link = 'https://news.google.com/rss/'
# link = 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml'
# link = 'https://www.cnbc.com/id/100727362/device/rss/rss.html'
# link = 'https://www.cbsnews.com/latest/rss/world'
# link = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
# link = 'https://auto.onliner.by/feed'
# link = 'http://feeds.bbci.co.uk/news/world/rss.xml'
# link = 'https://www.buzzfeed.com/world.xml'
# link = 'https://feeds.bbci.co.uk/news/world/rss.xml'
# link = 'https://vse.sale/news/rss'

def main():
    arg_parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
    arg_parser.add_argument("source", nargs='?', default='', type=str, help="RSS URL")
    arg_parser.add_argument("--version", action="store_true", help="Print version info")
    arg_parser.add_argument("--json", action="store_true", help=" Print result as JSON in stdout")
    arg_parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    arg_parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")

    args = arg_parser.parse_args()

    version = "Version 1.1"

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    try:
        if args.version:
            print(version)
        elif args.source == '':
            print("URL is are required")
        else:

            rss_reader.print_to_console(args.source, args.limit)
    except AttributeError:
        print("Error, failed to get an attribute. Check correctness URL")


if __name__ == "__main__":
    main()

