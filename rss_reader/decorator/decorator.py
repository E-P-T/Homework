
from functools import wraps
from rss_reader.logger.logger import Logger

log = Logger.get_logger(__name__)


def send_log_of_start_function(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper
