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


def test_JSONViewHandler_show(capsys):

    data = {'test_dict': 1}
    json_obj = JSONViewHandler({'json': 1})
    json_obj.show(data)
    out, err = capsys.readouterr()
    out = out.strip('\n')
    x = dumps(data, indent=3)
    assert out == x