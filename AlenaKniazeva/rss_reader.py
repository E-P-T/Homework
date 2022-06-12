"""
Pure Python command-line RSS reader.
"""

import argparse
import requests
import json
import sys
import logging
from logging import StreamHandler, Formatter
from bs4 import BeautifulSoup

version = '1.1'

def parse_input():
    """Parse a command line input"""
    parser = argparse.ArgumentParser(prog = 'rss-reader', description = 'Pure Python command-line RSS reader.')
    parser.add_argument('source', nargs = '?', default = '', help = 'RSS URL')
    parser.add_argument('--version', action ='version', help = 'Print version info',
        version='%(prog)s {}'.format (version))
    parser.add_argument('--json', help = 'Print result as JSON in stdout', action = "store_true")
    parser.add_argument('--verbose', help = 'Outputs verbose status messages', action = "store_true")
    parser.add_argument('--limit', type = int, help ='Limit news topics if this parameter provided')

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
    def __init__(self, content, limit, verbose):
        if verbose:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)

            handler = StreamHandler(stream=sys.stdout)
            handler.setLevel(logging.INFO)
            handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
            self.logger.addHandler(handler)

            self.logger.info('Logging started')  
        
        self.content = content
        self.feed = None
        self.news = []  # list of news articles
        self.parse(limit, verbose) # parses content and fill attributes "feed" and "news"
    
    def parse(self, limit, verbose):
        """Method to parse a content of a source page"""
        if verbose: self.logger.info('Parsing of sourse content...')
        soup = BeautifulSoup(self.content, "xml")
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
            pubdate = txt.find('pubDate').text
            
            a = connect(link)
            s = BeautifulSoup(a, "html.parser")
            meta_tag = s.find('meta', attrs={'property': 'og:description'})
            if meta_tag: 
                descr = meta_tag['content']
            else:
                descr = "No description provided"
        
            # create an Article object for each item
            article = {'title': title, 'pubdate': pubdate, 'link': link, 'description': descr}
            # append current article to a collection of news
            self.news.append(article)
            a_counter -= 1
            if not a_counter:
                break
        if verbose: self.logger.info('Parsing finished')
    
    def print_json(self):
        """Converts results to JSON and prints to stdout"""
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
    if args.source != '':
        content = connect(args.source)  # obtain a content of source page
        if content != None:
            my_feed = MyFeedParser(content, args.limit, args.verbose) # create an instance of MyFeedParser class
            if args.json:
                my_feed.print_json()
            else:
                print(my_feed)    
            if args.verbose: my_feed.logger.info('News are printed')
    if args.verbose: my_feed.logger.info('RSS-reader finished. Logging stopped')
        
if __name__ == '__main__':
    main()