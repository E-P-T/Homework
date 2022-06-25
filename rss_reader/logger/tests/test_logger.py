from logging import Logger

from ..logger import StreamHandlerConfig


def test_stream_config():
    """Check that the type of logger returned is of type Logger."""
    sc = StreamHandlerConfig()
    logger = sc.set_config('name')
    assert isinstance(logger, Logger)


def test_null_config():
    sc = NullHandlerConfig()
