"""A test suite for the loader module."""

import pytest

from rss_reader.loader.loader import FromWebHandler
from rss_reader.crawler.crawler import SuperCrawler
from rss_reader.parser.parser import BeautifulParser


@pytest.fixture
def mock_crawler(mocker):
    """Replaces crawler methods"""

    m = __name__ + '.SuperCrawler'
    mock_cls = mocker.patch(m)
    mock_cp = mock_cls.return_value
    mock_cp.get_data.return_value = "Response!"
