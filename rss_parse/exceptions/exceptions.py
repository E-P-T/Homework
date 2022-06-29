class ParsingException(Exception):
    """
    An exception that could happen during RSS parsing
    """
    pass


class CacheException(Exception):
    """
    An exception that could happen during caching of RSS feed
    """
    pass


class ProcessingException(Exception):
    """
    An exception that could happen during RSS feed processing
    """
    pass
