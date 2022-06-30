"""Accepts arguments from the command line and prints news according to the given arguments."""
import sys

from datetime import datetime
from reader.add_args import args
from reader.exceptions import URLError, CacheNotFound
from reader.cache import Cache
from reader.convert import Convert
from reader.convert_from_cache import ConvertCache
from reader.utils import dump_news_to_json, verification

VERSION = 1.5


class RSSReader:
    @staticmethod
    def show_news_from_cache():
        """Prints news in normal or in json format from cache"""
        try:
            all_news = Cache().read_from_cache(url=args.source, limit=args.limit, date=args.date)
        except CacheNotFound:
            print(CacheNotFound.__doc__)
            sys.exit()
        if args.to_pdf or args.to_html:
            ConvertCache().converter(to_html=args.to_html, to_pdf=args.to_pdf, news_item=all_news)
        number = 1
        for news in all_news:
            if args.verbose:
                print(f'{number} news is displayed')
            if args.json:
                dump_news_to_json(news[0])
            else:
                news[0].print_news()
                print(news[1])
            number += 1

    @staticmethod
    def show_news_from_source():
        """Prints news in normal or in json format"""
        try:
            reader = verification()
        except URLError:
            print(URLError.__doc__)
            sys.exit()
        if args.verbose:
            print(str(datetime.now()) + " News are parsed successfully.")
        all_news = reader.get_channel_news(args.limit)
        if args.to_pdf or args.to_html:
            Convert().converter(to_html=args.to_html, to_pdf=args.to_pdf, news_item=all_news)
        number = 1
        for news in all_news:
            if args.verbose:
                print(f'{number} news is displayed')
            Cache().save_in_cache(news, args.source)
            if args.json:
                dump_news_to_json(news)
            else:
                news.print_news()
                print(news.get_news())
            number += 1


def main():
    rss_reader = RSSReader()
    if args.version:
        print(VERSION)
    elif not (args.date or args.source):
        print('url or date required')
    elif args.date:
        if args.verbose:
            print("Getting results from cache.")
        rss_reader.show_news_from_cache()
    else:
        rss_reader.show_news_from_source()


if __name__ == '__main__':
    main()
