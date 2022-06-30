import requests

import bs4

import json
import logging as log


class NewsBrain:
    def __init__(self, url, limit, js):
        self.url = url
        self.limit = limit
        self.json = js

    @staticmethod
    def create_logger():
        log_format = "%(asctime)s - %(message)s \n"
        log.basicConfig(level=log.DEBUG, format=log_format)
        logger = log.getLogger()
        return logger

    def get_rss_data(self):
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException:
            print("Bad request status. Check your internet connection or RSS link and try again.")
        else:
            page_code = response.text
            xml_data = bs4.BeautifulSoup(page_code, "xml")
            return xml_data

    @staticmethod
    def get_news_text(url):
        text = ""
        response = requests.get(url)
        root = bs4.BeautifulSoup(response.content, 'html.parser')
        article = root.select_one('article')
        list_of_paragraphs = article.find_all('p')
        try:
            text = list_of_paragraphs[0].text + list_of_paragraphs[1].text
        except IndexError:
            text = list_of_paragraphs[0].text
        finally:
            return text

    def get_news(self, xml_data, limit=None):
        data = {}
        news = xml_data.find_all("item")
        if len(news) == 0:
            print("News Not Found. Please, check you RSS URL.")
            return
        else:
            if limit is None or limit > len(news):
                limit = len(news)

            for i in range(limit):
                data["Feed"] = xml_data.channel.title.text
                data["Title"] = news[i].title.text
                data["Date"] = news[i].pubDate.text
                data["Link"] = news[i].link.text
                try:
                    description = news[i].description.text.replace("<p>", "").replace("[", "&").replace("<", "&")
                    data["Description"] = description[0:description.index("&")] + ".. READ MORE"
                except ValueError:
                    description = news[i].description.text
                    data["Description"] = description + ".. READ MORE"
                except AttributeError:
                    data["Description"] = self.get_news_text(data["Link"])
                try:
                    data["Image"] = news[i].find("media:content").get("url")
                except AttributeError:
                    try:
                        data["Image"] = xml_data.image.url.text
                    except AttributeError:
                        data["Image"] = "[IMAGE]"

                finally:
                    log.info(f"Printing {i + 1} news")
                    if not self.json:
                        self.print_data(data)
                    else:
                        js_data = {i + 1: data}
                        self.print_data(js_data)

    def print_data(self, data):
        if not self.json:
            for key, value in data.items():
                print(f"{key}: {value}")
            print("\n\n")
        else:
            json_format = json.dumps(data, ensure_ascii=False)
            print(f"{json_format}\n\n")

    def check_value_of_limit(self):
        try:
            lim = int(self.limit)
        except ValueError:
            print("Invalid value of 'LIMIT'. Must be integer")
            return 0
        except TypeError:
            return None
        else:
            return lim
