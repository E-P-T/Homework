#!/usr/bin/env python3
"""The main workspace for RSS_reader application"""
import datetime
import argparse
import html
import validators
import json
from py_console import console 
from pprint import pprint #PrettyPrint function
from bs4 import BeautifulSoup
import os.path
from dateutil import parser as pr
from HTML_converter import convert_to_html #HTML converter function
import requests  # request img from web
import shutil  # save img locally
from PDF_converter import convert_to_pdf  # PDF converter function

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
        "--date", help="Get news published on a specific date from cache for further processing.", nargs="*")
    parser.add_argument(
        "--to-html", help="Convert news to .html format and save it into 'html_convert' directory with 'local datetime' name", action='store_true')
    parser.add_argument(
        "--to-pdf", help="Convert news to .pdf format and save it into 'pdf_convert' directory with 'local datetime' name", action='store_true')
    return parser




def datetime_now():
    '''Method of defining current datetime'''
    return datetime.datetime.now().astimezone().strftime('%Y.%m.%d %H:%M:%S')

def console_log(msg):
    '''Function for printing verbose log messages'''
    if verbose_true:
        console.info(f'{datetime_now()} - {msg}', showTime=False)

def console_error(msg):
    '''Function for printing verbsoe error messages'''
    console.error(f'{datetime_now()} - {msg}', showTime=False)

def check_version():
    """Method for revealing current version of the utility"""
    print("Version 4.3")

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


argument = all_args().parse_args()
verbose_true = True if argument.verbose else False

def check_storage():
    '''Method of checking for existance of storage, if the storage is not found, the function will automatically create one'''
    console_log('Checking for storage existance')
    if os.path.exists('local_storage.json'):
        console_log('Scanning the contaminants of the file')
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
        console_log('Local storage is not found')
        console_log("Creating local storage 'local_storage.json'")
        with open('local_storage.json', 'w', encoding='utf-8') as writefile:
            json.dump(list(), writefile, ensure_ascii=False, indent=4)

def get_data(arguments=None):
    print(arguments)
    """The main function for collectiong the major part of an Feed and its` items."""
    try:
        if arguments is None:
            arguments = all_args().parse_args()
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
                d1 = str(pr.parse(item_date).strftime("%Y-%m-%d %H:%M:%S"))
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

            img_folder='img_storage'
            if os.path.exists(img_folder):
                pass
            else:
                os.mkdir(img_folder)
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
            

            for item in item_list:
                if 'News image_link:' in item:
                    img_name=item['News image_link:'].split('/')[-1]+'.jpeg'
                    res = requests.get(item['News image_link:'], stream=True)
                    if res.status_code == 200:
                        with open(f'{img_folder}/{img_name}', 'wb') as f:
                            shutil.copyfileobj(res.raw, f)

            if arguments.to_html:
                """Function to convert feeds to html format."""
                data_dicts_html = []
                for data in item_list:
                    data_dicts_html.append(data)
                convert_to_html(data_dicts_html)
                console_log("The result for given date successfully convert into html")
                
            if arguments.to_pdf:
                """Function to convert feeds to pdf format."""
                data_dicts_pdf = []
                for data in item_list:
                    data_dicts_pdf.append(data)
                convert_to_pdf(data_dicts_pdf)
                console_log("The result for given date successfully convert into pdf")
        return True
    except:
        return False
    

def get_date(arguments = None):
    '''Distrubuting collected data from local storage "local_storage.json" for different functions according to required options'''
    try:
        if arguments is None:
            arguments = all_args().parse_args()
        date_data = []
        if len(arguments.date)>0:
            given_date = arguments.date[0]
        else:
            given_date = arguments.date
        given_source = arguments.source
        given_limit = arguments.limit
        data_json = arguments.json
        console_log('Reading the file')
        with open('local_storage.json', "r", encoding='utf-8') as file:
            data = json.loads(file.read())
            if given_source:
                console_log(f'Searching data with cource {given_source}')
                console_log('Converting collected data into json')
                console_log('Collecting data according to given requirements: [source], [limit], [date], [json]')
                console_log('Printing final result')
                if arguments.to_html and arguments.to_pdf:
                    console_log('Converting result into html')
                    console_log('Converting result into pdf')
                elif arguments.to_pdf:
                    console_log('Converting result into pdf')
                elif arguments.to_html:
                    console_log('Converting result into html')
                for item in data:
                    day = str(pr.parse(item['News date:']).strftime("%Y%m%d"))
                    source = item['Source']
                    if len(given_date)==0 and given_source == source:
                        if given_source == source:
                            date_data.append(item)
                    elif len(given_date) == 0 and given_source is None:
                        date_data.append(item)
                    elif given_date == day:
                        if given_source == source:
                            date_data.append(item)
                if data_json:
                    
                    if len(date_data[:given_limit]) > 0:
                        if arguments.to_html:
                            
                            convert_to_html(date_data[:given_limit], arguments.date)
                        elif arguments.to_pdf:
                            
                            convert_to_pdf(date_data[:given_limit], arguments.date)
                        else:
                            print(json.dumps(
                                date_data[:given_limit], indent=4, ensure_ascii=False))
                            print('Total data found:', len(date_data[:given_limit]))
                    else:
                        if verbose_true:
                            console_error('No data found')
                        else:
                            print('No data found')
                
                elif arguments.to_html:
                    
                    convert_to_html(date_data[:given_limit], arguments.date)
                elif arguments.to_pdf:
                
                    convert_to_pdf(date_data[:given_limit], arguments.date)
                for i in date_data[:given_limit]:
                    pprint(i)
                    print('Total data found:', len(date_data[:given_limit]))
            elif given_source is None:
                console_log('Searching source is not given. Looking up local storage with given date')
                console_log('Converting collected data into json')
                console_log('Collecting data according to given requirements: [limit], [date], [json]')
                console_log('Printing final result')
                if arguments.to_html and arguments.to_pdf:
                    console_log('Converting result into html')
                    console_log('Converting result into pdf')
                elif arguments.to_pdf:
                    console_log('Converting result into pdf')
                elif arguments.to_html:
                    console_log('Converting result into html')
                for item in data:
                    day = str(pr.parse(item['News date:']).strftime("%Y%m%d"))
                    source = item['Source']
                    if given_date == day:
                        date_data.append(item)
                    elif len(given_date)==0:
                        date_data.append(item)
                if data_json:
                    if len(date_data[:given_limit]) > 0:
                        if arguments.to_html:
                            convert_to_html(date_data[:given_limit], arguments.date)
                        elif arguments.to_pdf:
                            convert_to_pdf(date_data[:given_limit], arguments.date)
                        else:
                            print(json.dumps(
                                date_data[:given_limit], indent=4, ensure_ascii=False))
                            print('Total data found:', len(date_data[:given_limit]))
                    else:
                        if verbose_true:
                            console_error('No data found')
                        else:
                            print('No data found')
                else:
                    if arguments.to_html:
                        console_log('Converting result into html')
                        if arguments.to_pdf:
                            console_log('Converting result into pdf')
                        convert_to_html(date_data[:given_limit], arguments.date)
                    elif arguments.to_pdf:
                        if arguments.to_html:
                            console_log('Converting result into html')
                        console_log('Converting result into pdf')
                        convert_to_pdf(date_data[:given_limit], arguments.date)
                    for i in date_data[:given_limit]:
                        pprint(i)
                        print('Total data found:', len(date_data[:given_limit]))
                    
            file.close()
        return True
    except:
        return False


def read_defs():
    """Method to print obtained feeds to console."""
    if verbose_true:
        console_log('Verbose mode turned on')
    if argument.json:
        console_log('Json mode turned on')
    check_storage()
    if argument.date is None and argument.source:
        get_data()
    else:
        if argument.date or len(argument.date) == 0:
            console_log('Date mode turned on')
            console_log(f'Given date is {argument.date}')
            get_date()
    if argument.version:
        check_version()



if __name__ == '__main__':
    read_defs()
