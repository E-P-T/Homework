"""
This rss_reader.py is a python script intended to get RSS feed from given source URL
and write its content to standart output.

Please be carefull with redirecting output to files. In this case CPython implementation
of Python interpreter will change encoding from UTF-8 to
the system locale encoding (i.e. the ANSI codepage).

This script will try to install all required packages from PyPI with pip in
the current environment.
"""

import sys
import logging


def install_and_import(module_name, package_name=None):
    """
    This function tries to import module `module_name`.
    In case of failure of that operation the function installs package `package_name`
    """
    from importlib import import_module
    try:
        return import_module(module_name)
    except ImportError:
        from subprocess import run
        if package_name is None:
            package_name = module_name
        run([sys.executable, '-m', 'pip', 'install', package_name])
    try:
        return import_module(module_name)
    except ImportError:
        print(f'Failed to install package {package_name}', file=sys.stderr)


def parse_args(args=None):
    """
    Parse command line arguments from args or if not provided from sys.argv

    Args should not contain name of program.
    """
    import argparse
    parser = argparse.ArgumentParser(
        description='Pure Python command-line RSS reader.',
        exit_on_error=False)
    parser.add_argument('--version', action='version', help='Print version info', version='1.0')
    parser.add_argument('--json', action='store_true', default=False, help='Print result as JSON in stdout')
    parser.add_argument('--verbose', action='store_true', default=False, help='Outputs verbose status messages')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')
    parser.add_argument('source', help='RSS URL')
    return parser.parse_args(args)


def recieve_feed(source):
    """
    Get content of feed by URL
    """
    import requests
    resp = requests.get(source)
    return resp.text


def get_text(element):
    """
    Return text of element or None if no element
    """
    return element.text if element is not None else None


def get_date(element):
    """
    Get value of date that is written inside the element.

    At the moment this function just returns text of element,
    but this behaviour may be changed in later versions.

    If there are no element None will be returned.
    """
    return get_text(element)


def get_link(elem):
    """
    Get information of link element: url and type

    Return tuple with url and kind of resource
    """
    url = elem['url']
    type_ = elem['type'].split('/')[0] if 'type' in elem else 'image'
    return (url, type_)


def parse_item(item):
    """
    Parse item element

    Returns dict with keys title, pubDate, link, description and links.
    For keys title, pubDate and description correspond information is stored.
    For key links dict stores list of tuples:
    first element of the tuple is URL of the link and
    second element of the tuple is type (link or image etc).
    """
    from bs4 import BeautifulSoup
    logging.debug("Getting item information...")
    item_info = {
        'title': get_text(item.title),
        'pubDate': get_date(item.pubDate),
        'link': get_text(item.link)
    }
    links = [(item_info['link'], 'link')]
    logging.debug('Looking for enclosures')
    enclosures = [get_link(enclosure) for enclosure in item('enclosure')]
    prefix = "".join(f'[image {n}]' for n, _ in enumerate(enclosures, start=len(links) + 1))
    links.extend(enclosures)
    logging.debug('Looking for medias')
    medias = [get_link(media) for media in item('media:content')]
    prefix += "".join(f'[image {n}]' for n, _ in enumerate(medias, start=len(links) + 1))
    links.extend(medias)
    if item.description is not None:
        logging.debug('Parsing item description')
        description = BeautifulSoup(item.description.text, 'lxml')
        logging.debug('Replacing image references and links in description')
        for tag in description(['img', 'a']):
            if tag.name == 'img':
                links.append((tag['src'], 'image'))
                num = len(links)
                tag.replace_with(f'[image {num}]')
            else:
                links.append((tag['href'], 'link'))
                num = len(links)
                tag.append(f'[{num}]')
        description = description.text
    else:
        description = ''
    item_info['description'] = prefix + description
    item_info['links'] = links
    return item_info


def parse_feed(content):
    """
    Parse content as channel acording to RSS 2.0
    """
    from bs4 import BeautifulSoup
    try:
        logging.debug('Extracitng channel information...')
        feed = BeautifulSoup(content, 'lxml-xml').rss.channel
        logging.debug('Examining metadata')
        info = {
            'title': feed.find('title', recursive=False).text,
            'link': feed.find('link', recursive=False).text,
            'description': feed.find('description', recursive=False).text,
        }
        logging.debug('Getting items...')
        info['items'] = [parse_item(item) for item in feed('item')]
        return info
    except Exception as e:
        logging.debug(e)
        raise ValueError('Failed to parse feed')


def limit_feed(feed, limit):
    """
    Limit number of items in feed. This function will
    replace feed items list by its slice.
    """
    feed['items'] = feed['items'][:limit]


def format_text(feed):
    """
    Make a text representation of feed
    """
    from io import StringIO
    with StringIO() as fd:
        print('Feed:', feed['title'], file=fd)
        print(file=fd)
        for item in feed['items']:
            print('Title:', item['title'], file=fd)
            print('Date:', item['pubDate'], file=fd)
            print('Link:', item['link'], file=fd)
            print(file=fd)
            print(item['description'], file=fd)
            print('\nLinks:', file=fd)
            for num, (link, kind) in enumerate(item['links'], start=1):
                print(f'[{num}]: {link} ({kind})', file=fd)
        return fd.getvalue()


def format_json(news):
    """
    Represent feed in JSON format
    """
    from json import dumps
    return dumps(news, ensure_ascii=False, indent=1)


def main():
    """
    Preparation and execution organization
    """
    # parse arguments
    args = parse_args()
    # set logging level acording to --verbose flag
    logging.getLogger().setLevel(logging.DEBUG if args.verbose else logging.INFO)
    try:
        # install and import nonstandard modules
        for module_name in 'lxml', 'bs4', 'requests':
            install_and_import(module_name)
        logging.debug(f'Trying to get {args.source}')
        content = recieve_feed(args.source)
        logging.debug('Data received')
        news = parse_feed(content)
        logging.debug('Feed is parsed')
        limit_feed(news, args.limit)
        logging.debug(f'{len(news["items"])} item(s) extracted')
        content = format_json(news) if args.json else format_text(news)
        logging.debug('Content formatted')
        print(content)
    except ValueError as e:
        logging.debug(e)
        logging.critical(e)


if __name__ == '__main__':
    main()
