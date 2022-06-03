class RssReaderException(Exception):
    pass

class DateUnifyError(RssReaderException):
    pass

class EmptyUrlError(RssReaderException):
    pass

class InvalidUrlError(RssReaderException):
    pass
