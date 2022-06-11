from enum import Enum

from .Color import Color
from .Util import Util


class Logger:
    """
    Logger class
    """

    class Level(Enum):
        """
        Enum-class for logging levels
        """
        INFO = Color.GREEN
        WARNING = Color.YELLOW
        ERROR = Color.RED

    def __init__(self, verbose: bool):
        self.logger = print if verbose else lambda *args: None
        self.force_logger = print

    def log(self, message: str, level: Level) -> None:
        """
        Logs a message with a given level
        logger is print if verbose is True
        else is a lambda function that does nothing
        """
        message = f'[{level.name}] {message}'
        self.logger(Util.colorize(message, level.value))

    def force_log(self, message: str, level: Level) -> None:
        """
        Logs a message with a given level
        but prints even if verbose is False
        """
        message = f'[{level.name}] {message}'
        self.force_logger(Util.colorize(message, level.value))

    def info(self, message: str) -> None:
        """
        Logs a message with INFO level
        """
        self.log(message, Logger.Level.INFO)

    def warning(self, message: str) -> None:
        """
        Logs a message with WARNING level
        """
        self.log(message, Logger.Level.WARNING)

    def error(self, message: str) -> None:
        """
        Logs a message with ERROR level
        """
        self.force_log(message, Logger.Level.ERROR)
