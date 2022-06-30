from dateutil.parser import ParserError
from pytest_mock import MockerFixture

from rss_parse.utils.parsing_utils import sanitize_text, to_date


def test_sanitize_text_simple_text_not_changed():
    actual = sanitize_text("abcd xyz 123")
    assert actual == "abcd xyz 123"


def test_sanitize_text_nbsp_becomes_space():
    actual = sanitize_text("a&nbsp;&nbsp;&nbsp;c")
    assert actual == "a   c"


def test_to_date_empty_input_none():
    actual = to_date("")
    assert actual is None


def test_to_date_exception_error(mocker: MockerFixture):
    mocker.patch('dateutil.parser.parse', side_effect=ParserError())

    actual = to_date("1996-04-02 12:12:12")
    assert actual is None
