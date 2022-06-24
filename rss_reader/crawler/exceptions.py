"""This module contains custom exceptions for the crawler package."""


class BadURLError(Exception):
    """"Occurs when the url is specified incorrectly."""

    def __init__(self, url, *args, **kwargs) -> None:
        self.url = url
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f'It is not possible to get data for the given url ({self.url})'


class FailStatusCodeError(Exception):
    """Occurs when the server response code differs from the expected one."""

    def __init__(self, status_code, *args, **kwargs) -> None:
        self.status_code = status_code
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return 'An unsupported HTTP status code returned. ({self.status_code})'
