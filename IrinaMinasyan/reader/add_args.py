"""Add arguments, which will be available, when we work with command-line"""
import argparse


def check_positive(value):
    """Given argument must be positive"""
    check_digit(value)
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError(f"can only be positive. Your input = {value}.")
    return value


def check_digit(value):
    """Given argument must be digit"""
    if not value.isdigit():
        raise argparse.ArgumentTypeError(f"can only be integer. Your input = {value}.")
    return value


parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
parser.add_argument("source", nargs='?', help="RSS URL")
parser.add_argument("--version", help="Print version info", action="store_true")
parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
parser.add_argument("--verbose", help="Output verbose status messages", action="store_true")
parser.add_argument("--limit", help="Limit news topics if this parameter provided", type=check_positive)
parser.add_argument("--date", help="Read cached news for provided URL. If not provided source "
                                   "- prints all cached news for this date.", type=check_digit,)
parser.add_argument("--to_pdf", help="Converts news to pdf format and save it", action="store_true")
parser.add_argument("--to_html", help="Converts news to html format and save it", action="store_true")
args = parser.parse_args()
