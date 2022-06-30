"""
Module for application internal configs

exports appname, appauthor, verbose_print
"""
import builtins as __builtin__

# E731 do not assign a lambda expression, use a def
# Breaking the rule, because it will lead to less readability and more code
appname = "RSSReader"
appauthor = "nmac99"

COLORIZED_MODE = False
verbose_print = lambda *a, **k: None


COLORS = {
    "pink": "\033[95m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "warn": "\033[93m",
    "err": "\033[91m",
    "bold": "\033[1m",
    "und": "\033[4m",
    "none": ""
}


def print(text: str, type: str = "none"):
    """Custom print() function to handle colorized mode"""
    if not COLORIZED_MODE:
        return __builtin__.print(text)
    else:
        endc = "\033[0m"
        formatted_text = f"{COLORS[type]}{text}{endc}"
        return __builtin__.print(formatted_text)
