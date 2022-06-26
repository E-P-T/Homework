

import pytest
from collections.abc import Generator


from ..parser import BeautifulParser
from ..exceptions import EmptyListError


class MockTags:
    """A custom class.

    That will be a dummy return value will override BeautifulParser._select
    called in BeautifulParser.get_tags_text.
    """

    @property
    def text(self):
        return ['mock_1_text', 'mock_2_text']


def test_get_tags_text_type(monkeypatch):

    def mock_tag(*args, **kwargs):
        return MockTags

    monkeypatch.setattr(BeautifulParser, "_select", mock_tag)
    title_ = BeautifulParser(object).get_tags_text('title')
    assert isinstance(title_, Generator)
