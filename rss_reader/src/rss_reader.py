import json
import os
from pathlib import Path
from urllib.error import URLError
from xml.etree.ElementTree import ParseError

from args.Arguments import Arguments
from info import name, version
from news.News import News
from util.Logger import Logger
from util.Util import Util


def get_cache(path: os.path) -> News:
    """
    Get the cache from the local file.
    """
    if os.path.exists(path):
        with open(path, 'r') as file:
            return News.parse_dict(json.loads(file.read()))
    else:
        news = News('Local cached feed', [])
        return news


def save_cache(path: os.path, news: News, logger: Logger) -> None:
    """
    Save the cache to the local file.
    """
    logger.info('Saving to cache')
    with open(path, 'w') as file:
        file.write(Util.to_json(news))


def print_news(news: News, args: Arguments) -> None:
    print(
        Util.to_json(news) if args.json
        else Util.to_str(news)
    )


def from_url(logger: Logger, args: Arguments, path: os.path) -> None:
    """
    Get news from a URL.
    """
    logger.info(f'Downloading from {args.source}')
    try:
        element = Util.url_to_element(args.source)
    except (URLError, ValueError):
        logger.error('Invalid URL')
        return
    except ParseError:
        logger.error('Invalid XML')
        return

    logger.info('Parsing XML')
    news = News.parse(element, args.limit, args.date)

    print_news(news, args)

    cached = get_cache(path)
    cached.items += news.items

    items = []
    for item in cached.items:
        if item not in items:
            items.append(item)

    cached.items = items

    save_cache(path, cached, logger)


def from_local(logger: Logger, args: Arguments, path: os.path) -> None:
    """
    Get news from a local cache.
    """
    logger.info('Getting items from local cache: no source specified')
    news = get_cache(path)
    items = []
    for item in news.items:
        if item.date.date() == args.date.date():
            items.append(item)
    items = items[:args.limit]

    print_news(News('Local cached feed', items), args)


def main() -> None:
    """
    Main function of the program.
    """
    args = Arguments(name, version)
    logger = Logger(args.verbose)
    path = os.path.join(Path(__file__).parent.parent, 'news.json')

    if args.source is None:
        from_local(logger, args, path)
    else:
        from_url(logger, args, path)


if __name__ == '__main__':
    main()
