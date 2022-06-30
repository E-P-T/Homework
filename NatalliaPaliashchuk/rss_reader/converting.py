import os
import json
import logging
import html2epub
from jinja2 import Template
from .exceptions import ConvertError

logger = logging.getLogger(__name__)


def feed_to_html(feed):
    '''Convert RSS feed to html

    Args:
        feed (dict): RSS feed

    Raises:
        ConvertError: if an error is detected during converting

    Returns:
        str: string that contains html document
    '''    
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
    '''Convert RSS feed to json

    Args:
        feed (dict): RSS feed
        indent (int, optional): indent level. Defaults to None
        
    Raises:
        ConvertError: if an error is detected during converting
        
    Returns:
        str: string that contains JSON document
    '''
    logger.debug('Creating json')
    try:
        json_ = json.dumps(feed, ensure_ascii=False, indent=indent, default=str)
    except Exception as e:
        logger.debug(f'Creating JSON can\'t be done due to {e}')
        raise ConvertError(e) from None
    logger.debug('Done')
    return json_


def feed_to_epub(feed, path):
    '''Convert feed to epub

    Args:
        feed (dict): RSS feed
        path (str): path of directory

    Raises:
        ConvertError: if an error is detected during converting
    '''
    logger.debug(f'Creating epub in {path} directory')
    try:
        epub = html2epub.Epub(feed['feed_title'])
        chapter = html2epub.create_chapter_from_string(feed_to_html(feed))
        epub.add_chapter(chapter)
        epub.create_epub(path)
    except Exception as e:
        logger.debug(f'Creating epub can\'t be done due to {e}')
        raise ConvertError(e) from None    
    logger.debug('Done')
