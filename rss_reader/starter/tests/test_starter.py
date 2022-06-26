"""A test suite for the starter module."""

from pytest import raises


from ..starter import Starter
from ..ecxeptions import NonNumericError


def test_starter_run_NonNumericError():
    """Check NonNumericError exception return

    Occurs when --limit is not equal to a number.
    """

    argv = {'source': 1, 'limit': 'abc'}
    s = Starter(argv)
    with raises(NonNumericError):
        s.run()


def test_starter_run_BadURLError(monkeypatch):
    """Verify that the BadURLError exception is being caught.

    Occurs when an invalid URL is specified.
    """

    def mock_get_status(*args, **kwargs):
        class Mock_BadURLError:
            @classmethod
            def get_data(self, a, b, c, d):
                raise BadURLError
        return Mock_BadURLError()

    monkeypatch.setattr(Starter, '_get_data_from_resource', mock_get_status)

    argv = {'source': 1, 'limit': 1}
    s = Starter(argv)
    with raises(BadURLError):
        s.run()
