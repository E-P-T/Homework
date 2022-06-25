import pytest
import requests

from ..crawler import SuperCrawler


class MockResponse:
    """Mimics the behavior of the Response object."""

    def __init__(self, content: str, status_code: int = 200) -> None:
        """Initializer.

        :param content: The content to be returned.
        :type content: str
        :param status_code: HTTP status code, defaults to 200
        :type status_code: int, optional
        """
        self.content = content
        self.status_code = status_code


def test_get_data(monkeypatch):
    """Checks the type of the returned object.

    Type must be a byte string.
    """

    def mock_get_data(*args, **kwargs):
        return MockResponse(b'')

    monkeypatch.setattr(SuperCrawler, '_get_response', mock_get_data)
    data = SuperCrawler('https://news.yahoo888.com/rss/').get_data()

    assert isinstance(data, bytes)


def test_get_fail_error(monkeypatch):

    def mock_get_status(*args, **kwargs):
        return MockResponse(b'', 100)
