import pytest

from ..logger import Logger, StreamHandlerConfig, NullHandlerConfig


@pytest.fixture(scope="class",
                params=[StreamHandlerConfig,
                        NullHandlerConfig])
def logger_obj(request):
    """The fixture returns a logger object with different configurations."""
    yield Logger('test_name', request.param())
