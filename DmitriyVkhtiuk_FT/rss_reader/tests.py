"""
File contains tests for rss_reader.py script
"""
import unittest
from unittest import TestCase
from unittest.mock import patch, call
from modified_argparser import *
from news_brain import *


class TestRssReader(TestCase):
    @patch("builtins.print")
    def test_not_valid_path(self, mock_print):
        """
        tests not valid dir path and check, will the default dir path return
        :param mock_print: mock builtins.print
        :return: message, that path is incorrect and files will be saved to the default dir
        """
        p = ArgParser()
        path = Path.home().parent / "xdd"
        result = p.valid_path(path)
        expected = Path.cwd() / "default_dir"
        self.assertEqual(result, expected)
        self.assertEqual(mock_print.mock_calls, [call("Invalid path.. Saving to the project default dir")])

    def test_valid_path(self):
        """
        tests valid path and check, will the valid path to directory return or not.
        :return: valid dir path to save converted news
        """
        p = ArgParser()
        path = Path.home()
        result = p.valid_path(path)
        expected = Path(path)
        self.assertEqual(result, expected)

    @patch("requests.get")
    def test_valid_get_rss_data(self, mock_get):
        """
        test mocks requests.get and check the method get_rss_data with created template
        :param mock_get: part of  xml template to check the work of method get_rss_data
        :return: None
        """
        news = NewsBrain("https://news.yahoo.com/rss/", None, False, None, None, None, None)
        mock_get.return_value.text = '<?xml version="1.0" encoding="UTF-8"?><rss xmlns:media="http://search.yahoo.com/'\
                                     'mrss/" version="2.0"></rss>'
        expected_result = bs4.BeautifulSoup(
            '<?xml version="1.0" encoding="UTF-8"?><rss xmlns:media="http://search.yahoo.com/mrss/" version="2.0">'
            '</rss>',
            "xml")
        self.assertTrue(news.get_rss_data(), expected_result)

    @patch("requests.get")
    def test_get_news_text(self, mock_get):
        """
        Tests work of method get_news_text, if description tag is not in bs4.BeautifulSoup object.
        Mocks requests.get with template of html page with article tag and check the work of method.
        :return: None
        """
        news = NewsBrain("https://news.yahoo.com/rss/", None, False, None, None, None, None)
        mock_get.return_value.content = "<article><p>abcd</p></article>"
        self.assertEqual(news.get_news_text("https://news.yahoo.com/senator-2010-deposition-13-olds-152104735.html"),
                         "abcd")

    @patch("pandas.read_csv")
    def test_reformat_the_dates(self, mock_read):
        """
        Test mocks pandas.read_csv with template of DataFrame to check the work of method reformat_the_dates without
        reading "cache.csv".
        :return: None
        """
        news = NewsBrain(None, None, False, None, None, None, None)
        test_date_dict = {
            "Date": ["Tue, 25 May 2021 23:45:43 GMT", "2022-03-30T22:21:05Z", "Fri, 13 Jun 2022 17:15:00 -0400",
                     "2022-06-04T01:00:00+04:00"]
        }
        mock_read.return_value = pandas.DataFrame(test_date_dict)
        expected_dict = {
            "Date": ["20220613", "20220604", "20220330", "20210525"]
        }
        expected = pandas.DataFrame(expected_dict)
        self.assertEqual(True, news.reformat_the_dates().reset_index(drop=True).equals(expected.reset_index(drop=True)))

    @patch("builtins.print")
    @patch("pandas.read_csv")
    def test_invalid_reformat_the_dates(self, mock_read, mock_print):
        """
        Tests the case of pubDate, if the template to reformat the date does not exist.
        Mocks pandas.read_csv to check the work without file "cache.csv",
        mocks builtins.print to check, will be right message outputted or not.

        :return: None
        """
        news = NewsBrain(None, None, False, None, None, None, None)
        test_date_dict = {
            "Date": ["Tue, 25 May 2021 23:45:43 GMT", "2022-03-30T22:21:05Z", "Fri, 13 Jun 2022 17:15:00 -0400",
                     "2022-06-04T01:00:00+04:00+35"]
        }
        mock_read.return_value = pandas.DataFrame(test_date_dict)
        expected_dict = {
            "Date": ["20220613",  "20220330", "2022-06-04T01:00:00+04:00+35", "20210525"]
        }
        expected = pandas.DataFrame(expected_dict)
        news.reformat_the_dates().reset_index(drop=True)
        self.assertEqual(mock_print.mock_calls, [call("Can't reformat the date 2022-06-04T01:00:00+04:00+35")])
        self.assertEqual(True, news.reformat_the_dates().reset_index(drop=True).equals(expected))

    @patch("builtins.print")
    @patch("bs4.BeautifulSoup.find_all")
    def test_invalid_data_get_news(self, mock_val, mock_print):
        """
        Test mocks method find_all from bs4.BeautifulSoup class with template of invalid xml page.
        test mock builtins.print to check the message(error), which will be printed in stdout.
        :return: None
        """
        news = NewsBrain("https://news.google.com/rss/", None, False, None, None, None, None)
        mock_val.return_value = []
        xml_data = bs4.BeautifulSoup(
            '<?xml version="1.0" encoding="UTF-8"?><rss xmlns:media="http://search.yahoo.com/mrss/"></rss>', "xml")
        news.get_news(xml_data)
        self.assertEqual(mock_print.mock_calls, [call("News Not Found. Please, check your RSS URL.")])

    @patch("builtins.print")
    def test_df_to_dict(self, mock_print):
        """
        Tests that there are no changes in the initial data frame after converting df to dict and printing it out.
        Mocks printing dict to console.
        :return: None
        """
        news = NewsBrain(None, None, False, None, None, None, None)
        d = {
            "Source": ["b", "c", "d"],
            "Feed": ["e", "f", "g"],
            "Title": ["1", "2", "3"],
            "Date": ["2", "4", "5"],
            "Link": ["12", "32", "21"],
            "Description": ["A", "B", "C"],
            "Image": ["jpg", "png", "jpeg"]
        }
        mock_print.return_value = None
        df = pandas.DataFrame(d)
        self.assertEqual(True, news.df_to_dict(df).equals(df))

    @patch("builtins.print")
    def test_invalid_limit_get_news(self, mock_print):
        """
        Tests method behavior with an invalid limit, but with valid data. template for check is taken from test_files
        dir. Mocks builtins print to check message, what will be printed in this case.
        :return: None
        """
        news = NewsBrain("https://www.buzzfeed.com/world.xml", 0, False, None, None, None, None)
        with open(work_dir / "test_files" / "test_get_news.txt") as f:
            xml_data = bs4.BeautifulSoup(f.read(), "xml")
        news.get_news(xml_data, 0)
        self.assertEqual(mock_print.mock_calls, [call("News limit must be positive number")])

    @patch("builtins.print")
    @patch("pandas.read_csv")
    def test_print_from_cache_invalid_limit(self, mock_reformat_the_dates, mock_print):
        """
        Tests method behavior with an invalid limit, but with valid date. Test mocks pandas.read_csv to use
        template for check the behaviour of method. Mocks builtins.print to check message, what will be printed
        in this case.

        :return: None
        """
        test_dict = {
            "Date": ["Tue, 25 May 2021 23:45:43 GMT", "2022-03-30T22:21:05Z", "Fri, 13 Jun 2022 17:15:00 -0400",
                     "2022-06-04T01:00:00+04:00"],
            "Source": ["https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line",
                       "https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line"]
        }
        expected = pandas.DataFrame(test_dict)
        mock_reformat_the_dates.return_value = expected
        news = NewsBrain(None, 0, False, "20220613", None, None, None)
        news.print_from_cache(0)
        self.assertEqual(mock_print.mock_calls, [call("News limit must be a positive number..")])

    @patch("builtins.print")
    @patch("pandas.read_csv")
    def test_print_from_cache_no_news_found(self, mock_reformat_the_dates, mock_print):
        """
        Tests method behavior with a valid limit, but with invalid date. Test mocks pandas.read_csv to use
        template for check the behaviour of method. Mocks builtins.print to check message, what will be printed
        in this case.
        :return: None
        """
        test_dict = {
            "Date": ["Tue, 25 May 2021 23:45:43 GMT", "2022-03-30T22:21:05Z", "Fri, 13 Jun 2022 17:15:00 -0400",
                     "2022-06-04T01:00:00+04:00"],
            "Source": ["https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line",
                       "https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line"]
        }
        expected = pandas.DataFrame(test_dict)
        mock_reformat_the_dates.return_value = expected
        news = NewsBrain(None, 5, False, "20220603", None, None, None)
        news.print_from_cache(5)
        self.assertEqual(mock_print.mock_calls, [call("Error: No news found on this date")])

    @patch("builtins.print")
    @patch("pandas.read_csv")
    def test_print_from_cache_with_url_specified(self, mock_reformat_the_dates, mock_print):
        """
        Tests method behavior with a valid limit, with valid date but with invalid source. Test mocks pandas.read_csv
        to use template for check the behaviour of method. Mocks builtins.print to check message, what will be printed
        in this case.
        :return: None
        """
        test_dict = {
            "Date": ["Tue, 25 May 2021 23:45:43 GMT", "2022-03-30T22:21:05Z", "Fri, 13 Jun 2022 17:15:00 -0400",
                     "2022-06-04T01:00:00+04:00"],
            "Source": ["https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line",
                       "https://rss.art19.com/apology-line", "https://rss.art19.com/apology-line"]
        }
        expected = pandas.DataFrame(test_dict)
        mock_reformat_the_dates.return_value = expected
        news = NewsBrain("https://vse.sale/news/rss", 2, False, "20220613", None, None, None)
        news.print_from_cache(2)
        self.assertEqual(mock_print.mock_calls, [call("Error: No news found on this date with given source.")])

    @patch("pandas.DataFrame.to_csv")
    @patch("builtins.print")
    def test_valid_get_news(self, mock_print, mock_pandas):
        """
        Test checks behaviour of get_news() method with valid limit and  with valid template 'test_get_news.txt',
        which is the part of real xml page. Mocks builtins print to check new, what will be printed in this case.
        :return: None
        """
        news = NewsBrain("https://www.buzzfeed.com/world.xml", 1, False, None, None, None, None)
        with open(work_dir / "test_files" / "test_get_news.txt", encoding="utf-8") as f:
            xml_data = bs4.BeautifulSoup(f.read(), "xml")
        news.get_news(xml_data)
        mock_pandas.return_value = None
        self.assertEqual(mock_print.mock_calls, [
            call('\x1b[39m'),
            call('Source: https://www.buzzfeed.com/world.xml'),
            call('Feed: BuzzFeed News'),
            call('Title: She Was One Year Away From Going To College. Then The Taliban Banned Her From School.'),
            call('Date: Mon, 13 Jun 2022 20:32:05 -0400'),
            call('Link: https://www.buzzfeednews.com/article/syedzabiullah/afghanistan-taliban-girls-school-ban'),
            call('Description: BuzzFeed, Reporting To You'),
            call('Image: https://webappstatic.buzzfeed.com/static/images/public/rss/logo-news.png'),
            call('\n\n')])


if __name__ == '__main__':
    unittest.main()
