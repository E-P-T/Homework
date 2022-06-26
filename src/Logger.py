from enum import Enum
from typing import Callable

from colorama import Fore

from Util import Util


class Level(Enum):
    INFO: Fore = Fore.GREEN
    WARNING: Fore = Fore.YELLOW
    ERROR: Fore = Fore.RED


class Logger:
    __logger: Callable

    @classmethod
    def verbose(cls, is_verbose: bool):
        cls.__logger = print if is_verbose else lambda *args: None

    @classmethod
    def log(cls, level: Level, message: str) -> None:
        message = Util.colorize(f'[{level.name}] {message}', level.value)

        if level is Level.ERROR:
            print(message)
            exit(-1)

        cls.__logger(message)
