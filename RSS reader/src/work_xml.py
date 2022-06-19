from pprint import pprint

import logging
import importlib
import requests
from bs4 import BeautifulSoup
import json


def print_to_console(link, limit):
    try:
        xml_items = take_xml_items(link, limit)
        if xml_items['title']:
            print(f"Feed: {xml_items['title']}")

        for item in xml_items['items']:
            print(f"Title: {item.title.get_text()}")
            print(f"Date: {item.pubDate.get_text()}")
            print(f"Link: {item.link.get_text()}")
            print(f"Description: {item.description.get_text()}")

    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')


def take_xml_items(link, limit):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, features='xml')

        title = soup.find('channel').findChildren("title", recursive=False)  # out name feed
        if title:
            title = title[0].get_text()
        else:
            title = ''

        items = soup.findAll("item", limit=limit) #

        return {'title': title, 'items': items}
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')


def generate_json(link, limit):
    try:
        xml_items = take_xml_items(link, limit)

        for item in xml_items['items']:
            title = item.title.get_text()
            pubDate = item.pubDate.get_text()
            description = item.description.get_text()
            link = item.link.get_text()

            news = {
                'title': title,
                'pubDate': pubDate,
                'description': description,
                'link': link
            }

            # print(json.dumps(news, indent=4))
            # print(json.loads(news_dict))

            news_dict = json.dumps(news, indent=4)
            n = json.loads(news_dict)
            pprint(n)

    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')