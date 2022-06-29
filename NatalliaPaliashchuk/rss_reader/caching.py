import pickle
import logging
from .exceptions import CachingError

logger = logging.getLogger(__name__)


def cache_feed(feed):
    '''Serialization feed into a pickle file'''
    logger.debug('Feed serialization started')
    try:
        with open('cache.pk1', 'wb') as f:
            pickle.dump(feed, f)
    except Exception as e:
        logger.debug(f'Cashing can\'t be done due to {e}')
        raise CachingError(e) from None
    logger.debug('Done')


def get_feed_by_date(date, url, limit):
    '''Get feed by date from cache'''
    logger.debug(f'Getting feed by {date} started')
    try:
        with open('cache.pk1', 'rb') as f:
            feed = pickle.load(f)
    except Exception as e:
        logger.debug(f'Getting from cache can\'t be done due to {e}')
        raise CachingError(e) from None
    if url not in feed:
        logger.debug(f'{url} not found in cache')
        return None
    logger.debug('Done')
    if limit == 0:
        return {url: {'feed_title': feed[url]['feed_title'],
                'feed_items': [item for item in feed[url]['feed_items'] if item['item_pub_date'] >= date]}}    
    else:
        return {url: {'feed_title': feed[url]['feed_title'],
                'feed_items': [item for item in feed[url]['feed_items'] if item['item_pub_date'] >= date][:limit]}}
