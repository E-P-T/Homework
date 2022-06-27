"""This module contains decorators used in the program."""

from functools import wraps
from rss_reader.logger.logger import Logger

log = Logger.get_logger(__name__)


def send_log_of_start_function(func):
    """Log the start and end of the function.

    It is decorator function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.info(f'A {func.__name__} function starts working.')
        res = func(*args, **kwargs)
        log.info(f'A {func.__name__} function has completed its work.')
        return res
    return wrapper