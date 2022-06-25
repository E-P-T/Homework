import pytest
import requests

from ..crawler import SuperCrawler


class MockResponse:
    def __init__(self, content, status_code=200) -> None:
        self.content = content
        self.status_code = status_code


def test_get_data(monkeypatch):
    def mock_get_data(*args, **kwargs):
        return MockResponse(b'')

    monkeypatch.setattr(SuperCrawler, '_get_response', mock_get_data)
    data = SuperCrawler('https://news.yahoo888.com/rss/').get_data()
