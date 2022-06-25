import argparse
import logging
from src import work_xml



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
    arg_parser = argparse.ArgumentParser(description="Pure Python command-line src reader.")
    arg_parser.add_argument("source", nargs='?', default='', type=str, help="src reader URL")
    arg_parser.add_argument("--version", action="store_true", help="Print version info")
    arg_parser.add_argument("--json", action="store_true", help=" Print result as JSON in stdout")
    arg_parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    arg_parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    arg_parser.add_argument("--date", type=int, help="Outputs news from cash by date")
    arg_parser.add_argument("--html", action="store_true", help=" Print result as HTML in stdout")
    arg_parser.add_argument("--pdf", action="store_true", help=" Print result as PDF in stdout")

    args = arg_parser.parse_args()

    version = "Version 1.4"

    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(filename='app.log', level=logging.INFO)

    try:
        if args.version:
            print(version)
        elif args.source == '':
            if args.date:
                xml_items = work_xml.get_cache_news(args.date)
            else:
                print("URL is are required")
        elif args.date:
            xml_items = work_xml.get_cache_news(args.date, args.source)
        else:
            xml_items = work_xml.take_xml_items(args.source, args.limit)
            work_xml.set_cache_news(args.source, xml_items["items"])


        if xml_items == False:
            return False

        if args.json:
            work_xml.generate_json(xml_items)
        elif args.html:
            work_xml.generate_html(xml_items)
        elif args.pdf:
            work_xml.generate_pdf(xml_items)
        else:
            work_xml.print_to_console(xml_items)
    except AttributeError:
        print("Error, failed to get an attribute. Check correctness URL")


if __name__ == "__main__":
    main()
