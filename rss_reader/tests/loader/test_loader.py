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


@pytest.fixture
def mock_parser(mocker):
    """Replaces parser methods"""

    m = __name__ + '.BeautifulParser'
    mock_cls = mocker.patch(m)
    mock_cp = mock_cls.return_value
    mock_cp.create_parser.return_value = "Create!"
    mock_cp.get_tags_text.return_value = iter(["Title!"])
    mock_cp.get_items.return_value = [{'mock_item': 1}]


def test_get_items_empty(mock_crawler, mock_parser):
    """Check that a dictionary of the given structure is returned"""

    h = FromWebHandler('a', 'b', 'c', 1, SuperCrawler, BeautifulParser('s'))
    r = h.get_data()
    assert r == [{'title_web_resource': 'Title!',
                  'link': 'c',
                  'items': [{'mock_item': 1}]}]
