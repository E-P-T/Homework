"""Test RssCacher class."""

from unittest import TestCase

from engine.rsscacher import QueryError, RssCacher, StorageError


class TestRssCacher(TestCase):
    """Testcase for RssCacher class."""

    def test_store_channel(self):
        """
        store_channel() test.
        """
        with RssCacher(':memory:') as db:
            with self.assertRaises(StorageError):
                db.store_channel({})

    def test_store_entry(self):
        """
        store_entry() test.
        """
        with RssCacher(':memory:') as db:
            with self.assertRaises(StorageError):
                db.store_entry({}, 0)

    def test_feed(self):
        """
        feed() test.
        """
        with RssCacher(':memory:') as db:
            with self.assertRaises(QueryError):
                db.feed("", 1, None)
