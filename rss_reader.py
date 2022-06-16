"""The main workspace for RSS_reader application"""
import datetime
import argparse
import html
import validators
import requests
import json
from py_console import console
from pprint import pprint
from bs4 import BeautifulSoup


def datetime_now():
    return datetime.datetime.now().astimezone().strftime('%Y.%m.%d %H:%M:%S')


def console_log(msg):
    if verbose_true:
        console.info(f'{datetime_now()} - {msg}', showTime=False)


def console_error(msg):
    console.error(f'{datetime_now()} - {msg}', showTime=False)


def all_args():
    parser = argparse.ArgumentParser(
        description="Pure Python command-line RSS reader.")
    parser.add_argument("source", help="RSS URL", nargs="?")
    parser.add_argument(
        "--version", help="Print version info", action="store_true")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument(
        "--verbose", help="Output verbose status messages", action="store_true")
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", nargs="?", type=int)
    parser.add_argument(
        "-d", "--date", help="Get news published on a specific date from cache for further processing.",)
    args = parser.parse_args()
    print(args)
    return args


def check_version():
    """Method for revealing current version of the utility"""
    print("Version 2.1")


def clean_desc(description):
    '''Function for decoding some part of feed item'''
    decoded_string = html.unescape(description)
    soup = BeautifulSoup(decoded_string, features="lxml")
    return soup.get_text()


def check_url(url):
    '''Method for checking url`s validation and availability'''
    console_log(f'Checking for validation of URL: {url}')
    if validators.url(str(url)):
        console_log('URL validation completed')
        try:
            console_log('Requesting data from URL')
            if requests.get(url).status_code == 200:
                console_log(
                    'Request completed successfully. Reading and decoding request data')
                return True
            console_error('URL is not responding')
            return False
        except:
            console_error(f'This URL can`t be reached ')
            return False
    console_error(f'URL validation error')
    return False


def get_data():
    """Collectiong the major part of an Feed and its` items."""
    given_limit = arguments.limit
    console_log(f'Limit is given {given_limit}')
    if check_url(arguments.source):
        console_log(f'Parsing data from URL')
        ready_url = requests.get(arguments.source)
        soup = BeautifulSoup(ready_url.content, features="xml")
        items = soup.find_all('item')
        feeds = soup.find('channel')
        feed = feeds.find_all('title')[0].text
        feed_link = soup.find_all('link')[0].text
        feed_desc = soup.find_all('description')[0].text
        feed_date = soup.find_all('pubDate')[0].text
        if arguments.limit:

            if given_limit >= len(items):
                given_limit = len(items)
        else:
            console_log(f'Limit is not given')
            given_limit = len(items)
        news = []
        links = []
        feed_json = {}
        items_json = {}
        console_log(
            "Searching and collecting data from tags: ('title', 'pubDate', 'link', 'content', 'creator', 'enclosure', 'description')")
        for i in range(given_limit):
            news.append("\n")
            feed_json['Feed title'] = f'{feed}'
            feed_json['Feed link'] = f'{feed_link}'
            feed_json['Feed description:'] = f'{feed_desc}'
            feed_json['Feed date:'] = f'{feed_date}'
            item_date = items[i].pubDate.text
            d1 = str(datetime.datetime.strptime(
                f"{item_date}", "%Y-%m-%dT%H:%M:%SZ"))
            items_json[d1] = {}
            if items[i].title:
                title = items[i].title.text
                news.append(f"Title: {title}")
                items_json[d1]['News title:'] = f'{title}'
            if items[i].pubDate:
                date = items[i].pubDate.text
                news.append(f"Date: {date}")
                items_json[d1]['News date:'] = f'{d1}'
            if items[i].link:
                link = items[i].link.text
                news.append(f"Link: {link}")
                links.append(f"{link}(link)")
                items_json[d1]['News link:'] = f'{link}'
            if items[i].source:
                source = items[i].source['url']
                news.append(f"Source: {source}")
                items_json[d1]['News source:'] = f'{source}'
            if items[i].content:
                image_link = items[i].content['url']
                news.append(f"Image_link: {image_link}")
                links.append(f"{image_link}(Image_link)")
                items_json[d1]['News image_link:'] = f'{image_link}'
            if items[i].creator:
                creator = items[i].creator.text
                news.append(f"Creator: {creator}")
                items_json[d1]['News creator:'] = f'{creator}'
            if items[i].enclosure:
                enclosure = items[i].enclosure['url']
                news.append(f"Enclosure: {enclosure}")
                items_json[d1]['News enclosure:'] = f'{enclosure}'
            if items[i].description:
                description_decode = str(items[i].description)
                description = clean_desc(description_decode)
                news.append(f"\nDescription: {description}")
                items_json[d1]['News description:'] = f'{description}'

        console_log('Data successfully collected')
        console_log(
            f'Organising and preparing datas according to given limit {given_limit}')
        if arguments.json:
            console_log('Converting data into JSON')
        console_log('Printing all collected information ')

        print(f'\nFeed: {feed}')

        for new in news:
            print(new)

        print('\nLinks:')
        for i in range(len(links)):
            print(f'[{i+1}]: {links[i]}')
        print("\n")

        if arguments.json:
            """Function to convert feeds to json format."""
            item = {'Feed items': items_json}
            feed_json.update(item)
            pprint(json.dump(feed_json), sort_dicts=False,)


arguments = all_args()

verbose_true = True if arguments.verbose else False


def read_defs():
    """Method to print obtained feeds to console."""
    if verbose_true:
        console_log('Verbose mode turned on')

    if arguments.json:
        console_log('Json mode turned on')

    if arguments.source:
        get_data()

    if arguments.version:
        check_version()


if __name__ == '__main__':
    read_defs()
