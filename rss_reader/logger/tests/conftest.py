import pytest

from ..logger import Logger


def logger_obj(request):
    yield Logger('test_name', request.param())
