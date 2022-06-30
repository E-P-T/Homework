"""
Module for datetime enhancements

exports valid_date
"""
from argparse import ArgumentTypeError
from datetime import datetime


def valid_date(s: str) -> datetime.date:
    """
    Parses string with datetime to date format

    Args:
        s:              datetime containing string

    Returns:
        datetime.date:  parsed string to date
    """

    try:
        return datetime.strptime(s, "%Y%m%d").date()
    except ValueError:
        msg = "Not a valid date: {0!r}".format(s)
        raise ArgumentTypeError(msg)
