class RssReaderException(Exception):
    pass


class DateUnifyError(RssReaderException):
    pass


class EmptyUrlError(RssReaderException):
    pass


class InvalidUrlError(RssReaderException):
    pass


class NoDataInCache(RssReaderException):
    pass


if __name__ == '__main__':
    pass
