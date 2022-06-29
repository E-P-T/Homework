import argparse
from datetime import datetime

import pytest

from rss_parse.utils.arg_parse_types import date_YYYYMMDD


def test_date_YYYYMMDD_parsing():
    actual = date_YYYYMMDD("20201010")
    assert actual == datetime(2020, 10, 10)


def test_date_YYYYMMDD_invalid_format_error():
    with pytest.raises(argparse.ArgumentTypeError):
        date_YYYYMMDD("2020-10-10")
