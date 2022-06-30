"""RSS_reader exception classes"""


class URLError(Exception):
    """No such URL exist"""
    pass


class NotRssFormat(Exception):
    """URL doesn't match the RSS format"""
    pass


class MissingHTTP(Exception):
    """In URL Missing https"""
    pass


class CacheNotFound(Exception):
    """Could not find articles for the specified url or date"""
    pass


class NoImgFound(Exception):
    """News doesn't contain images."""
    pass


class PATHError(Exception):
    """Setted PATH is invalid"""
    pass
