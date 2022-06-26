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
