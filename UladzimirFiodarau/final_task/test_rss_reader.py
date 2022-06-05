import unittest
from unittest.mock import patch
import os

import rss_exceptions
from rss_reader import ET, RssReader


class TestRssReader(unittest.TestCase):

    def test_unify_pubdate(self):
        self.assertEqual(RssReader.unify_pubdate('Tue, 24 May 2022 23:45:43 GMT'), '2022:05:24 23:45:43')
        self.assertEqual(RssReader.unify_pubdate('2022-05-30T22:22:05Z'), '2022:05:30 22:22:05')
        self.assertEqual(RssReader.unify_pubdate('Fri, 13 May 2022 17:15:00 -0400'), '2022:05:13 17:15:00')
        self.assertEqual(RssReader.unify_pubdate('2022-06-04T01:00:00+04:00'), '2022:06:04 01:00:00')
        with self.assertRaises(rss_exceptions.DateUnifyError):
            RssReader.unify_pubdate('')
        with self.assertRaises(rss_exceptions.DateUnifyError):
            RssReader.unify_pubdate('20 July 2020')

    def test_validate_url(self):
        self.assertTrue(RssReader.validate_url('https://www.latimes.com/local/rss2.0.xml'))
        self.assertTrue(RssReader.validate_url('https://feeds.simplecast.com/54nAGcIl'))
        with self.assertRaises(rss_exceptions.InvalidUrlError):
            RssReader.validate_url('Hi there!')
        with self.assertRaises(rss_exceptions.InvalidUrlError):
            RssReader.validate_url('latimes.com/local/rss2.0.xml')
        with self.assertRaises(rss_exceptions.InvalidUrlError):
            RssReader.validate_url('https://')
        with self.assertRaises(rss_exceptions.InvalidUrlError):
            RssReader.validate_url('https://feeds.latimes.com/' + 'local/' * 400 + 'rss2.0.xml')
        with self.assertRaises(rss_exceptions.EmptyUrlError):
            RssReader.validate_url()
        with self.assertRaises(rss_exceptions.EmptyUrlError):
            RssReader.validate_url(' ')

    @patch('urllib.request.urlopen')
    def test_get_rss_data(self, mock_open):
        mock_open.read_data = b"&lt;p&gt; Iowa, May 27, 2022&lt;/strong&gt; \xe2\x80\x93 Today during ..."
        expected_result = "&lt;p&gt; Iowa, May 27, 2022&lt;/strong&gt; – Today during ..."
        self.assertTrue(RssReader.get_rss_data('https://www.latimes.com/local/rss2.0.xml'), expected_result)

    def test_convert_rss_data_to_root(self):
        with open('./test_examples/rss_data_xml.xml', encoding='utf-8') as file:
            self.assertEqual(type(RssReader.convert_rss_data_to_root(file.read())), ET.Element)
        with open('./test_examples/rss_data_not_xml.txt', encoding='utf-8') as file:
            with self.assertRaises(ET.ParseError):
                RssReader.convert_rss_data_to_root(file.read())

    def test_convert_root_to_dict(self):
        with open('./test_examples/data_v1.xml', encoding='utf-8') as inp, open('./test_examples/dict_v1.txt',
                                                                                encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open('./test_examples/data_v2.xml', encoding='utf-8') as inp, open('./test_examples/dict_v2.txt',
                                                                                encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open('./test_examples/data_v3.xml', encoding='utf-8') as inp, open('./test_examples/dict_v3.txt',
                                                                                encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open('./test_examples/data_v4.xml', encoding='utf-8') as inp, open('./test_examples/dict_v4.txt',
                                                                                encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open('./test_examples/data_v5.xml', encoding='utf-8') as inp, open('./test_examples/dict_v5.txt',
                                                                                encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())

    def test_process_string(self):
        self.assertEqual(RssReader.process_string('Suzy &amp; John'), 'Suzy & John')
        self.assertEqual(RssReader.process_string('&quot;,&gt;,&lt;'), '",>,<')
        self.assertEqual(
            RssReader.process_string('<p><strong>May 25, 2022</strong> – In its ... shortage.</p>'),
            'May 25, 2022 – In its ... shortage.')
        self.assertEqual(
            RssReader.process_string('<p><strong>May 25,\xa02022</strong> – In its ... shortage.</p>'),
            'May 25, 2022 – In its ... shortage.')


if __name__ == '__main__':
    unittest.main()
