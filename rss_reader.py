#!/usr/bin/env python3
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
import os.path
from dateutil import parser


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
        "--limit", help="Limit news topics if this parameter provided", type=int)
    parser.add_argument(
        "--date", help="Get news published on a specific date from cache for further processing.")
    args = parser.parse_args()
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


def check_storage():
    console_log('Checking for storage existance')
    if os.path.exists('local_storage.json'):
        console_log('Sorting and filtering')
        if os.stat("local_storage.json").st_size <= 2:
                with open('local_storage.json', 'w', encoding='utf-8') as writefile:
                    json.dump(list(), writefile, ensure_ascii=False, indent=4)
        else:

            with open('local_storage.json') as f:
                try:
                    f.read()
                except:
                    with open('local_storage.json', 'w', encoding='utf-8') as writefile:
                        json.dump(list(), writefile, ensure_ascii=False, indent=4)
    else:
        with open('local_storage.json', 'w', encoding='utf-8') as writefile:
            json.dump(list(), writefile, ensure_ascii=False, indent=4)





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
        item_list = []
        console_log(
            "Searching and collecting data from tags: ('title', 'pubDate', 'link', 'content', 'creator', 'enclosure', 'description')")
        for i in range(given_limit):
            items_json = {}
            news.append("\n")
            feed_json['Feed title'] = feed
            feed_json['Feed link'] = feed_link
            feed_json['Feed description:'] = feed_desc
            feed_json['Feed date:'] = feed_date
            item_date = items[i].pubDate.text
            d1 = str(parser.parse(item_date).strftime("%Y-%m-%d %H:%M:%S"))
            items_json.update({'Source': arguments.source})
            
            if items[i].title:
                title = items[i].title.text
                news.append(f"Title: {title}")
                items_json['News title:'] = title
            if items[i].pubDate:
                news.append(f"Date: {d1}")
                items_json['News date:'] = d1
            if items[i].link:
                link = items[i].link.text
                news.append(f"Link: {link}")
                links.append(f"{link}(link)")
                items_json['News link:'] = link
            if items[i].source:
                source = items[i].source['url']
                news.append(f"Source: {source}")
                items_json['News source:'] = source
            if items[i].content:
                image_link = items[i].content['url']
                news.append(f"Image_link: {image_link}")
                links.append(f"{image_link}(Image_link)")
                items_json['News image_link:'] = image_link
            if items[i].creator:
                creator = items[i].creator.text
                news.append(f"Creator: {creator}")
                items_json['News creator:'] = creator
            if items[i].enclosure:
                enclosure = items[i].enclosure['url']
                news.append(f"Enclosure: {enclosure}")
                items_json['News enclosure:'] = enclosure
            if items[i].description:
                description_decode = str(items[i].description)
                description = clean_desc(description_decode)
                news.append(f"\nDescription: {description}")
                items_json['News description:'] = description
            item_list.append(items_json)
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
        

        with open('local_storage.json', "r", encoding='utf-8') as file:
            data = json.loads(file.read())
            file.close()
        for item in item_list:
                if os.stat("local_storage.json").st_size == 2:
                    data.append(item)
                else:
                    if item not in data:
                        data.append(item)
        
        with open('local_storage.json', 'w', encoding='utf-8') as writefile:
            json.dump(data, writefile, ensure_ascii=False, indent=4)
            writefile.close()
        
        
        if arguments.json:
            """Function to convert feeds to json format."""
            item = {'Feed items': item_list}
            feed_json.update(item)
            json_object = json.dumps(feed_json, indent=4, ensure_ascii=False)
            print(json_object)


arguments = all_args()
def get_date():
    date_data = []
    given_date = arguments.date
    given_source = arguments.source
    given_limit = arguments.limit
    data_json = arguments.json
    
    with open('local_storage.json', "r", encoding='utf-8') as file:
        data = json.loads(file.read())
        amount = 0
        if given_source:
            
            for i in range(len(data)):
                day = str(parser.parse(data[i]['News date:']).strftime("%Y%m%d"))
                source = data[i]['Source']
                if given_date == day and given_source == source:
                    date_data.append(data[i])
                    amount += 1
                    if amount == given_limit:
                        break
            pprint(date_data)
            print('Total data found:',len(date_data))
        elif given_source is None:
            for i in range(len(data)):
                day = str(parser.parse(data[i]['News date:']).strftime("%Y%m%d"))
                if given_date == day:
                    date_data.append(data[i])
                    amount += 1
                    if amount == given_limit:
                        break
            if data_json:
                print(json.dumps(date_data, indent=4, ensure_ascii=False))
            else:
                pprint(date_data)
            print('Total data found:', len(date_data))
        else:
            print('No data found for given source')
        file.close()

verbose_true = True if arguments.verbose else False
# data_true = True if arguments.verbose else False


def read_defs():

    """Method to print obtained feeds to console."""
    if verbose_true:
        console_log('Verbose mode turned on')

    if arguments.json:
        console_log('Json mode turned on')

    if arguments.date:
        console_log('Date mode turned on')
        console_log(f'Given date is {arguments.date}')

    check_storage()
    if arguments.source:
        if arguments.date is None:
            get_data()
        

    if arguments.version:
        check_version()

    if arguments.date:
        get_date()
    


if __name__ == '__main__':
    read_defs()
