"""
File contains tests for rss_reader.py script
"""
import unittest
import contextlib
import io
import os
import sys
from unittest.mock import patch, call

import rss_exceptions
import rss_reader
from rss_reader import ET, RssReader
tests_dir = os.path.dirname(__file__) + '/test_examples/'
print(tests_dir)


@contextlib.contextmanager
def captured_output():
    """
    The function provides a context manager to redirect 'sys.stdout' to prevent unnecessary information prints
    during testing if needed
    :return:
    """
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestRssReader(unittest.TestCase):

    def test_process_string(self):
        """
        Tests for process_string method of RssReader class
        :return: None
        """
        self.assertEqual(RssReader.process_string('Suzy &amp; John'), 'Suzy & John')
        self.assertEqual(RssReader.process_string('&quot;,&gt;,&lt;'), '",>,<')
        self.assertEqual(
            RssReader.process_string('<p><strong>May 25, 2022</strong> – In its ... shortage.</p>'),
            'May 25, 2022 – In its ... shortage.')
        self.assertEqual(
            RssReader.process_string('<p><strong>May 25,\xa02022</strong> – In its ... shortage.</p>'),
            'May 25, 2022 – In its ... shortage.')

    def test_unify_pubdate(self):
        """
        Tests for unify_pubdate method of RssReader class
        :return: None
        """
        self.assertEqual(RssReader.unify_pubdate('Tue, 24 May 2022 23:45:43 GMT'), '2022:05:24 23:45:43')
        self.assertEqual(RssReader.unify_pubdate('2022-05-30T22:22:05Z'), '2022:05:30 22:22:05')
        self.assertEqual(RssReader.unify_pubdate('Fri, 13 May 2022 17:15:00 -0400'), '2022:05:13 17:15:00')
        self.assertEqual(RssReader.unify_pubdate('2022-06-04T01:00:00+04:00'), '2022:06:04 01:00:00')
        with self.assertRaises(rss_exceptions.DateUnifyError):
            RssReader.unify_pubdate('')
        with self.assertRaises(rss_exceptions.DateUnifyError):
            RssReader.unify_pubdate('20 July 2020')

    def test_validate_url(self):
        """
        Tests for validate_url method of RssReader class
        :return: None
        """
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
        """
        Tests for get_rss_data method of RssReader class
        mocks 'urllib.request.urlopen' to guarantee constant and reliable request data
        :return: None
        """
        mock_open.read_data = b"&lt;p&gt; Iowa, May 27, 2022&lt;/strong&gt; \xe2\x80\x93 Today during ..."
        expected_result = "&lt;p&gt; Iowa, May 27, 2022&lt;/strong&gt; – Today during ..."
        self.assertTrue(RssReader.get_rss_data('https://www.latimes.com/local/rss2.0.xml'), expected_result)

    def test_convert_rss_data_to_root(self):
        """
        Tests for convert_rss_data_to_root method of RssReader class
        uses example files form ./test_examples folder
        :return:
        """
        with open(tests_dir + 'rss_data_xml.xml', encoding='utf-8') as file:
            self.assertEqual(type(RssReader.convert_rss_data_to_root(file.read())), ET.Element)
        with open(tests_dir + 'rss_data_not_xml.txt', encoding='utf-8') as file:
            with self.assertRaises(ET.ParseError):
                RssReader.convert_rss_data_to_root(file.read())

    def test_convert_root_to_dict(self):
        """
        Tests for convert_root_to_dict method of RssReader class
        uses example files form ./test_examples folder
        :return: None
        """
        with open(tests_dir + 'data_v1.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v1.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open(tests_dir + 'data_v2.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v2.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open(tests_dir + 'data_v3.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v3.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open(tests_dir + 'data_v4.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v4.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open(tests_dir + 'data_v5.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v5.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())
        with open(tests_dir + 'data_v6.xml', encoding='utf-8') as inp, open(tests_dir + 'dict_v6.txt',
                                                                            encoding='utf-8') as out:
            self.assertEqual(str(RssReader.convert_root_to_dict(ET.fromstring(inp.read()))), out.read().strip())

    @patch('rss_reader.RssReader.validate_url')
    @patch('builtins.print')
    def test_prepare_dict_val_url(self, mock_print, mock_validate_url):
        """
        Tests for a part of prepare_dict method of RssReader class
        mocks 'builtins.print' for output catching
        mocks 'rss_reader.RssReader.validate_url' to guarantee needed Exceptions raising
        :return: None
        """
        values_val_url = {rss_exceptions.EmptyUrlError('Empty URL'): 'Error occurred while processing URL: Empty URL',
                          rss_exceptions.InvalidUrlError('Invalid URL'): 'Error occurred while processing URL: '
                                                                         'Invalid URL',
                          }
        for i, (key, value) in enumerate(values_val_url.items()):
            mock_validate_url.side_effect = key
            RssReader.prepare_dict('SOME URL, NO MATTER WHAT')
            expected_value = call(value)
            mock_value = mock_print.mock_calls[i]
            self.assertEqual(expected_value, mock_value)

    @patch('rss_reader.RssReader.get_rss_data')
    @patch('builtins.print')
    def test_prepare_dict_get_rss(self, mock_print, mock_get_rss):
        """
        Tests for a part of prepare_dict method of RssReader class
        mocks 'builtins.print' for output catching
        mocks 'rss_reader.RssReader.get_rss_data' to guarantee needed Exceptions raising
        :return: None
        """
        values_get_rss = {rss_reader.error.HTTPError('HTTP Error', 404, 'Not Found', 'smth', 'fp'): 'Error occurred '
                                                                                                    'while accessing '
                                                                                                    'HTTP: HTTP Error '
                                                                                                    '404: Not Found',
                          rss_reader.error.URLError('URL Error'): 'Error occurred while requesting URL: <urlopen '
                                                                  'error URL Error>',
                          UnicodeDecodeError('Some', b'123', 3, 10, 'Bad-bad codec'): "Error occurred while decoding "
                                                                                      "byte string of rss data to "
                                                                                      "UTF-8: 'Some' codec can't "
                                                                                      "decode bytes in position 3-9: "
                                                                                      "Bad-bad codec",
                          Exception('I dunno why'): ('An unexpected error occurred while requesting and processing '
                                                     'rss data: I dunno why'),
                          }
        for i, (key, value) in enumerate(values_get_rss.items()):
            mock_get_rss.side_effect = key
            RssReader.prepare_dict('http://valid_url')
            expected_value = call(value)
            mock_value = mock_print.mock_calls[i]
            self.assertEqual(expected_value, mock_value)

    @patch('rss_reader.RssReader.convert_rss_data_to_root')
    @patch('builtins.print')
    def test_prepare_dict_rss_to_root(self, mock_print, mock_rss_to_root):
        """
        Tests for a part of prepare_dict method of RssReader class
        mocks 'builtins.print' for output catching
        mocks 'rss_reader.RssReader.convert_rss_data_to_root' to guarantee needed Exceptions raising
        mocks 'RssReader.get_rss_data' to ignore previous stages of the prepare_dict function
        :return: None
        """
        values_rss_to_root = {rss_reader.ET.ParseError('some position'): 'Error while parsing rss data, possibly not '
                                                                         'an rss URL passed: ParseError some position',
                              Exception('I dunno why'): ('An unexpected error occurred while parsing rss data: '
                                                         'I dunno why'),
                              }
        RssReader.get_rss_data = unittest.mock.MagicMock()
        for i, (key, value) in enumerate(values_rss_to_root.items()):
            mock_rss_to_root.side_effect = key
            RssReader.prepare_dict('http://valid_url')
            expected_value = call(value)
            mock_value = mock_print.mock_calls[i]
            self.assertEqual(expected_value, mock_value)

    @patch('rss_reader.RssReader.convert_root_to_dict')
    @patch('builtins.print')
    def test_prepare_dict_root_to_dict(self, mock_print, mock_root_to_dict):
        """
        Tests for a part of prepare_dict method of RssReader class
        mocks 'builtins.print' for output catching
        mocks 'rss_reader.RssReader.convert_root_to_dict' to guarantee needed Exceptions raising
        mocks 'RssReader.get_rss_data' and 'RssReader.convert_rss_data_to_root' to ignore previous stages of the
        prepare_dict function
        :return: None
        """
        values_root_to_dict = {rss_exceptions.DateUnifyError('Bad Date'): 'Error occurred while converting datetime: '
                                                                          'Bad Date',
                               TypeError('Wrong type'): ('Incorrect argument type while forming a news dictionary: '
                                                         'Wrong type'),
                               ValueError('Wrong value'): ('Incorrect argument value while forming a news dictionary: '
                                                           'Wrong value'),
                               KeyError('No such key'): ("Incorrect key while forming a news dictionary: "
                                                         "'No such key'"),
                               Exception('I dunno why'): ('An unexpected error occurred while forming a news '
                                                          'dictionary: I dunno why'),
                               }
        RssReader.get_rss_data = unittest.mock.MagicMock()
        RssReader.convert_rss_data_to_root = unittest.mock.MagicMock()
        for i, (key, value) in enumerate(values_root_to_dict.items()):
            mock_root_to_dict.side_effect = key
            RssReader.prepare_dict('http://valid_url')
            expected_value = call(value)
            mock_value = mock_print.mock_calls[i]
            self.assertEqual(expected_value, mock_value)

    @patch('rss_reader.RssReader.get_rss_data')
    def test_prepare_dict(self, mock_get_rss):
        """
        Test for prepare_dict method of RssReader class
        mocks 'RssReader.get_rss_data' to prevent test errors due to URL misfunction
        uses example file form ./test_examples folder
        :return: None
        """
        with open(tests_dir + 'data_v6.xml', encoding='utf-8') as file:
            mock_get_rss.return_value = file.read()
            self.assertTrue(isinstance(RssReader.prepare_dict('https://valid_url'), dict))

    def test_limit_news_dict(self):
        """
        Test for limit_news_dict method of RssReader class
        uses example files form ./test_examples folder
        :return: None
        """
        with open(tests_dir + 'dict_v1.txt', encoding='utf-8') as file:
            dictionary = eval(file.read().strip())
            self.assertEqual(RssReader.limit_news_dict(dictionary), dictionary)
        with open(tests_dir + 'dict_v1.txt', encoding='utf-8') as file:
            dictionary = RssReader.limit_news_dict(eval(file.read().strip()), 1)
            self.assertTrue(len(dictionary['feed_items']) == 1)
        with open(tests_dir + 'dict_v1.txt', encoding='utf-8') as file:
            dictionary = RssReader.limit_news_dict(eval(file.read().strip()), 5)
            self.assertTrue(len(dictionary['feed_items']) == 2)  # test file dict_v1.txt has 2 news items

    @patch('rss_reader.RssReader.prepare_dict')
    @patch('builtins.print')
    def test_return_news_default(self, mock_print, mock_dict):
        """
        Test for return_news_default method of RssReader class
        mocks 'builtins.print' for output catching
        mocks 'RssReader.prepare_dict' to prevent test errors due to URL misfunction
        uses example file form ./test_examples folder
        :return: None
        """
        with open(tests_dir + 'dict_v7.txt', encoding='utf-8') as file:
            dictionary = eval(file.read().strip())
            mock_dict.return_value = dictionary
            news = RssReader('http://valide_url')
            news.return_news_default()
            self.assertEqual(mock_print.mock_calls,
                             [call('=' * 120),
                              call('Feed title: World - CBSNews.com'),
                              call('Feed description: World From CBSNews.com'),
                              call('Feed URL: https://www.cbsnews.com/'),
                              call('Last update: Fri, 03 Jun 2022 09:08:13 -0400'),
                              call('=' * 120),
                              call('Title: Suspected serial killer accused of luring women on Facebook'),
                              call('Link: https://www.cbsnews.com/news/suspected-serial-killer'),
                              call('Publication date: Fri, 03 Jun 2022 08:44:00 -0400'),
                              call(),
                              call('"There are at least seven cases of women\'s killings'),
                              call(),
                              call('Media (image/jpeg) link:\n https://cbsnews3.cbsistatic.com/dnvn-800x450-nopad.jpg'),
                              call('-' * 120)
                              ])

    def test_parse_command_line(self):
        """
        tests rss_reader.parse_command_line function
        uses redirection of 'sys.stdout' to prevent unnecessary information print during tests
        :return:
        """
        parser = rss_reader.parse_command_line(['--limit', '3', '--verbose', '--json', 'https://vse.sale/news/rss',
                                                '--date', '20220601'])
        self.assertTrue(parser.limit)
        self.assertTrue(parser.verbose)
        self.assertTrue(parser.json)
        self.assertTrue(parser.source)
        self.assertTrue(parser.date)
        with captured_output():
            with self.assertRaises(SystemExit):
                rss_reader.parse_command_line(['--help'])
            with self.assertRaises(SystemExit):
                rss_reader.parse_command_line(['-h'])
            with self.assertRaises(SystemExit):
                rss_reader.parse_command_line(['--version'])


if __name__ == '__main__':
    unittest.main()
