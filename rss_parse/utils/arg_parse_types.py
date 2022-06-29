import argparse
import os.path
from datetime import datetime


def date_YYYYMMDD(s):
    """
    argparse type that reads date in a format of YYYYMMDD
    """
    try:
        return datetime.strptime(s, "%Y%m%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid format of date: {s}")


def dir_path(dir):
    """
    argparse type that represents an existing directory
    """
    if os.path.isdir(dir):
        return dir
    else:
        raise argparse.ArgumentTypeError(f"{dir} should be an existing directory")
