from logging import Logger

from ..logger import StreamHandlerConfig


def test_stream_config():
    sc = StreamHandlerConfig()
    logger = sc.set_config('name')
    assert isinstance(logger, Logger)
