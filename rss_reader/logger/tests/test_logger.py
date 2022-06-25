from logging import Logger

from ..logger import StreamHandlerConfig, NullHandlerConfig


def test_stream_config():
    """Check that the type of logger returned is of type Logger."""
    sc = StreamHandlerConfig()
    logger = sc.set_config('name')
    assert isinstance(logger, Logger)


def test_null_config():
    """Check that NullHandlerConfig returns the desired logger type."""
    sc = NullHandlerConfig()
    logger = sc.set_config('name')
    assert isinstance(logger, Logger)


class TestLogger():
    def test_setup_logger(self, logger_obj):
        o = logger_obj.setup_logger()
        assert isinstance(o, Logger)
