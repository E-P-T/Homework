import requests
import pandas
import bs4
import html
import json
import logging as log
from datetime import datetime
from pathlib import Path
work_dir = Path(__file__).absolute().parent


class NewsBrain:
    def __init__(self, url, limit, js, date):
        self.url = url
        self.limit = limit
        self.json = js
        self.date = date
        try:
            self.cache = pandas.read_csv(work_dir / "cache.csv")
        except FileNotFoundError:
            self.cache = pandas.DataFrame(columns=["Source", "Feed", "Title", "Date", "Link", "Description", "Image"])
        except pandas.errors.EmptyDataError:
            self.cache = pandas.DataFrame(columns=["Source", "Feed", "Title", "Date", "Link", "Description", "Image"])

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

        response = requests.get(url)
        root = bs4.BeautifulSoup(response.content, 'html.parser')
        article = root.select_one('article')
        if article is None:
            text = "Something went wrong.. Article not found.. Please, click on the link to read the news"
        else:
            list_of_paragraphs = article.find_all('p')
            try:
                text = list_of_paragraphs[0].text + list_of_paragraphs[1].text
            except IndexError:
                text = list_of_paragraphs[0].text

        return text

    def get_news(self, xml_data, limit=None):
        data = {}
        list_of_news = []

        news = xml_data.find_all("item")
        if len(news) == 0:
            print("News Not Found. Please, check you RSS URL.")
            return
        else:
            if limit is None or limit > len(news):
                limit = len(news)
            elif limit <= 0:
                print("News limit must be positive number")
                return
            for i in range(limit):
                data["Source"] = self.url
                try:
                    data["Feed"] = xml_data.channel.title.text
                except AttributeError:
                    data["Feed"] = "Feed not found.."
                try:
                    data["Title"] = html.unescape(news[i].title.text)
                except AttributeError:
                    data["Title"] = "Title not found.."
                try:
                    data["Date"] = news[i].pubDate.text
                except AttributeError:
                    data["Date"] = "Date not found"
                try:
                    data["Link"] = news[i].link.text
                except AttributeError:
                    data["Link"] = "Link not found.."
                try:
                    desc = news[i].find("description").text
                    soup = bs4.BeautifulSoup(desc, "html.parser")
                    data["Description"] = soup.p.text
                    if data["Description"] == "":
                        data["Description"] = xml_data.channel.description.text
                except AttributeError:
                    try:
                        desc = news[i].find("description").text
                        if '<' not in desc:
                            data["Description"] = news[i].find("description").text
                        else:
                            data["Description"] = xml_data.channel.description.text
                    except AttributeError:
                        data["Description"] = self.get_news_text(data["Link"])
                try:
                    data["Image"] = news[i].find("media:content").get("url")
                except AttributeError:
                    try:
                        data["Image"] = xml_data.image.url.text
                    except AttributeError:
                        data["Image"] = "Image not found"
                finally:
                    cached_d = {key: value for key, value in data.items()}
                    list_of_news.append(cached_d)
                    log.info(f"Printing {i + 1} new")
                    if not self.json:
                        self.print_data(data)
                    else:
                        js_data = {i + 1: data}
                        self.print_data(js_data)
            cached_news = pandas.DataFrame(list_of_news)
            cache_merge = pandas.merge(self.cache, cached_news, how="outer").drop_duplicates(subset="Title")
            cache_merge.to_csv(work_dir / "cache.csv", index=False)

    def print_data(self, data):
        if not self.json:
            for key, value in data.items():
                print(f"{key}: {value}")
            print("\n\n")
        else:
            json_format = json.dumps(data, ensure_ascii=False, indent=4)
            print(f"{json_format}\n\n")

    @staticmethod
    def reformat_the_dates():
        try:
            df = pandas.read_csv(work_dir / "cache.csv")
        except FileNotFoundError:
            return
        except pandas.errors.EmptyDataError:
            return
        else:
            log.info("Prepare dates for search in df..")
            list_of_dates = df.Date
            list_of_new_dates = []

            for elem in list_of_dates:
                try:
                    str_to_date = datetime.strptime(elem, "%a, %d %b %Y %H:%M:%S %z")
                    d_2 = datetime.strftime(str_to_date, "%Y%m%d")
                    list_of_new_dates.append(d_2)
                except ValueError:
                    try:
                        str_to_date = datetime.strptime(elem, "%Y-%m-%dT%H:%M:%SZ")
                        d_2 = datetime.strftime(str_to_date, "%Y%m%d")
                        list_of_new_dates.append(d_2)
                    except ValueError:
                        try:
                            str_to_date = datetime.strptime(elem, "%a, %d %b %Y %H:%M:%S %Z")
                            d_2 = datetime.strftime(str_to_date, "%Y%m%d")
                            list_of_new_dates.append(d_2)
                        except ValueError:
                            try:
                                str_to_date = datetime.strptime(elem, "%Y-%m-%dT%H:%M:%S%z")
                                d_2 = datetime.strftime(str_to_date, "%Y%m%d")
                                list_of_new_dates.append(d_2)
                            except ValueError:
                                print(f"Can't reformat the date {elem}")
                                list_of_new_dates.append(elem)

            df.Date = list_of_new_dates
            return df.sort_values(by="Date", ascending=False).reset_index(drop=True)

    def df_to_dict(self, df):
        cache_to_output = {}
        for index, row in df.iterrows():
            cache_to_output["Source"] = row.Source
            cache_to_output["Feed"] = row.Feed
            cache_to_output["Title"] = row.Title
            cache_to_output["Date"] = row.Date
            cache_to_output["Link"] = row.Link
            cache_to_output["Description"] = row.Description
            cache_to_output["Image"] = row.Image
            log.info(f"Printing {index + 1} new from cache")
            if not self.json:
                self.print_data(cache_to_output)
            else:
                js_data = {index + 1: cache_to_output}
                self.print_data(js_data)
        return df

    def print_from_cache(self, limit=None):
        cache_data = self.reformat_the_dates()

        try:
            news_on_date = cache_data[(cache_data.Date == self.date)].reset_index(drop=True)
            if len(news_on_date) == 0:
                print("Error: No news found on this date")
                return
            else:
                news_not_on_date = cache_data[(cache_data.Date != self.date)].reset_index(drop=True)
                news_on_date_with_source = news_on_date[(news_on_date.Source == self.url)].reset_index(drop=True)
                news_not_on_date_with_source = news_not_on_date[(news_not_on_date.Source == self.url)].reset_index(
                    drop=True)
                news_on_date_without_source = cache_data[(cache_data.Date == self.date) & (
                        cache_data.Source != self.url)].reset_index(drop=True)
                another_news = cache_data[(cache_data.Date != self.date) & (cache_data.Source != self.url)].reset_index(
                    drop=True)
                limit_date = pandas.concat([news_on_date, news_not_on_date]).reset_index(drop=True)
                limit_date_source = pandas.concat(
                    [news_on_date_with_source, news_on_date_without_source,
                     news_not_on_date_with_source, another_news]).reset_index(drop=True)

        except AttributeError:

            print("Error: News cache not found..")

        else:
            if limit is None:
                if self.url is None:
                    cache = self.df_to_dict(news_on_date)
                else:
                    if len(news_on_date_with_source) == 0:
                        print("Error: No news found on this date with given source.")
                        return
                    cache = self.df_to_dict(news_on_date_with_source)
            else:
                if limit > len(cache_data):
                    limit = len(cache_data)
                elif limit <= 0:
                    print("News limit must be a positive number..")
                    return
                if self.url is None:
                    cache = self.df_to_dict(limit_date.head(limit))
                else:
                    if len(news_on_date_with_source) == 0:
                        print("Error: No news found on this date with given source.")
                        return
                    cache = self.df_to_dict(limit_date_source.head(limit))

