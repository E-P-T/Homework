"""
Module for custom Errors

exports WringUrlError, WrongLimitError, ConvertJSONError, LinkWithNoSourceError, CachedFeedNotFoundError
"""


class Error(Exception):
    """Base class for custom errors"""
    pass


class WrongUrlError(Error):
    """Error for wrong url specification"""
    pass


class WrongLimitError(Error):
    """Error for wrong limit specification"""
    pass


class ConvertJSONError(Error):
    """Error for JSON converting issues"""
    pass


class LinkWithNoSourceError(Error):
    """Error for not providing source to Link object"""
    pass


class CachedFeedNotFoundError(Error):
    """Error for not found feed cache"""
    pass


class NotSupportedConversionFormat(Error):
    """Error for not supported conversion formats"""
    pass
