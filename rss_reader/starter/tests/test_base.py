"""A test suite for the base module."""

import pytest

from ..base import init_arguments_functionality as iaf


@pytest.mark.parametrize("option", [("https://y.com",)])
def test_init_arguments_functionality(option):
    a = iaf(option)
    assert isinstance(a, dict)
