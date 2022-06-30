"""
Main rss-reader module which does all needed operations with data passed on python script call.
Parses rss-feed, get needed data from here, print it out, convert output to JSON format, create cache,
convert information to html or pdf etc.
"""
import colorama
import requests
import pandas
import bs4
import html
import json
import logging as log
from datetime import datetime
import io
from template import temp
from colorama import Fore
from pygments import highlight, lexers, formatters
import os
from pathlib import *
from xhtml2pdf import pisa
from xhtml2pdf.default import DEFAULT_FONT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


work_dir = Path(__file__).absolute().parent
colorama.init()


class NewsBrain:
    """
      Base class of rss-reader, gathers required information from rss-feeds and print a dictionary with valuable data.
    Caches gathered news for later use, using pandas lib.
    Provides methods for printing data in stdout with option of converting to JSON format.
    News dictionary and JSON structure are described in README.md
    provides converters functionality
    """
    def __init__(self, url, limit, js, date, html_path, pdf_path, colorized):
        """
        Method serves for processing news from rss feeds.
        On object creation it gathers required news data, updates news cache and processes data for future output.
        :param url: default = None. URL of rss-feed.
        :param limit: default value = None.
         If not None, limits the number of news which will be printed in stdout or wil be converted to the specified
         format.
        :param js: default value = False. if True, outputs data in JSON format.
        :param date: default = None. If not None, indicates the date on which the local cache will be searched.
        :param html_path: default = None. if not None, the path that indicates where the html file will be saved.
        :param pdf_path: default = None. if not None, the path that indicates where the pdf file will be saved.
        """

        self.url = url
        self.limit = limit
        self.json = js
        self.date = date
        self.html_path = html_path
        self.pdf_path = pdf_path
        self.colorized = colorized

        try:
            self.cache = pandas.read_csv(work_dir/"cache.csv")
        except FileNotFoundError:
            self.cache = pandas.DataFrame(columns=["Source", "Feed", "Title", "Date", "Link", "Description", "Image"])
        except pandas.errors.EmptyDataError:
            self.cache = pandas.DataFrame(columns=["Source", "Feed", "Title", "Date", "Link", "Description", "Image"])

    @staticmethod
    def create_logger():
        """
        This file sets logging configuration, by default, according to the task, logging level is set to Debug
        :return logger
        """
        log_format = "%(asctime)s - %(message)s \n"
        log.basicConfig(level=log.DEBUG, format=log_format)
        logger = log.getLogger()
        return logger

    def get_rss_data(self):
        """
        The method takes a URL as an argument and returns request response in form of object of bs4.BeautifulSoup.
        If URL is invalid, or None, prints clear user message about bad connection status and asks to check internet
         connection or RSS URL.
        :return: object of bs4.BeautifulSoup, parsed with xml parser, containing rss data
        """
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
        """
        Method which is called only if there is not <description> section in rss data to try fetch the first and second
        paragraphs as a description  or firs paragraph of article as the description of new.
        :param url: link of html page with article
        :return first and second paragraphs is they exist, else try to return first paragraph of article, if there is no
        <article> section on web page, prints 'article not found' and return None.
        """
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
        """
        A method that finds the required information in the bs4.BeautifulSoup object and writes it to the corresponding
        dictionary keys.
        if the object does not have a corresponding description section, the method tries to get the first two
        paragraphs of the article. If the self.json parameter is specified(True), outputs information in JSON format.
        If the method cannot fetch the information from a particular tag, the value of the dictionary key = not found.
        Also updates the local news cache and converts the news to html or pdf if the paths for these parameters have
        been specified.
        :param xml_data: object of bs4.BeautifulSoup which contains all needed information about news.
        :param limit: limits the number of news which will be printed in stdout or wil be
        converted to the specified format.
        :return: if limit <= 0 prints an error 'News limit must be positive number' and return None.
        If RSS URL does not contain standard information of xml file like <item>, prints
        "News Not Found. Please, check your RSS URL." and return None.
        """
        data = {}
        list_of_news = []

        news = xml_data.find_all("item")
        if len(news) == 0:
            print("News Not Found. Please, check your RSS URL.")
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
                    data["Title"] = html.unescape(news[i].title.text.replace("\xa0", " "))
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
                    data["Description"] = html.unescape(soup.p.text.replace("\n", " ").replace("\xa0", " "))
                    if data["Description"] == "":
                        data["Description"] = xml_data.channel.description.text
                except AttributeError:
                    try:
                        desc = news[i].find("description").text
                        if '<' not in desc:
                            data["Description"] = html.unescape(
                                news[i].find("description").text.replace("\n", " ").replace("\xa0", " "))
                        else:
                            data["Description"] = xml_data.channel.description.text
                    except AttributeError:
                        data["Description"] = html.unescape(
                            self.get_news_text(data["Link"]).replace("\n", " ").replace("\xa0", " "))
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
                    print(Fore.RESET)
                    if not self.json:
                        self.print_data(data)
                    else:
                        js_data = {i + 1: data}
                        self.print_data(js_data)
            cached_news = pandas.DataFrame(list_of_news)
            cache_merge = pandas.merge(self.cache, cached_news, how="outer").drop_duplicates(subset="Title")
            cache_merge.to_csv(work_dir/"cache.csv", index=False)
            self.convert(cached_news)

    def print_data(self, data):
        """
        a method that prints a dictionary with news tags. If the json parameter is specified,
        converts the dictionary to json string and prints it to stdout.
        :param data: The dictionary which will be printed in stdout
        :return: None
        """
        if self.colorized:
            if not self.json:
                for key, value in data.items():
                    print(f"{Fore.BLUE}{key}: {Fore.YELLOW}{value}")
                print("\n\n")
            else:
                json_format = json.dumps(data, ensure_ascii=False, indent=4)
                colored_json = highlight(json_format, lexers.JsonLexer(), formatters.TerminalFormatter())
                print(f"{colored_json}\n\n")
            print(Fore.LIGHTCYAN_EX)
        else:
            if not self.json:
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("\n\n")
            else:
                json_format = json.dumps(data, ensure_ascii=False, indent=4)
                print(f"{json_format}\n\n")

    @staticmethod
    def reformat_the_dates():
        """
        Method formats the dates of the data frame without changing it to the format "% Y% m% d".
        If there is no template for date formatting, this date remains unchanged.

        :return: pandas Dataframe with dates, sorted by values in order from last to older.
        """
        try:
            df = pandas.read_csv(work_dir/"cache.csv")
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
        """
        the method that takes the dataframe as input converts its data into a dictionary and outputs it to the stdout,
        but the dataframe itself returns unchanged.
        :param df: pandas DataFrame, which will be converted into a dict, and printed out.
        :return: pandas DataFrame without changing.
        """
        log.info("prepare dict from dataframe..")
        cache_to_output = {}
        for index, row in df.iterrows():
            cache_to_output["Source"] = row.Source
            cache_to_output["Feed"] = row.Feed
            cache_to_output["Title"] = row.Title
            cache_to_output["Date"] = row.Date
            cache_to_output["Link"] = row.Link
            cache_to_output["Description"] = row.Description
            cache_to_output["Image"] = row.Image
            log.info(f"Printing {index+1} new from cache")
            print(Fore.RESET)
            if not self.json:
                self.print_data(cache_to_output)
            else:
                js_data = {index + 1: cache_to_output}
                self.print_data(js_data)
        return df

    def convert(self, cached_data):
        """
        Method modifies the dataframe with adding img and a href tags according to the html image and link tags,
        and converts the dataframe to html using a previously created template for the html format.
        If the html parameter is specified, saves the html file in the appropriate path, if the path for html is not
        specified, but specified for PDF,  converts the already prepared string with html code to PDF.
        If it is not possible to save the file in the specified path, it creates a default folder and saves the
        files there. If a file name is specified, and specified path is valid to create file,
        saves it under this name, if not - saves it under  default name news.pdf or news.html.
        Prints to stdout, where file is saved after saving.
        Disables warnings and from xhtml2pdf lib logger for case if internet connection is not provided. It doesn't
        print xhtml2pdf lib logs to console.
        Change default font of this lib to display cyrillic correctly.
        :param cached_data: pandas dataframe that converts to the specified format.
        :return: None
        """
        default = Path.cwd() / "default_dir"
        df = cached_data

        def create_images(img):
            """
            Method, which creates a template with local paths of images to convert the dataframe to html without
            internet connection and to display images correctly
            :param img: local path to image
            :return: template for tag 'image', which will be used to convert needed dataframe to html
            """
            if img != "Image not found":
                img_template = '''<img src="{img}" alt="image" width="300" height="300">'''.format(img=img)
            else:
                img_template = '''<p>{img}</p>'''.format(img=img)
            return img_template

        def create_url(url):
            """
            Method, which creates a template for links to convert the dataframe to html to display links correctly.
            :param url: tag Link for each row for dataframe
            :return: template for tag 'link', which will be used to convert needed dataframe to html
            """
            if url != "Link not found..":
                url_template = '''<a href="{url}" target="_blank">Click me!!</a>'''.format(url=url)
            else:
                url_template = '''<p>{url}</p>'''.format(url=url)
            return url_template

        for index, row in df.iterrows():
            row.Image = create_images(row.Image)
            row.Source = create_url(row.Source)
            row.Link = create_url(row.Link)

        t = df.to_html(render_links=True, escape=False, index=False, justify="center")
        html_out = temp.format(outp=t)
        if self.html_path is not None:
            if self.html_path.suffix != ".html":
                self.html_path = self.html_path / 'news.html'
            try:
                with open(self.html_path, 'w', encoding="utf-8") as f:
                    f.write(html_out)
                print(f"was saved there: {os.path.abspath(self.html_path)}")
            except OSError:
                if not default.is_dir():
                    default.mkdir()
                with open(default / "news.html", 'w', encoding="utf-8") as f:
                    f.write(html_out)
                print(f"Invalid path was given..Was saved there: {os.path.abspath(default / 'news.html')}")

        if self.pdf_path is not None:
            source_html = html_out
            if self.pdf_path.suffix != ".pdf":
                self.pdf_path = self.pdf_path / 'news.pdf'

            output_filename = self.pdf_path

            def convert_html_to_pdf(html_string, path_to_save):
                """
                Method converts html string to pdf format.

                :param html_string: string of html code page
                :param path_to_save: path to save the pdf file
                :return: None
                """
                result_file = None
                font_path = work_dir / 'font' / 'calibri.ttf'
                pdfmetrics.registerFont(TTFont('ru-readable', font_path))
                DEFAULT_FONT["helvetica"] = "ru-readable"

                try:
                    result_file = open(path_to_save, "w+b")
                    print(f"Was saved there: {os.path.abspath(path_to_save)}")
                except OSError:
                    if not default.is_dir():
                        default.mkdir()
                    result_file = open(default / "news.pdf", "w+b")
                    print(f"Invalid path was given..Was saved there: {os.path.abspath(default / 'news.pdf')}")
                finally:
                    pisa.CreatePDF(io.StringIO(html_string), dest=result_file, encoding="utf-8")
                    result_file.close()
                    return
            log.disable(log.ERROR)
            convert_html_to_pdf(source_html, output_filename)

    def print_from_cache(self, limit=None):
        """
        Method that selects the required news by date, limit, and source and outputs and converts the data to the
        desired format if arguments are specified.
        Formats the dates of the dataframe to "% Y% m% d" to search for the specified date.
        if there is no news on a given date, prints "Error: No news found", else if cache.csv could not be found or is
        empty, prints "Error: News cache not found..", else if limit <= 0, prints "News limit must be a positive
        number", else if source is specified and there is no news for specified date with this source, prints
        "Error: No news found on this date with given source."
        Also, this method combines several data frames into one, so that if the limit is specified,
        to display the desired news, sorted by date from all sources.

        :param limit: limits the number of news which will be printed in stdout or wil be
        converted to the specified format.
        :return: None
        """
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
            self.convert(cache)
