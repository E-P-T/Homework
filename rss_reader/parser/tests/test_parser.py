

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
    """Check the type of the returned object.

    The type of the returned object is Generator.
    """

    def mock_tag(*args, **kwargs):
        return MockTags

    monkeypatch.setattr(BeautifulParser, "_select", mock_tag)
    title_ = BeautifulParser(object).get_tags_text('title')
    assert isinstance(title_, Generator)


def test_get_tags_text_EmptyListError(monkeypatch):

    def mock_raise(*args, **kwargs):
        return []

    monkeypatch.setattr(BeautifulParser, "_select", mock_raise)

    with pytest.raises(EmptyListError):
        next(BeautifulParser(object).get_tags_text('title'))
