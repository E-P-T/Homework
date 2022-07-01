"""A test suite for the parser module."""

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
    """подтвердить возникновение ошибки EmptyListError."""

    def mock_raise(*args, **kwargs):
        return []

    monkeypatch.setattr(BeautifulParser, "_select", mock_raise)

    with pytest.raises(EmptyListError):
        next(BeautifulParser(object).get_tags_text('title'))


def test_get_tags_text_amount_of_elements(monkeypatch):
    """Check that the correct number of elements is returned."""

    def mock_tags(*args, **kwargs):
        return [MockTags(), MockTags()]

    monkeypatch.setattr(BeautifulParser, "_select", mock_tags)

    result = BeautifulParser(object).get_tags_text('title')
    count = 0
    for i in result:
        count += 1
    assert count == 2


def test_get_items_empty(monkeypatch):
    """Check that an empty dictionary is returned on an invalid tag"""
    def mock_items(*args, **kwargs):
        return []

    monkeypatch.setattr(BeautifulParser, "_find_all", mock_items)

    result = BeautifulParser(object).get_items({}, 'title')

    assert bool(result) is False
