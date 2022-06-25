import pytest
import requests


class MockResponse:
    def __init__(self, content, status_code=200) -> None:
        self.content = content
        self.status_code = status_code


def test_get_data(monkeypatch):
    def mock_get_data(*args, **kwargs):
        return MockResponse(b'')
