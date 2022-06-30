from modified_argparser import ArgParser
import logging as log
from news_brain import NewsBrain

parser = ArgParser()

parser.add_argument("source", type=str, help="RSS URL")
parser.add_argument("--limit",
                    help="Limit news topics if this parameter provided. (MUST expect one argument)",
                    default=None)
parser.add_argument("--json", help="print result as JSON in stdout. ", action="store_true")
parser.add_argument("--verbose", help="Outputs verbose status messages", action='store_true')
parser.add_argument("--version", help="Print version info", action='version', version=f'Version 1.2')


def main():
    args = parser.parse_args()

    news = NewsBrain(args.source, args.limit, args.json)
    if args.verbose:
        news.create_logger()

    xml = news.get_rss_data()

    lim = news.check_value_of_limit()
    if xml is not None:
        if lim is None or lim > len(xml.find_all("item")):
            news.get_news(xml)
        else:
            news.get_news(xml, lim)
            log.info("END")


if __name__ == "__main__":
    main()
