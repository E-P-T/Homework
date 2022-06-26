"""A test suite for the viewer module."""

from json import dumps

from ..viewer import JSONViewHandler, StandartViewHandler


def test_StandartViewHandler_show(capsys):
    """check that the show method prints the correct data to stdout."""

    data = {'title_web_resource': 'mock_show'}
    json_obj = StandartViewHandler()
    json_obj.show(data)
    out, err = capsys.readouterr()
    out = out.strip('\n')
    assert out == 'Feed: : mock_show'
