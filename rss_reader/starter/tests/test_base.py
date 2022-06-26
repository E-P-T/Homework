"""A test suite for the base module."""

import pytest

from ..base import init_arguments_functionality as iaf


@pytest.mark.parametrize("option", [("https://y.com",)])
def test_init_arguments_functionality(option):
    """Check if dictionary returned"""
    a = iaf(option)
    assert isinstance(a, dict)


@pytest.mark.parametrize("option", [("https://y.com", "--json",)])
def test_init_return_json(option):
    """Check if a key exists in a dictionary."""
    a = iaf(option)
    assert 'json' in a
