import json
import os
from pathlib import Path
from urllib.error import URLError
from xml.etree.ElementTree import ParseError

from args.ArgumentParser import ArgumentParser
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


def from_url(logger: Logger, args: ArgumentParser.Arguments, path: os.path) -> News:
    """
    Get news from a URL.
    """
    logger.info(f'Downloading from {args.source}')
    try:
        element = Util.url_to_element(args.source)
    except (URLError, ValueError):
        logger.error('Invalid URL')
        exit(-1)
    except ParseError:
        logger.error('Invalid XML')
        exit(-1)

    logger.info('Parsing XML')
    news = News.parse(element, args.limit, args.date)

    cached = get_cache(path)
    cached.items += news.items

    items = []
    for item in cached.items:
        if item not in items:
            items.append(item)

    cached.items = items

    save_cache(path, cached, logger)

    return news


def from_local(logger: Logger, args: ArgumentParser.Arguments, path: os.path) -> News:
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

    return News('Local cached feed', items)


def to_html(path: str, news: News, logger: Logger) -> str:
    """
    Generate HTML file and save it to specified path.
    """
    logger.info(f'Generating HTML file and saving it to {path}')
    news = news.to_html()

    with open(path, 'w+') as file:
        file.write(news)

    return news


def to_pdf(path: str, news: News, html: str, logger: Logger) -> None:
    """
    Generate PDF file and save it to specified path.
    """
    logger.info(f'Generating PDF file and saving it to {path}')
    if html is None:
        html = news.to_html()
    Util.html_to_pdf(html, path)


def main() -> None:
    """
    Main function of the program.
    """
    args = ArgumentParser(name, version).parse()
    logger = Logger(args.verbose)
    path = os.path.join(Path(__file__).parent.parent, 'news.json')

    if args.source is None:
        news = from_local(logger, args, path)
    else:
        news = from_url(logger, args, path)

    print(
        Util.to_json(news) if args.json
        else Util.to_str(news)
    )

    if args.html is not None:
        html = to_html(args.html, news, logger)
    if args.pdf is not None:
        to_pdf(args.pdf, news, html, logger)


if __name__ == '__main__':
    main()
