import unittest
from rss_reader_package.link import Link
from rss_reader_package.utils.exceptions import LinkWithNoSourceError


class TestLink(unittest.TestCase):
    def test_link(self):
        link = Link("source", "image")
        self.assertEqual(link.href, "source")
        self.assertEqual(link.link_type, "image")
        self.assertEqual(str(link), "source (image)")
        link2 = Link("source")
        self.assertEqual(link2.link_type, "unknown")
        with self.assertRaises(LinkWithNoSourceError):
            Link(True)


unittest.main()
