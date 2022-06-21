""" Pure Python command-line RSS reader."""

import argparse
from unittest import result
import requests
import json
import sys
import logging
import datetime
import os
import jsonlines     
from logging import StreamHandler, Formatter
from bs4 import BeautifulSoup
from dateutil import parser             


version = '3.1'


def parse_input():
    """Parse a command line input"""

    parser = argparse.ArgumentParser(prog = 'rss-reader', description = 'Pure Python command-line RSS reader.')
    parser.add_argument('source', nargs = '?', default = '', help = 'RSS URL')
    parser.add_argument(
        '--version', action ='version', help = 'Print version info', version='%(prog)s {}'.format (version))
    parser.add_argument('--json', help = 'Print result as JSON in stdout', action = "store_true")
    parser.add_argument('--verbose', help = 'Outputs verbose status messages', action = "store_true")
    parser.add_argument('--limit', type = int, help ='Limit news topics if this parameter provided')
    parser.add_argument(
        '--date', type = lambda s: datetime.datetime.strptime(s, '%Y%m%d'), 
        help = 'Print result from a cash for a given date')

    args, rest = parser.parse_known_args()
    if rest:
        print("Error: Wrong input! Unexpected arguments: " + str(rest))
    else:
        return args


def connect(path):
    """Send a get-request and obtain a content of a response in unicode"""
    try:
        response = requests.get(url = path, timeout = 5)
    except requests.exceptions.ConnectTimeout or requests.exceptions.ReadTimeout:
        print("Error: Timeout occured. Try to connect later.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: DNS lookup failed.")
        return None
    except requests.exceptions.HTTPError:
        print("Error: HTTP error occured.")
        return None
    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL. Check the entered argument 'source'")
        return None
    except requests.RequestException:
        print("Error: Unknown request exception occured.")
        return None
    else:
        return response.text


class MyFeedParser:
    """Class for a created feed-parser"""

    def __init__(self, verbose):
        if verbose:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)

            handler = StreamHandler(stream=sys.stdout)
            handler.setLevel(logging.INFO)
            handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
            self.logger.addHandler(handler)

            self.logger.info('Logging started')  
        
        self.feed = None
        self.news = []  # list of news articles
    
    def parse(self, content, limit, verbose, source):
        """Method to parse a content of a source page"""
        if verbose: self.logger.info('Parsing of sourse content...')
        soup = BeautifulSoup(content, "xml")
        self.feed = soup.title.text
        articles = soup.findAll('item')
        a_num = len(articles)
        if limit != None:
            if limit < a_num:
                a_counter = limit
            else:
                a_counter = a_num
                if verbose: self.logger.warning('All available content of a feed will be read')
        else:
            a_counter = a_num
            if verbose: self.logger.warning('All available content of a feed will be read')
        if verbose: self.logger.info('Reading news...')
        for txt in articles:
            title = txt.find('title').text
            link = txt.find('link').text
            pubdate = parser.parse(txt.find('pubDate').text) # parses pubDate to datetime object
            # connect to link and psrse description from an initial web-page                        
            a = connect(link)
            s = BeautifulSoup(a, "html.parser")
            meta_tag = s.find('meta', attrs={'property': 'og:description'})
            if meta_tag: 
                descr = meta_tag['content']
            else:
                descr = "No description provided"
        
            # create an Article object for each item
            article = {'title': title, 'pubdate': pubdate.isoformat(), 'link': link, 'description': descr}
            # append current article to a collection of news
            self.news.append(article)

            # send article to cash file
            article['feed'] = self.feed
            article['source'] = source
            with open('dates.json', 'r') as f:
                mydates = json.load(f)
            cur_data = str(pubdate.date())
            if cur_data in mydates:
                filepath = os.path.abspath(mydates[cur_data])
                with jsonlines.open(filepath, mode='a') as writer:
                    writer.write(article)
            else:
                mydates[cur_data] = os.path.join(os.path.abspath('cashed_feeds'), cur_data+'.jsonl')
                with open('dates.json', 'w') as f:
                    json.dump(mydates, f) 
                with jsonlines.open(mydates[cur_data], mode='w') as writer:
                    writer.write(article)

            a_counter -= 1
            if not a_counter:
                break
        if verbose: self.logger.info('Parsing finished')
    
    def cash_read(self, my_date, my_source, verbose, limit):
        """Reading of cashed news"""

        if verbose: self.logger.info('Reading available dates from cash')
        with open('dates.json', 'r') as f:
            mydates = json.load(f)
        cur_date = str(my_date.date())
        if cur_date in mydates:
            if verbose: self.logger.info('Reading news from cash for the entered date...') 
            with jsonlines.open(mydates[cur_date]) as reader:
                if my_source != '':
                    flag = 0 # Flag to check if cashed news for entered date are available for entered feed
                    for obj in reader:
                        if obj['source'] == my_source and flag == 0:
                            self.feed = obj['feed']
                            self.news.append(obj)
                            flag = 1
                        elif obj['source'] == my_source and flag == 1:
                            self.news.append(obj)
                        if limit != None:
                            if len(self.news) > limit:
                                self.news = self.news[len(self.news)-limit:]
                    if verbose: self.logger.info('Reading of news from cash is finished')
                    if flag == 0: 
                        print("Error: There are no cashed news for the entered date and feed.")
                        sys.exit()
                else:
                    #read all cashed articles for the entered date
                    for obj in reader:
                        self.news.append(obj)
                    if limit != None:
                        if len(self.news) > limit:
                            self.news = self.news[len(self.news)-limit:]
                    # create a list of feeds available for the entered date
                    list_feeds = [a['feed'] for a in self.news]
                    unique_feeds = set(list_feeds)
                    self.feed = ", ".join(unique_feeds)
                    if verbose: self.logger.info('Reading of news from cash is finished')
        else:
            print("Error: There are no cashed news for the entered date.")
            sys.exit()

    def print_json(self):
        """Converts results to JSON and prints to stdout"""
        news_cut = []
        for new in self.news:
            news_cut.append(
                {'title': new['title'], 'pubdate': new['pubdate'], 
                'link': new['link'], 'description': new['description']})
        d = {'feed' : self.feed, 'news' : self.news}
        print(json.dumps(d, ensure_ascii = False, indent = 2))

    def __str__(self):
        result = '\n' + "Feed: {}".format(self.feed) + '\n' + '\n'
        for n in self.news:
            result += "Title: {}".format(n['title']) + '\n'
            result += "Date: {}".format(n['pubdate']) + '\n'
            result += "Link: {}".format(n['link']) + '\n'
            result += "Description: {}".format(n['description']) + '\n'+ '\n'
        return result


def main():
    args = parse_input()  # parsing of command line input

    # create an instance of MyFeedParser class
    my_feed = MyFeedParser(args.verbose) 

    if args.date:
        my_feed.cash_read(args.date, args.source, args.verbose, args.limit)
        if args.json:
            my_feed.print_json()
        else:
            print(my_feed)    
        if args.verbose: my_feed.logger.info('News are printed')
    else: 
        if args.source != '':
            content = connect(args.source)  # obtain a content of source page
            if content != None:
                # create an instance of MyFeedParser class
                my_feed.parse(content, args.limit, args.verbose, args.source) 
                if args.json:
                    my_feed.print_json()
                else:
                    print(my_feed)    
                if args.verbose: my_feed.logger.info('News are printed')
    if args.verbose: my_feed.logger.info('RSS-reader finished. Logging stopped')     


if __name__ == '__main__':
    main()