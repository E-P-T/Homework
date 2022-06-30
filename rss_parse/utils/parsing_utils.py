from dateutil import parser as iso_date_parser
from dateutil.parser import ParserError


def sanitize_text(txt):
    """
    Removes some encoded text from a string
    """
    return txt.replace("&nbsp;", " ")


def to_date(date_str):
    """
    Reads a date from a string and converts in to a user timezone
    """
    if not date_str:
        return None
    try:
        return iso_date_parser.parse(date_str).astimezone()
    except ParserError:
        return None
