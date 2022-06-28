import argparse
from datetime import datetime


def date_YYYYMMDD(s):
    try:
        return datetime.strptime(s, "%Y%m%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid format of date: {s}")
