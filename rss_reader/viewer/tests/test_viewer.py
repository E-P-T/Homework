"""A test suite for the viewer module."""

from json import dumps

from ..viewer import JSONViewHandler, StandartViewHandler


def test_StandartViewHandler_show(capsys):

    data = {'title_web_resource': 'mock_show'}
    json_obj = StandartViewHandler()
    json_obj.show(data)
    out, err = capsys.readouterr()
    out = out.strip('\n')
    assert out == 'Feed: : mock_show'
