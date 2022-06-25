import pytest


def logger_obj(request):
    yield Logger('test_name', request.param())
