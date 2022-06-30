"""Comparison of data that we expect to receive from methods"""
import pytest
import argparse

from reader.item import NewsItem
from reader import add_args
from os import path, getcwd
import xml.etree.ElementTree as ET
from reader.utils import media_content_verification

tree = ET.parse(path.join(getcwd(), 'examples', 'example_xml.xml'))
root = tree.getroot()
news_item = root.find('channel').find('item')

def test_get_json():
    """Comparing json format"""
    news = NewsItem(news_item)
    assert NewsItem.get_json(news) == str({"Title": news.get_title(),
                                                   "Date": news.get_date(),
                                                   "Link": news.get_link(),
                                                   "Image link": news.get_image()}).replace("'", '"')


def test_item_title():
    assert NewsItem(news_item).get_title() == 'Officials: Georgia man sentenced to die kills self in prison'


def test_item_date():
    assert NewsItem(news_item).get_date() == '2022-06-27T12:50:43Z'


def test_item_link():
    assert NewsItem(news_item).get_link() == 'https://news.yahoo.com/officials-georgia-man-sentenced-die-125043110.html'


def test_item_image():
    assert NewsItem(news_item).get_image() == "https://s.yimg.com/uu/api/res/1.2/zEeBoPLQVzw1u2VjZt.THA--~B/aD03NDk7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap.org/5cf8e923a8d9dec8758480785184f376"


def test_attribute_error():
    """Expect this error if the not xml format was sent"""
    with pytest.raises(AttributeError):
        NewsItem("https://news.yahoo.com")


def test_args_digit_type_error():
    with pytest.raises(argparse.ArgumentTypeError):
        add_args.check_digit('hello')


def test_args_positive_type_error():
    with pytest.raises(argparse.ArgumentTypeError):
        add_args.check_positive('-15')


def test_img_verification():
    assert media_content_verification(news_item)['url'] == "https://s.yimg.com/uu/api/res/1.2/zEeBoPLQVzw1u2VjZt.THA--~B/aD03NDk7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap.org/5cf8e923a8d9dec8758480785184f376"
