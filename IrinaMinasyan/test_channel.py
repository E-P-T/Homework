"""Comparison of data that we expect to receive from methods"""
import pytest


from reader.channel import Channel
from reader.exceptions import NotRssFormat, MissingHTTP

channel_item = Channel("https://news.yahoo.com/rss/")


def test_channel_title():
    """Comparing the title of the channel and our script"""
    assert channel_item.get_channel_title() == 'Yahoo News - Latest News & Headlines'


def test_channel_link():
    """Comparing the title of the channel and our script"""
    assert channel_item.get_channel_link() == 'https://www.yahoo.com/news'


def test_channel_description():
    """Comparing the title of the channel and our script"""
    assert channel_item.get_channel_description() == 'The latest news and headlines from Yahoo! News. ' \
                                                     'Get breaking news stories and in-depth coverage with ' \
                                                     'videos and photos.'


def test_parse_error():
    """Expect this error if the wrong url was sent"""
    with pytest.raises(NotRssFormat):
        Channel("https://news.yahoo.com")


def test_missing_schema_error():
    """Expect this error if the HyperText Transfer Protocol is missing 'https://'"""
    with pytest.raises(MissingHTTP):
        Channel("www.news.yahoo.com")
