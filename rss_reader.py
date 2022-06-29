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
import json
from functools import cached_property


def install_and_import(module_name, package_name=None):
    """
    This function tries to import module `module_name`.
    In case of failure of that operation the function installs package `package_name`
    """
    from importlib import import_module
    try:
        logging.debug(f'Trying to import module {module_name}')
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


def install_modules():
    """
    Try to import nonstandard modules and install them in case of failure
    """
    for module_name in 'lxml', 'bs4', 'requests':
        install_and_import(module_name)
    for module_name, package_name in ('dateutil', 'python-dateutil'), ('fpdf', 'fpdf2'):
        install_and_import(module_name, package_name)


def parse_args(args=None):
    """
    Parse command line arguments from args or if not provided from sys.argv

    Args should not contain name of program.
    """
    import argparse
    from datetime import datetime
    parser = argparse.ArgumentParser(
        description='Pure Python command-line RSS reader.',
        exit_on_error=False)
    parser.add_argument('--version', action='version', help='Print version info', version='4.0')
    parser.add_argument('--json', action='store_true', default=False, help='Print result as JSON in stdout')
    parser.add_argument('--verbose', action='store_true', default=False, help='Outputs verbose status messages')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')
    parser.add_argument('--date', type=lambda s: datetime.strptime(s, '%Y%m%d').astimezone(),
                        help='Get from cache news that was published after specified date\n'
                        '(date should be specified in format YYYYmmdd, for example --date 20191020)')
    parser.add_argument('--to-html', dest='html_dest', help='Store feed in HTML as specified file')
    parser.add_argument('--to-pdf', dest='pdf_dest', help='Store feed in PDF as specified file')
    parser.add_argument('source', help='RSS URL')
    parsed_args = parser.parse_args(args)
    return parsed_args


def request_feed(source):
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
    return element.text if element is not None else ''


def get_date(element):
    """
    Create datetime object from text of element. If element is None then datetime.min is returned
    """
    from dateutil import parser
    from datetime import datetime
    return parser.parse(element.text) if element is not None else datetime.min


def get_link(elem):
    """
    Get information of link element: url and type

    Return tuple with url and kind of resource
    """
    url = elem['url']
    type_ = elem['type'].split('/')[0] if 'type' in elem.attrs else 'image'
    return (url, type_)


def recieve_image(src):
    """
    Get content of resource. Intended to store images in cache.
    Returns bytes object with content downloaded from specified URL.
    """
    from requests import get
    from shutil import copyfileobj
    from io import BytesIO

    r = get(src, stream=True)
    with BytesIO() as f:
        r.raw.decode_content = True
        copyfileobj(r.raw, f)
        return f.getvalue()


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
    item_info['images'] = {url: recieve_image(url) for url, t in enclosures if t == 'image'}
    logging.debug('Looking for medias')
    medias = [get_link(media) for media in item('media:content')]
    prefix += "".join(f'[image {n}]' for n, _ in enumerate(medias, start=len(links) + 1))
    links.extend(medias)
    item_info['images'].update({url: recieve_image(url) for url, t in medias if t == 'image'})
    if item.description is not None:
        logging.debug('Parsing item description')
        item_info['description_raw'] = item.description.text
        description = BeautifulSoup(item.description.text, 'lxml')
        logging.debug('Replacing image references and links in description')
        for tag in description(['img', 'a']):
            if tag.name == 'img':
                links.append((tag['src'], 'image'))
                num = len(links)
                tag.replace_with(f'[image {num}]')
                item_info['images'][tag['src']] = recieve_image(tag['src'])
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
    from operator import itemgetter
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
        info['items'] = sorted([parse_item(item) for item in feed('item')],
                               key=itemgetter('pubDate', 'title', 'description'), reverse=True)
        return info
    except Exception:
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
        for item in feed['items']:
            print(file=fd)
            print('Title:', item['title'], file=fd)
            print('Date:', item['pubDate'].strftime('%a, %d %b %Y %H:%M:%S %z'), file=fd)
            print('Link:', item['link'], file=fd)
            print(file=fd)
            print(item['description'], file=fd)
            print('\nLinks:', file=fd)
            for num, (link, kind) in enumerate(item['links'], start=1):
                print(f'[{num}]: {link} ({kind})', file=fd)
        return fd.getvalue()


class DateTimeEncoder(json.JSONEncoder):

    """
    The DateTimeEncoder class provides marshalling of type datatime.datetime for JSON encoding with module json.
    """

    def __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True,
                 allow_nan=True, sort_keys=False, indent=None,
                 separators=None, default=None):
        """
        The constructor just call parents constructor with the same parameters
        """
        super().__init__(skipkeys=skipkeys, ensure_ascii=ensure_ascii,
                         check_circular=check_circular, allow_nan=allow_nan,
                         sort_keys=sort_keys, indent=indent,
                         separators=separators, default=default)

    def default(self, obj):
        """
        Objects of type datatime.datetime will be converted to JSON as
        string of format strftime('%a, %d %b %Y %H:%M:%S %z'). All other objects will be
        converted in usual way.
        """
        from datetime import datetime
        if type(obj) == datetime:
            return obj.strftime('%a, %d %b %Y %H:%M:%S %z')
        else:
            return super().default(obj)


def format_json(news):
    """
    Represent feed in JSON format
    """
    from json import dumps
    from copy import deepcopy
    noimg = deepcopy(news)
    for item in noimg['items']:
        del item['images']
        item['description'] = item['description_raw']
        del item['description_raw']
    return dumps(noimg, ensure_ascii=False, indent=1, cls=DateTimeEncoder)


def load_cache():
    """
    Loading all items from local cache

    Cache is represented as dictionary:
    - keys are of sources
    - values are news collections for the source with of items sorted ascending by pubDate
    """
    from pickle import load
    try:
        with open('rss_reader.cache', 'rb') as f:
            return load(f)
    except (FileNotFoundError, EOFError):
        # Cache is empty
        return {}


def save_cache(cache):
    """
    Save cache in locate storage
    """
    from pickle import dump
    with open('rss_reader.cache', 'wb') as f:
        dump(cache, f)


def merge_items(alist, blist):
    """
    Merge two lists of feed items. Eleminate duplicates. Items from blist has greater prececdnce
    """
    from operator import itemgetter
    key_getter = itemgetter('pubDate', 'title', 'link', 'description')
    adict = {key_getter(a): a for a in alist}
    bdict = {key_getter(b): b for b in blist}
    adict.update(bdict)
    return sorted(adict.values(), key=itemgetter('pubDate'), reverse=True)


def update_cache(cache, source, feed):
    """
    Update cache with parsed feed
    """
    from copy import deepcopy, copy
    if source in cache:
        items = merge_items(cache[source]['items'], feed['items'])
    else:
        items = copy(feed['items'])
    cache[source] = deepcopy(feed)
    cache[source]['items'] = items


def lookup_cache(cache, source, date):
    """
    Looking for feed items in cache
    """
    from itertools import takewhile
    logging.debug(f'Looking for news not before {date=}')
    assert source in cache, f'No news in cache for {source=}'
    news = cache[source]
    news['items'] = list(takewhile(
        lambda item: item['pubDate'] >= date,
        news['items']))
    return news


def receive_feed(source, cache):
    """
    Request feed content from specified source
    """
    logging.debug(f'Trying to get {source}')
    content = request_feed(source)
    logging.debug('Data is received')
    news = parse_feed(content)
    logging.debug('Feed is parsed')
    try:
        update_cache(cache, source, news)
        logging.debug('Cache update')
        save_cache(cache)
        logging.debug('Cache stored')
    except Exception as e:
        logging.debug(e)
        print('WARNING: Cache is disabled. No new items were stored.')
    return news


def _download_font():
    """
    Download archive with fonts for FPDF and extract DejaVuSansCondensed.ttf

    If the file DejaVuSansCondensed.ttf is found in current directory
    then no operation is performed
    """
    from os.path import exists
    from requests import get
    from io import BytesIO
    from zipfile import ZipFile
    from shutil import copyfileobj
    if exists('DejaVuSansCondensed.ttf'):
        return
    try:
        r = get('https://github.com/reingart/pyfpdf/releases/download/binary/fpdf_unicode_font_pack.zip', stream=True)
        with BytesIO(r.content) as b, ZipFile(b) as z, z.open('font/DejaVuSansCondensed.ttf') as f:
            with open('DejaVuSansCondensed.ttf', 'wb') as d:
                copyfileobj(f, d)
    except Exception as e:
        raise IOError(f'Can not get font: {e}')


class Formatters:

    """
    Set of interdependant formatters. One formatter may require result of other formatter
    """

    def __init__(self, feed):
        """
        Initialize formatter. Feed is parsed representation of feed being formatted
        """
        self.feed = feed
        self.images = {url: image for item in self.feed['items'] for url, image in item['images'].items()}

    def _get_cached_image(self, url):
        """
        Get image from feed as BytesIO
        """
        from io import BytesIO
        return BytesIO(self.images[url])

    @cached_property
    def to_html(self):
        """
        Represent feed as HTML document
        """
        from bs4 import BeautifulSoup as bsoup
        html = bsoup('<!DOCTYPE html><html></html>', 'html.parser')
        new_tag = html.new_tag
        head = new_tag('head')
        html('html')[0].append(head)
        head.append(new_tag('meta', charset='utf-8'))
        title = new_tag('title')
        title.append(self.feed['title'])
        head.append(title)
        body = new_tag('body')
        html('html')[0].append(body)
        tag = new_tag('h1')
        body.append(tag)
        tag.append(self.feed['title'])
        tag = new_tag('div')
        body.append(tag)
        tag.append(self.feed['description'])
        for item in self.feed['items']:
            art_title = new_tag('h2')
            body.append(art_title)
            art_title.append(item['title'])
            art_time = new_tag('p')
            body.append(art_time)
            art_time.append(item['pubDate'].strftime('%a, %d %b %Y %H:%M:%S %z'))
            if 'description_raw' in item:
                description = new_tag('div')
                body.append(description)
                descr_content = bsoup(item['description_raw'], 'lxml')
                for img_tag in descr_content('img'):
                    if 'width' not in img_tag.attrs or 'height' not in img_tag.attrs:
                        img_tag['width'] = 160
                        img_tag['height'] = 100
                try:
                    inner = descr_content.html.body.p.text
                except Exception:
                    inner = None
                if inner == item['description_raw']:
                    description.append(inner)
                else:
                    description.append(descr_content)
            link_list = new_tag('ol')
            body.append(link_list)
            for link, mt in item['links']:
                links_item = new_tag('li')
                link_list.append(links_item)
                if mt == 'image':
                    link_tag = new_tag('img', src=link, width=160, height=100)
                    links_item.append(link_tag)
                else:
                    link_tag = new_tag('a', href=link)
                    links_item.append(link_tag)
                    link_tag.append(mt)
        return str(html).encode('utf-8')

    @cached_property
    def to_pdf(self):
        """
        Represent feed as PDF document.

        Use weasyprint to convert from HTML representation
        """

        from fpdf import FPDF, HTMLMixin

        class PDF(FPDF, HTMLMixin):
            pass

        html_str = self.to_html.decode('utf-8')
        pdf = PDF()
        pdf.set_title(self.feed['title'])
        pdf.add_page()
        _download_font()
        pdf.add_font('DejaVu', fname='DejaVuSansCondensed.ttf')
        pdf.set_font('DejaVu', size=14)
        pdf.write_html(html_str, image_map=self._get_cached_image)
        return pdf.output()


def main():
    """
    Preparation and execution organization
    """
    try:
        # parse arguments
        args = parse_args()
        # install required modules
        install_modules()
        # set logging level acording to --verbose flag
        logging.basicConfig(
            level=logging.DEBUG if args.verbose else logging.INFO
        )
        cache = load_cache()
        logging.debug('Cache loaded')
        if args.date is None:
            news = receive_feed(args.source, cache)
        else:
            news = lookup_cache(cache, args.source, args.date)
        assert news is not None, 'No news found'
        limit_feed(news, args.limit)
        logging.debug(f'{len(news["items"])} item(s) extracted')
        text_required = args.html_dest is None and args.pdf_dest is None and not args.json
        formatter = Formatters(news)
        if args.html_dest:
            try:
                with open(args.html_dest, 'wb') as f:
                    html = formatter.to_html
                    f.write(html)
            except Exception as e:
                print(f'Faild to write html file: {e}')
        if args.pdf_dest:
            try:
                with open(args.pdf_dest, 'wb') as f:
                    pdf = formatter.to_pdf
                    f.write(pdf)
            except Exception as e:
                print(f'Failed to write pdf file: {e}')
        if args.json:
            content = format_json
            sys.stdout.write(content)
        if text_required:
            content = format_text(news)
            logging.debug('Content formatted')
            sys.stdout.write(content)
    except AssertionError as failed:
        print(failed)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
