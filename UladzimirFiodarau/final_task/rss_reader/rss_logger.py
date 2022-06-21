"""
This file sets logging configuration, by default, according to the task, logging level is set to INFO
"""
import sys
import logging

NO_COLOR = "\33[m"


def add_color(logger_method, _color):
    """
    A decorator to enable colouring of logger output methods, uses ANSI escape codes to apply colouring
    :param logger_method: method to set colour
    :param _color: 3* for foreground colouring, 4* for background
    :return: coloured output in wrapped method
    """
    def wrapper(message, *args, **kwargs):
        """
        Wraps a message with ANSI color escape codes
        :param message: Given message
        :param args: args of logger_method
        :param kwargs: kwargs of logger_method
        :return: logger method with message wrapped
        """
        color = kwargs.pop("color", _color)
        if isinstance(color, int):
            color = "\33[%dm" % color
        return logger_method(color + message+NO_COLOR, *args, **kwargs)
    return wrapper


# setting basic logger configuration
logger_info = logging
log_format = "%(levelname)s %(asctime)s - %(message)s"
logger_info.basicConfig(level=logging.INFO,
                        stream=sys.stdout,
                        format=log_format,
                        datefmt='%Y:%m:%d %H:%M:%S',
                        )

# setting default color of info print to no color and enabling decorator
setattr(logger_info, "info", add_color(getattr(logger_info, "info"), NO_COLOR))


if __name__ == '__main__':
    pass
