import requests
from bs4 import BeautifulSoup
import json

def print_to_console(link, limit):
    try:
        xml_items = take_xml_items(link, limit)
        if xml_items['title']:
            print(f"Feed: {xml_items['title']}")

        for item in xml_items['items']:
            print(item.title.get_text())
            print(item.link.get_text())
            print(item.pubDate.get_text())
            print(item.description.get_text())



    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')


def take_xml_items(link, limit):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, features='xml')

        title = soup.find('channel').findChildren("title", recursive=False)
        if title:
            title = title[0].get_text()
        else:
            title = ''

        items = soup.findAll("item", limit=limit)

        return {'title': title, 'items': items}
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')


