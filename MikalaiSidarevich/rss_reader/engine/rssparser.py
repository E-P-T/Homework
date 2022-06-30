"""
RssParser - parser for RSS data.
"""

import threading
import xml.dom.minidom
from html import unescape
from time import sleep

import requests
from bs4 import BeautifulSoup


class RequestError(Exception):
    """
    Request URL exception.
    """
    pass


class XmlParseError(Exception):
    """
    Parse XML document exception.
    """
    pass


class HtmlParseError(Exception):
    """
    Parse HTML document exception.
    """
    pass


class RssParser:
    """Parser for RSS data."""

    def __init__(self, verbose=False):
        """
        Initialize parser with `verbose` ability and setup feed storage.
        """
        self._verbose = verbose
        self._feed = {}

    def feed(self, url, limit):
        """
        Get parsed RSS feed.
        """
        self._url = url
        self._limit = limit

        # Get XML document
        self._document = self._request_url(url).strip()

        # Parse XML document into the internal storage
        self._parse_feed()

        return self._feed

    def _request_url(self, url):
        """
        Get content by the `url`.
        """
        headers = {'User-Agent': 'Mozilla/5.0'}
        timeout = 10

        try:
            response = requests.get(url, headers=headers, timeout=timeout)
        except Exception:
            raise RequestError(f"Unable to get content by URL '{url}'")

        return response.content

    def _parse_feed(self):
        """
        Parse XML document into the internal storage.
        """
        # Get XML DOM structure
        try:
            dom = xml.dom.minidom.parseString(self._document)
        except Exception:
            raise XmlParseError(f"Invalid XML document by URL '{self._url}'")

        # Get feed channel title
        try:
            title_dom = dom.getElementsByTagName('title').item(0)
            if title_dom.firstChild:
                title = title_dom.firstChild.nodeValue
            else:
                title = self._url
        except Exception:
            raise XmlParseError(f"RSS channel '{self._url}' has no title")

        self._feed['channel'] = unescape(title)

        # Add channel url
        self._feed['url'] = self._url

        # Get list of RSS entries
        for tag in ['item', 'entry']:
            item_list = dom.getElementsByTagName(tag)
            if item_list:
                break

        self._feed['entries'] = []

        # Items limit depends on user limit-parameter provided
        if self._limit is None:
            limit = item_list.length
        else:
            limit = min(self._limit, item_list.length)

        # Get RSS entries data
        for i in range(limit):
            item = item_list[i]
            thread = threading.Thread(target=self._get_entry,
                                      args=(i, item))
            thread.start()

            # Prevent too fast requests
            sleep(0.2)

        # Join spawned threads
        for thread in threading.enumerate():
            # Main thread should be skipped
            if thread is threading.main_thread():
                continue
            thread.join()

        if self._verbose:
            print(f"Total {len(self._feed['entries'])} items processed", flush=True)

    def _get_entry(self, n, item):
        """
        Request `n`-th entry attributes:
        get title, date, link from XML, description, image by entry's url.
        """
        if self._verbose:
            print(f"Entry #{n} requested", flush=True)

        entry = {'title': None,
                 'date': None,
                 'link': None,
                 'description': None,
                 'image_link': None}

        # Get entry title
        try:
            entry_title_dom = item.getElementsByTagName('title').item(0)

            # Search non-empty node
            for node in entry_title_dom.childNodes:
                if node.nodeValue.strip():
                    entry['title'] = unescape(node.nodeValue)
                    break
        except Exception:
            if self._verbose:
                print(f"Entry #{n} has no title", flush=True)
            # Title must be present
            return

        # Get entry link
        try:
            for tag in ['link', 'id']:
                entry_link_dom = item.getElementsByTagName(tag).item(0)
                if entry_link_dom.firstChild:
                    entry['link'] = entry_link_dom.firstChild.nodeValue
                    entry['link'] = entry['link'].lower()
                    break
        except Exception:
            if self._verbose:
                print(f"Entry #{n} has no link", flush=True)
            # Link must be present
            return

        # Get entry published date
        try:
            for tag in ['pubDate', 'published']:
                entry_date_dom = item.getElementsByTagName(tag).item(0)
                if entry_date_dom:
                    entry['date'] = entry_date_dom.firstChild.nodeValue
                    break
        except Exception:
            if self._verbose:
                print(f"Entry #{n} has no date published", flush=True)

        # Get entry description
        try:
            attrs = {'name': 'description',
                     'property': 'og:description',
                     'itemprop': 'description'}
            entry['description'] = self._get_meta_tag(entry['link'], **attrs)
            entry['description'] = unescape(entry['description']).strip()
        except Exception as e:
            if self._verbose:
                print(f"Entry #{n} description: {e}", flush=True)

        # Get entry image link
        try:
            attrs = {'property': 'og:image'}
            entry['image_link'] = self._get_meta_tag(entry['link'], **attrs)
        except Exception as e:
            if self._verbose:
                print(f"Entry #{n} image: {e}", flush=True)

        # Add current entry
        self._feed['entries'].append(entry)

        if self._verbose:
            print(f"Entry #{n} received", flush=True)

    def _get_meta_tag(self, url, **kwargs):
        """
        Extract meta tags content from `url` specified.
        Meta tag attributes specified by `kwargs`.
        """
        raw_html = self._request_url(url)
        parsed_html = BeautifulSoup(raw_html.decode('utf-8', 'ignore'), features='html.parser')

        try:
            for attr, value in kwargs.items():
                meta = parsed_html.find('meta', {attr: value})
                if meta:
                    return meta['content']
            else:
                raise Exception
        except Exception:
            raise HtmlParseError(f"Couldn't parse data by URL '{url}'")
