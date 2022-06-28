import unittest
from datetime import datetime
from json_to_html import convert_to_html
from json_convert_to_pdf import convert_to_pdf
from utilty import isValidURL
import argparse
# from rss_reader import get_arg

def create_parser():
    parser = argparse.ArgumentParser(...)
    parser.add_argument("-v", "--version", help="Print version info",
                        action="store_true")
    parser.add_argument(
        "--verbose", help="Output verbose status messages", action="store_true")
    parser.add_argument("source", type=str, nargs="?",  help="RSS URL")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true")

    parser.add_argument("--limit", type=int, const=None,
                        help="Limit news topics if this parameter provided", nargs='?')
    parser.add_argument("--date", nargs="?", const=1, type=int,
                        help="Retrieves data from a given date from the cache if this parameter is provided")
    parser.add_argument("--to_html", nargs="?", const='rss_news.html',
                        help="Convert news to .html format and save it by the specified folder path (FOLDER_PATH can be optional).",
                        )
    parser.add_argument("--to_pdf", const='news_rss.pdf', nargs="?",
                        help="Convert news to .pdf format and save it by the specified folder path (FOLDER_PATH can be optional)")
    # ...Create your parser as you like...
    return parser

class TestRssReader(unittest.TestCase):
    def setUp(self) -> None:
        self.html_filename = 'test.html'
        self.pdf_filename = 'test.pdf'
        self.url = "https://news.google.com/rss/"
        self.convert_dataset = [{'title': 'Abortion Pills Take the Spotlight as States Impose Abortion Bans', 'date': '2022-06-26 07:00:12', 'link': 'https://www.nytimes.com/2022/06/26/health/abortion-medication-pills.html',
                                 'image_link': 'https://static01.nyt.com/images/2022/06/25/multimedia/25abortion-pills-topart/25abortion-pills-topart-moth.jpg', 'description': 'Demand for medication abortion is surging, setting the stage for new legal battles.', 'creator': 'Pam Belluck'}]
        
        self.to_html = convert_to_html(self.convert_dataset,self.html_filename)
        self.to_pdf = convert_to_pdf(self.convert_dataset,self.pdf_filename)
        self.valid_url = isValidURL(self.url)
        self.parser = create_parser()
        
    def test_convet_to_html(self):
        self.assertEqual(self.to_html, 'OK')

    def test_convert_to_pdf(self):
        self.assertEqual(self.to_pdf, 'OK')
    
    def test_is_valid_url(self):
        self.assertEqual(self.valid_url,True)
    
    def test_arg_limit(self):
        parsed = self.parser.parse_args(['--limit','5'])
        self.assertEqual(parsed.limit, 5)
    
    def test_arg_source(self):
        parsed = self.parser.parse_args(['https://news.google.com/rss/'])
        self.assertEqual(parsed.source, 'https://news.google.com/rss/')

    def test_arg_date(self):
        parsed = self.parser.parse_args(['--date','20220621'])
        self.assertEqual(parsed.date, 20220621)
  
if __name__ == '__main__':
    unittest.main()