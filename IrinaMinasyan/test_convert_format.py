import pytest
import xml.etree.ElementTree as ET

from reader.convert import Convert
from os import path, getcwd
from reader.item import NewsItem
from reader.cache import Cache
from reader.exceptions import CacheNotFound

tree = ET.parse(path.join(getcwd(), 'examples', 'example_xml.xml'))
root = tree.getroot()
news_item = root.find('channel').find('item')
news = NewsItem(news_item)


def test_html_convert():
    with open(path.join(getcwd(), 'examples', 'example_html.html'), 'r') as efile:
        exam_file = efile.read()
    Convert.create_html_file([news])
    with open(path.join(getcwd(), 'RSS_NEWS.html'), 'r') as rfile:
        read_file = rfile.read()
    assert exam_file == read_file


def test_read_from_cache():
    with pytest.raises(CacheNotFound):
        Cache().read_from_cache('23232323')
