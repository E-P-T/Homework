import os
import json
import logging
import html2epub
from jinja2 import Template
from .exceptions import ConvertError

logger = logging.getLogger(__name__)


def feed_to_html(feed):
    '''Convert feed to html'''
    here = os.path.abspath(os.path.dirname(__file__))
    logger.debug('Creating html')
    try:
        with open(os.path.join(here, 'templates', 'to_.html')) as f:
            html = Template(f.read()).render(feed)
    except Exception as e:
        logger.debug(f'Creating html can\'t be done due to {e}')
        raise ConvertError(e) from None
    logger.debug('Done')
    return html


def feed_to_json(feed, indent=None):
    '''Convert feed to json'''
    logger.debug('Creating json')
    json_ = json.dumps(feed, ensure_ascii=False, indent=indent, default=str)
    logger.debug('Done')
    return json_


def feed_to_epub(feed, path):
    '''Convert feed to epub'''
    logger.debug('Creating epub')
    epub = html2epub.Epub(feed['feed_title'])
    chapter = html2epub.create_chapter_from_string(feed_to_html(feed))
    epub.add_chapter(chapter)
    epub.create_epub(path)
    logger.debug('Done')
