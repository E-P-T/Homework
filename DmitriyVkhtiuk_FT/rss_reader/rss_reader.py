from modified_argparser import ArgParser
from news_brain import NewsBrain

parser = ArgParser(description="Pure Python command-line RSS reader.", add_help=True)
parser.add_argument("source", type=str, help="RSS URL", nargs="?", default=None)
parser.add_argument("--limit",
                    help="Limit news topics if this parameter provided. (MUST expect one argument)",
                    default=None, type=int)
parser.add_argument("--json", help="print result as JSON in stdout. ", action="store_true")
parser.add_argument("--verbose", help="Outputs verbose status messages", action='store_true')
parser.add_argument("--version", help="Print version info", action='version', version=f'Version {1.3}')
parser.add_argument("--date",
                    help="Fetch news from local cache by date", default=None, type=str, )


def main():
    args = parser.parse_args()
    news = NewsBrain(args.source, args.limit, args.json, args.date)
    lim = args.limit
    if args.verbose:
        news.create_logger()
    if args.date is None:
        xml = news.get_rss_data()

        if xml is not None:
            if lim is None or lim > len(xml.find_all("item")):
                news.get_news(xml)
            else:
                news.get_news(xml, lim)

    else:
        news.print_from_cache(lim)


if __name__ == "__main__":
    main()
