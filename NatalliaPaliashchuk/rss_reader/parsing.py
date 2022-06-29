import logging
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from .exceptions import ParserError

logger = logging.getLogger(__name__)


def get_item_desc(item):
    '''Parse description of RSS item'''
    logger.debug('Parsing description of RSS feed')
    url_tags = {'a': {'attr': 'href', 'type': 'link', 'alt_text': ''},
                'img': {'attr': 'src', 'type': 'image', 'alt_text': 'alt'}}
    text, links, link_pos = '', [], 1
    if desc := item.description:
        bs = BeautifulSoup(desc.get_text(strip=True), features='html.parser')
        for tag in bs.find_all():
            if tag.attrs and not tag.find_all():
                url = tag.attrs.get(url_tags.get(tag.name, {}).get('attr', ''))
                if url:
                    links.append({'link_pos': link_pos, 'link_url': url, 'link_type': url_tags.get(tag.name)['type']})
                    alt = tag.text or tag.attrs.get(url_tags.get(tag.name)['alt_text'], '')
                    tag.replace_with(f'[{link_pos} {alt}'.strip() + ']')
                    link_pos += 1
            tag.smooth()
        text = bs.text
    logger.debug('Done')
    return {'desc_text': text, 'desc_links': links}


def get_item_image_url(item, url):
    '''Parse image url of RSS item'''
    logger.debug('Parsing image url of RSS feed')
    image_url = ''
    if media_content := item.find('media:content', attrs={'url': True}):
        if media_content.has_attr('medium'):
            if media_content.get('medium') == 'image':
                image_url = media_content['url']
        else:
            if requests.head(media_content['url']).headers.get('Content-Type')[:5] == 'image':
                image_url = media_content['url']
    else:
        bs_html = BeautifulSoup(requests.get(url).content, features='html.parser')
        if preview_image := bs_html.find('meta', property='og:image', attrs={'content': True}):
            image_url = preview_image.attrs.get('content')
    logger.debug('Done')
    return image_url.strip()


def parse_rss(url, limit=0):
    '''Parse a RSS feed and return a RSS dict'''
    logger.debug(f'Parsing RSS from {url} started')
    try:
        bs_xml = BeautifulSoup(requests.get(url).content, features='xml')
    except Exception as e:
        raise ParserError(f'The {url} can\'t be parsed due to {e}') from None
    if not bs_xml.rss:
        raise ParserError(f'The {url} can\'t be parsed as RSS')
    try:
        feed = {url: {'feed_title': bs_xml.title.text, 'feed_items': []}}
        for item in bs_xml.findAll('item')[:None if limit == 0 else limit]:
            item_dict = {'item_title': getattr(item.title, 'text', '').strip(),
                         'item_pub_date': parse(getattr(item.pubDate, 'text', '0001-01-01')),
                         'item_url': getattr(item.link, 'text', '').strip(),
                         'item_desc_text': get_item_desc(item)['desc_text'].strip(),
                         'item_desc_links': get_item_desc(item)['desc_links']}
            item_dict['item_image_url'] = get_item_image_url(item, item_dict['item_url'])
            feed[url]['feed_items'].append(item_dict)
    except Exception as e:
        raise ParserError(f'The {url} can\'t be parsed as RSS due to {e}') from None
    logger.debug('Done')
    return feed
