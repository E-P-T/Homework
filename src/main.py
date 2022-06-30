import json
from datetime import datetime
from xml.etree.ElementTree import ParseError

import info
from Arguments import Arguments
from Logger import Logger, Level
from Util import Util
from news.News import News

args = Arguments(info.fullname, info.version).parse()
Logger.verbose(args.verbose)


def get_news(source: str, limit: int, date: datetime) -> News:
    Logger.log(Level.INFO, 'Downloading and parsing ' + source)
    try:
        element = Util.to_element(source)
    except ValueError:
        Logger.log(Level.ERROR, 'Invalid URL')
    except ParseError:
        Logger.log(Level.ERROR, 'Invalid XML')

    return News.parse_element(element, limit, date)


def print_news(news_to_print: News, to_json: bool, to_colorize: bool) -> None:
    string = Util.to_json(news_to_print) \
        if to_json else str(news_to_print)
    string = '\n' + string
    print(
        Util.colorize_object(string) if to_colorize
        else string
    )


def get_cached_news(cached: str) -> News:
    Logger.log(Level.INFO, 'Getting cached items and parsing')
    if cached:
        news_cached = News.parse_json(json.loads(cached))
    else:
        Logger.log(Level.WARNING, 'Cached items are empty')
        news_cached = News()
        news_cached.feed = 'Cached news'
        news_cached.items = []

    return news_cached


def save_cached_news(news_to_cache: News) -> None:
    Logger.log(Level.INFO, 'Caching news')
    Util.save_cache(Util.to_json(news_to_cache))


def save_to_files(to_save: News, html: str, fb2: str) -> None:
    if html is not None:
        Logger.log(Level.INFO, 'Saving as html')
        Util.save(to_save.to_html(), html)
    if fb2 is not None:
        Logger.log(Level.INFO, 'Saving as fb2')
        Util.save(to_save.to_fb2(), fb2)


cached_news = get_cached_news(Util.get_cached())

to_print: News

if args.source:
    news = get_news(args.source, args.limit, args.date)
    cached_news.items += news.items
    cached_news.items = Util.unique(cached_news.items)
    save_cached_news(cached_news)

    to_print = news
else:
    cached_news.items = News.date_filter(cached_news.items, args.date)[:args.limit]
    to_print = cached_news

save_to_files(to_print, args.to_html, args.to_fb2)
print_news(to_print, args.json, args.colorize)
