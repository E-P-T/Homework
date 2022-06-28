from dateutil import parser as iso_date_parser
from dateutil.parser import ParserError


def sanitize_text(txt):
    return txt.replace("&nbsp;", " ")


def to_date(date_str):
    if not date_str:
        return None
    try:
        return iso_date_parser.parse(date_str).astimezone()
    except ParserError:
        return None
