from pprint import pprint
from dateutil import parser
from fpdf import fpdf
from bs4 import BeautifulSoup, Tag
import requests
import json
import logging
import os

system_path = os.path.dirname(os.path.abspath(__file__))
cache_file = os.path.join(system_path, 'cache.json')


def take_xml_items(link, limit):
    logging.info("Take xml items started")
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, features='xml')

        title = soup.find('channel').findChildren("title", recursive=False)  # out name feed
        if title:
            title = title[0].get_text()
        else:
            title = ''

        items_temp = soup.findAll("item", limit=limit)
        items = dict()
        key = 0
        for item in items_temp:
            items[key] = {'title': item.title.get_text(), 'pubDate': item.pubDate.get_text(),
                          'description': item.description.get_text(), 'link': item.link.get_text()}
            key += 1
        logging.info("Take xml items finished successfully")

        return {'title': title, 'items': items}
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Take xml items with exception")
        return False


def print_to_console(xml_items):
    logging.info("Print to console started")
    try:
        if 'title' in xml_items:
            print(f"Feed: {xml_items['title']}")

        for item in xml_items['items'].values():
            print(f"Title: {item['title']}")
            print(f"Date: {item['pubDate']}")
            print(f"Link: {item['link']}")
            print(f"Description: {item['description']}")

        logging.info("Print to console finished successfully")
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Print to console finished with exception")
        return False


def generate_json(xml_items):
    logging.info("Generate json started")
    try:
        for item in xml_items['items'].values():
            news = {
                'title': item['title'],
                'pubDate': item['pubDate'],
                'description': item['description'],
                'link': item['link']
            }

            # print(json.dumps(news, indent=4))
            # print(json.loads(news_dict))

            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(json.dumps(xmltodict.parse(my_xml)))

            news_dict = json.dumps(news, indent=4)
            n = json.loads(news_dict)
            pprint(n)
        logging.info("Generate json finished successfully")


    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Generate json finished with exception")
        return False


def read_cache_file():
    logging.info("Read cache file started")
    try:
        if os.path.exists(cache_file) and os.path.getsize(cache_file) > 0:
            with open(cache_file, 'r') as file:
                cache = json.load(file)
        else:
            logging.info("Read cache file: cache file is not exist")
            return dict()

        logging.info("Read cache file finished successfully")
        return cache
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Read cache file finished with exception")
        return False


def write_cache_file(cache):
    logging.info("Write cache file started")
    try:
        with open(cache_file, 'w+') as file:
            json.dump(cache, file, indent=4)

        logging.info("Write cache file finished successfully")
    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Write cache file finished with exception")
        return False


def set_cache_news(source, items):
    logging.info("Set cache news started")
    try:
        cache = read_cache_file()
        if not cache:
            cache = dict()

        for item in items.values():
            date = parser.parse(item['pubDate']).strftime('%Y%m%d')

            if date not in cache:
                cache[date] = dict()

            if source not in cache[date]:
                cache[date][source] = dict()

            cache[date][source][item['title']] = item

        write_cache_file(cache)
        logging.info("Set cache news finished successfully")

    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Set cache news finished with exception")
        return False


def get_cache_news(date, source=False):
    logging.info("Get cache news started")
    try:
        cache = read_cache_file()
        date = str(date)

        if date in cache:
            if source != False and source in cache[date]:
                items = dict()
                key = 0
                for item in cache[date][source].values():
                    items[key] = item
                    key += 1
                logging.info("Get cache news by date and source finished successfully")
                return {'items': items}
            elif source != False:
                print(f'News by date and source not found in cache')
                logging.info("News by date and source not found in cache")
                return False
            else:
                items = dict()
                key = 0
                for key_source in cache[date]:
                    for item in cache[date][key_source].values():
                        items[key] = item
                        key += 1
                logging.info("Get cache news by date finished successfully")
                return {'items': items}
        else:
            print(f'News by date not found in cache')
            logging.info("News by date not found in cache")
            return False

    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Get cache news finished with exception")
        return False


def generate_html(xml_items):
    logging.info("Generate html started")
    soup = BeautifulSoup()
    html = Tag(soup, name="html")
    body = Tag(soup, name="body")
    soup.append(html)
    html.append(body)

    try:
        for item in xml_items['items'].values():
            div = Tag(soup, name="div")

            h1 = Tag(soup, name="h1")
            h1.string = item['title']
            pPubDate = Tag(soup, name="p")
            pPubDate.string = item['pubDate']
            pdescription = Tag(soup, name="p")
            pdescription.string = item['description']
            plink = Tag(soup, name="p")
            plink.string = item['link']

            div.append(h1)
            div.append(pPubDate)
            div.append(pdescription)
            div.append(plink)

            body.append(div)

        with open("HTML_file.html", 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        logging.info("Generate html finished successfully")

        return soup

    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Generate html finished with exception")
        return False


def generate_pdf(xml_items):
    logging.info("Generate pdf started")
    # html = generate_html(xml_items)
    # pdf = pdfkit.from_file('HTML_file.html', 'PDF_file.pdf')

    try:
        pdf = fpdf.FPDF()
        pdf.add_font("Sans", style="", fname="Noto_Sans/NotoSans-Regular.ttf", uni=True)
        pdf.set_font("Sans", size=16)

        pdf.add_page()

        feed = xml_items['title']
        pdf.cell(200, 10, feed, ln=1, align='C')

        for item in xml_items['items'].values():
            # wrapped_title = '\n'.join(wrap(title, width=50)) # добавляет через каждые 50 символов \n
            # print(wrapped_title)

            pdf.cell(200, 10, 'NEWS', ln=1, align='C')
            pdf.multi_cell(200, 10, item['title'])
            pdf.multi_cell(200, 10, item['pubDate'])
            pdf.multi_cell(20, 10, item['description'])
            pdf.cell(20, 10, f"Link: {item['link']}", ln=1)

        pdf.output("PDF_file.pdf")
        logging.info("Generate pdf finished successfully")


    except Exception as e:
        print(f'This extraction job failed. See exceptions: {e}')
        logging.info("Generate pdf finished with exception")
        return False
