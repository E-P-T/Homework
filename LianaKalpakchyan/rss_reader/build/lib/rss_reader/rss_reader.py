#!/usr/bin/env python3
import os.path
import sys
import time
import json
import logging
import requests
import datetime
import dateparser
from bs4 import BeautifulSoup
from rss_argparser.rss_argparser import Argparser
from rss_save_into.rss_save_into import Converter


class Reader:
    """
    A class to implement the rss_reader logic

    ...

    Attributes
    ----------
    start : float
        The start time of the program is expressed in seconds since the epoch, in UTC.
        Will be used to calculate the working duration of the program
    args : list
        Arguments list received from CLI with rss_argparser package
    source : str
        Provided RSS link
    version : str
        The current iteration version of the program
    json : bool
        Flag for activating json mode
    verbose : bool
        Flag for activation verbose mode
    limit : int
        Number for quantity of selected news to print or to save
    date : int
        If provided only news having that date or fresher will be shown
    to_pdf : lst
        If mentioned only --to-pdf news will be converted into pdf and saved into a default folder for pdf files.
        If path is provided will be saved in that path.
    to_html : lst
        If mentioned only --to-html news will be converted into html and saved into a default folder for html files.
        If path is provided will be saved in that path.
    cashed_news : str
        File name for caching news

    Methods
    -------
    verbose_mode():
        Function to activate verbose mode
    get_xml():
        Functions gets xml page content with requests
    parse_link_page():
        Function searches by a specific news original page and finds description from it
    parse_xml():
        Function parses the xml page and separates every item with its details
    cashing_news():
        Functions caches all new news into json file
    reading_cache():
        Function reads news from cache
    json_mode():
        Function activates json mode
    items_in_terminal():
        Functions prints news items in terminal (shell)
    html_or_pdf():
        Function calls relevant functions to create html, pdf files or both
    main():
        Analyze the received data from rss_argparser and run the corresponding functions based on them
    """

    def __init__(self):
        self.start = time.time()
        self.args = Argparser().get_args()
        self.source = self.args.source
        self.version = Argparser().version
        self.json = self.args.json
        self.verbose = self.args.verbose
        self.limit = self.args.limit
        self.date = self.args.date
        self.to_pdf = self.args.to_pdf
        self.to_html = self.args.to_html
        self.cashed_news = 'cached_news.json'

    def verbose_mode(self):
        """
        This function activates verbose mode
        :returns None
        """
        if self.verbose:
            logging.basicConfig(
                stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
            logging.debug(f'VERBOSE MODE ACTIVATED')
            logging.debug(
                f'--version: {self.version}, --json: {self.json}, --verbose: {self.verbose}, --limit: {self.limit}, source: {self.source}')

    def get_xml(self):
        """
        Functions requests provided link and gets content of it
        :returns None or xml page text
        """
        if self.source is None:
            print('Please, make sure to provide RSS URL.')
            return None
        logging.debug('get_xml function is activated')
        attempt = 3
        while True:
            try:
                logging.debug(f'Waiting for response from {self.source}...')
                page_response = requests.get(self.source)
                if page_response.status_code == 200:
                    logging.debug(f'Page response status code: {page_response.status_code}')
                    logging.debug(f'get_xml function is completed')
                    return page_response.text
                else:
                    logging.debug(f'Unfortunately, no relevant page response from {self.source}')
                    logging.debug(f'get_xml function is completed')
                    return None
            except:
                logging.debug('Oops, unable to connect.')
                print(f'No worries, will check again in 5 seconds.')
                print(f'If there are no changes it will be checked {attempt} more {"time" if attempt == 1 else "times"}')
                time.sleep(5)
            attempt -= 1
            if attempt < 1:
                print(f'{self.source} is can\'t be connected. Check the url address or internet connection.')
                logging.debug('Program has stopped to working: Connection Error')
                return None

    def parse_link_page(self, description_link):
        """
        Function searches by a specific news original page and finds description from it
        :param description_link
        :returns description if found
        """
        logging.debug('parse_link_page function is activated')
        page_html = self.get_xml()
        if page_html is None:
            return 'No description'
        logging.debug(f'Activating BeautifulSoup for: {description_link}')
        soup = BeautifulSoup(page_html, 'lxml')
        all_p = soup.find_all('p')
        description = ''
        for p in all_p[:3]:
            if p.text.split() != '\n':
                description += p.text
        logging.debug('parse_link_page is completed')
        return description

    def parse_xml(self, xml_text):
        """
        Function parses the xml page and separates every item with its details, exits if it is invalid RSS page
        :param xml_text
        :returns page_title, all_items
        """
        logging.debug('get_xml function is activated')
        logging.debug('Activating BeautifulSoup')
        soup = BeautifulSoup(xml_text, 'xml')
        if not soup.find('channel'):
            print('Invalid RSS page')
            exit()
        else:
            try:
                logging.debug('Looking for page "title" tag')
                page_title = soup.find('title').text
            except:
                logging.debug('"title" tag is unavailable')
                page_title = 'No page title'
            all_items = []
            logging.debug('Collecting and analyzing items')
            xml_items = soup.find_all('item')
            if self.limit < 0:
                self.limit = len(xml_items)
            for item in xml_items[:self.limit]:
                logging.debug('Generating each item details')
                xml_item = {"title": item.find("title").text.lstrip(), "link": item.find("link").text,
                              "pubDate": item.find("pubDate").string}
                try:
                    try:
                        xml_item["image"] = item.find('enclosure')["url"]
                    except:
                        xml_item["image"] = item.find('media:content')["url"]
                except:
                    xml_item["image"] = 'No image found'

                try:
                    xml_item["description"] = item.find("description").text
                except:
                    logging.debug('Evoking parse_link_page function')
                    description = self.parse_link_page(xml_item["link"])
                    if description is not None:
                        xml_item["description"] = description
                    else:
                        xml_item["description"] = "No description"

                logging.debug(f'Saving {xml_item} to "all_items" dict')
                all_items.append(xml_item)

            logging.debug('parse_xml function is completed')
            return page_title, all_items

    def cashing_news(self, page_title, page_items):
        """
        Function receives page_title, page_items and caches them in cached_news.txt file
        :params page_title, page_items
        :returns None
        """
        logging.debug('cashing_news function is activated')
        if not self.source.endswith('/'):
            self.source += '/'

        json_content = ''
        if os.path.exists(self.cashed_news):
            logging.debug(f'Generating "{self.cashed_news}" file for news caching')
            with open(f'{self.cashed_news}', 'r', encoding='utf-8') as json_file:
                json_content = json.loads(json_file.read())

        with open(self.cashed_news, 'w', encoding='utf-8') as file:
            cached_items = [] if json_content == '' else json_content
            news_dict = dict()
            news_dict["caching_date"] = str(datetime.datetime.now()).replace('-', '/')
            news_dict["news_feed"] = page_title
            news_dict["news_items"] = []
            for item in page_items:
                unique_news = {}
                item_pub_date = dateparser.parse(item['pubDate'])
                item_normal_date = item_pub_date.strftime('%Y%m%d')
                if str(item) not in str(json_content):
                    logging.debug(f'New item found! Adding it to "{self.cashed_news}"')
                    unique_news["date"] = item_normal_date
                    unique_news["link"] = self.source
                    unique_news["item_details"] = item
                    news_dict["news_items"].append(unique_news)
                else:
                    logging.debug(f'Item exists in "{self.cashed_news}". No need to add')

            cached_items.append(news_dict)
            json.dump(cached_items, file, ensure_ascii=False, indent=4)

    def reading_cache(self):
        """
        Function reads news for the specified date or/and resource from cached_news.txt file
        :returns list with items (if there is a need to convert into html or pdf)
        """
        logging.debug('"reading_cache" function is activated')
        no_data = True
        if self.source is not None and not self.source.endswith('/'):
            self.source += '/'
        try:
            with open(f'{self.cashed_news}', 'r', encoding='utf-8') as file:
                logging.debug(f'Open file "{self.cashed_news}". Params: {self.date}, {self.source}, {self.limit}')
                for_news = f'For source: {self.source}' if self.source else ''
                print('Reading cache file...')
                print(for_news)
                json_content = json.loads(file.read())
                limit = 0
                i = 0
                items_to_convert = []
                for fetched_news in json_content:
                    for sep_news in fetched_news['news_items']:
                        source = True if self.source is None else sep_news['link'] == self.source
                        if int(sep_news['date']) >= int(self.date) and source:
                            item = sep_news['item_details']
                            items_to_convert.append(item)
                            print('*'*100)
                            logging.debug(f'Printing #{i + 1} element:')
                            print(f'Number {i + 1}')
                            print(f'\tTitle: {item["title"]}')
                            print(f'\tDate: {item["pubDate"]}')
                            print(f'\tLink: {item["link"]}')
                            print(f'\tDescription: {item["description"]}')
                            print(f'\tImage: {item["image"]}')
                            logging.debug(f'End Printing number {i + 1} element:')
                            print('*'*100)
                            limit += 1
                            i += 1
                            no_data = False
                        if limit == self.limit:
                            break
                if no_data:
                    logging.debug(f'Nothing found found for date: {self.date}')
                    print(f'Error! Nothing found for date: {self.date}')
                return items_to_convert
        except FileNotFoundError as e:
            logging.debug(f'{e} nothing is cached yet.')
            print(f'Use rss-reader without --date argument at first then with --date, so there will ba cached news.')

    @staticmethod
    def json_mode(items, title=''):
        """
        This functions prints news in json format
        """
        logging.debug('"json_monde" function is activated')
        print(title, '\n', json.dumps(items, indent=4, ensure_ascii=False, sort_keys=False))

    @staticmethod
    def items_in_terminal(title, items):
        """
        This function receives title for xml page its items and print in terminal (shell)
        :params title, items
        :returns None
        """
        logging.debug('"items_in_terminal" function is activated')
        print(f'\nFeed: {title}\n')
        for i, item in enumerate(items):
            print('*' * 100)
            logging.debug(f'Printing #{i + 1} element:')
            print(f'Number {i + 1}')
            print(f'\tTitle: {item["title"]}')
            print(f'\tDate: {item["pubDate"]}')
            print(f'\tLink: {item["link"]}')
            print(f'\tDescription: {item["description"]}')
            print(f'\tImage: {item["image"]}')
            logging.debug(f'End Printing number {i + 1} element:')
            print('*' * 100)
        logging.debug('"items_in_terminal" function is completed')

    def html_or_pdf(self, content):
        """
        This function forwards completed html template to html creating function, to pdf creating function or to both
        :param content
        :returns None
        """
        logging.debug(f'to_html = {self.to_html} , to_pdf = {self.to_pdf}')
        converter = Converter()
        converter.make_html_template(content)
        if self.to_html is not None:
            logging.debug(f'Converting to_html = {self.to_html}')
            path_to_save = self.to_html[0] if self.to_html else 'html_files'
            converter.convert_to_html(path_to_save)
        if self.to_pdf is not None:
            logging.debug(f'Converting to_pdf = {self.to_pdf}')
            path_to_save = self.to_pdf[0] if self.to_pdf else 'pdf_files'
            converter.convert_to_pdf(path_to_save)

    def main(self):
        """
        This method is for analyzing arguments from rss_argparser.
        Evokes the corresponding functions based on arguments' requirements.
        """
        self.verbose_mode()
        logging.debug('Evoking get_xml function')
        xml_text = self.get_xml() if self.source else None

        if xml_text is not None and self.date is None:
            logging.debug('Evoking parse_xml function')
            title, items = self.parse_xml(xml_text)
            if not items:
                logging.debug('No item found')
                print(f"{self.source} doesn't have any RSS items, or --limit is set up as 0")
            elif items:
                logging.debug(f'Start caching to "{self.cashed_news}"')
                self.cashing_news(title, items)

            if self.to_html is not None or self.to_pdf is not None:
                self.html_or_pdf(items)

            if self.json:
                logging.debug('Activating printing items in JSON format')
                self.json_mode(items, title)
            else:
                logging.debug('Activating printing items in terminal')
                self.items_in_terminal(title, items)

        elif self.date is not None:
            cached_news_dated = self.reading_cache()
            if self.to_html is not None or self.to_pdf is not None:
                self.html_or_pdf(cached_news_dated)

            elif self.json:
                self.json_mode(cached_news_dated)

            else:
                self.reading_cache()

        elif self.date is None:
            logging.debug(f'{self.source} is empty.')
            print(f'Invalid RSS link: {self.source}, please, provide valid RSS link.')
        print(f'Thank you for using our RSS reader. Program is done time spent: {time.time() - self.start}s.')


def main():
    Reader().main()


if __name__ == '__main__':
    main()



