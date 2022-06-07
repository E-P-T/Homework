"""
This file sets logging configuration, by default, according to the task, logging level is set to INFO
"""
import sys
import logging

logger_info = logging
log_format = "%(levelname)s %(asctime)s - %(message)s"
logger_info.basicConfig(level=logging.INFO,
                        stream=sys.stdout,
                        format=log_format,
                        datefmt='%Y:%m:%d %H:%M:%S',
                        )
