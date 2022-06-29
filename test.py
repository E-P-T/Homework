
import unittest
from rss_reader import all_args, check_url, clean_desc, get_data
from PDF_converter import convert_to_pdf
from HTML_converter import convert_to_html


class TestRssReader(unittest.TestCase):
    '''Testing the projcet`s main functions with Unittest module'''
    def setUp(self) -> None:
        
        self.text = '''&lt;p&gt;&lt;a href="https://auto.onliner.by/2022/06/27/v-uruche-ukreplyayut-most"&gt;&lt;img src="https://content.onliner.by/news/thumbnail/18dcaf08bb50e746d6e7f1b1007881e6.jpeg" alt="" 
        /&gt;&lt;/a&gt;&lt;/p&gt;&lt;p&gt;О том, что с путепроводом на пересечении пр. Независимости и ул. ;'''
        
        self.text2 = '''О том, что с путепроводом на пересечении пр. Независимости и ул. ;'''
        
        self.url = "https://news.yahoo.com/rss/"
        self.dataset = [{
            "Source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
            "News title:": "Shanghai Wrestles With Psychological Scars From Lockdown",
            "News date:": "2022-06-29 09:00:46",
            "News link:": "https://www.nytimes.com/2022/06/29/world/asia/shanghai-lockdown-china.html",
            "News image_link:": "https://static01.nyt.com/images/2022/06/28/world/00china-mentalhealth-01/00china-mentalhealth-01-moth.jpg",
            "News creator:": "Vivian Wang",
            "News description:": "The lockdown fueled anxiety, fear and depression among the city’s residents. Experts have warned that the mental health impact of the confinement will be long-lasting."
        }]

        self.convert_to_html = convert_to_html(self.dataset)
        self.convert_to_pdf = convert_to_pdf(self.dataset)
        self.url_validation = check_url(self.url)
        self.desc_clean = clean_desc(self.text)
        self.parser = all_args()

    def test_convet_to_html(self):
        '''This function test the html convertion. Berfore testing please run rss_reader url {your option} operation'''
        self.assertEqual(self.convert_to_html, 'test')

    def test_convert_to_pdf(self):
        '''Function for testing pdf convertion. This func requires images from local storage. If there none, the test wont work'''
        self.assertEqual(self.convert_to_pdf, 'test')

    def test_url_validation(self):
        '''Testing URL validation'''
        self.assertEqual(self.url_validation, True)

    def test_args_limit(self):
        '''Limit tester'''
        parsed = self.parser.parse_args(['--limit', '5'])
        self.assertEqual(parsed.limit, 5)

    def test_args_source(self):
        parsed = self.parser.parse_args(['https://news.google.com/rss/'])
        self.assertEqual(parsed.source, 'https://news.google.com/rss/')

    def test_args_date(self):
        '''Gets date as a str'''
        parsed = self.parser.parse_args(['--date', '20220630'])
        self.assertEqual(parsed.date[0], '20220630')

    def test_clean_desc(self):
        unittest.TestCase.maxDiff = None
        print(self.desc_clean)
        self.assertEqual(self.desc_clean, self.text2)

    def test_arg_source_news(self):
        test = get_data(self.parser.parse_args(['https://news.google.com/rss/', '--limit', '1']))
        self.assertEqual(test, True)

    def test_arg_source_news_json(self):
        test = get_data(self.parser.parse_args(
            ['https://news.google.com/rss/', '--limit', '1', '--json']))
        self.assertEqual(test, True)

    def test_arg_source_news_json_verbose(self):
        test = get_data(self.parser.parse_args(
            ['https://news.google.com/rss/', '--limit', '1', '--json', '--verbose']))
        self.assertEqual(test, True)

    def test_arg_news_date(self):
        test = get_data(self.parser.parse_args(
            ['https://news.google.com/rss/', '--limit', '1', '--date', '20220628' ]))
        self.assertEqual(test, True)

if __name__ == '__main__':
    unittest.main()
