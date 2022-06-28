"""
Converter
"""
import os
import pathlib
import re
import json
import jinja2
import fpdf
import logging

BASE_DIR = pathlib.Path(__file__).parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")
FONT_DIR = os.path.join(BASE_DIR, "font")
WORKING_DIR = os.getcwd()


class MyFPDF(fpdf.FPDF, fpdf.HTMLMixin):
    """
    Mixin class that inherits FPDF and HTML2PDF methods
    """
    pass


class Converter:
    """
    Converter class that receives the data and path (optional)
    and convert data into pdf or html format (depending on your choice).
    If no path is specified, Converter object will convert your data to
    a file in your current working directory
    """

    def __init__(self, feed, path):
        self.feed = None
        self.path = self.check_path(path)
        self.__prepare_feed(feed)

    def to_html(self):
        """
        Creates html page with feed from specified template
        :return:
        """
        logging.info("Starting transformation to HTML")
        html_data = self.__get_html(template_name="template.html")
        html_out_path = os.path.join(self.path, 'feed.html')
        self.load(html_data, html_out_path)

    def to_pdf(self):
        """
        Creates pdf file with feed
        :return:
        """
        logging.info("Starting transformation to PDF")
        pdf = MyFPDF()
        pdf.add_font("DejaVu", "", f"{FONT_DIR}/DejaVuSansCondensed.ttf")
        pdf.set_font("DejaVu", "", 32)
        pdf.add_page()
        pdf.set_margins(10, 120, 10)
        pdf.multi_cell(0, None, txt=self.feed['title'], align="C")
        pdf.set_margins(10, 10, 10)
        pdf.set_font("Dejavu", "", 18)
        pdf.set_margins(10, 20, 10)
        for item in self.feed['items']:
            pdf.add_page()
            html_item = self.__get_html(template_name="item.html", data=item)
            pdf.write_html(html_item)
        pdf.output(os.path.join(self.path, "feed.pdf"))

    @staticmethod
    def check_path(path):
        logging.info("Checking your path exists")
        if not os.path.exists(os.path.abspath(path)):
            logging.info(f"Your inputter path doesn't exists! File will be saved to {WORKING_DIR}")
            print(f"Your inputter path doesn't exists! File will be saved to {WORKING_DIR}")
            return WORKING_DIR
        return path

    @staticmethod
    def load(data, path):
        """
        Loads received data to specified path and opens it after loading
        :param data: Any string data
        :param path: path to load
        :return:
        """
        with open(path, "wb") as file:
            file.write(data.encode("utf-8"))
            os.startfile(path)

    def __get_html(self, template_name, data=None):
        """
        Method that renders received data in specified template
        :param template_name: string with template name (all templates you can see in template directory)
        :param data: dict with feed
        :return: result in html (str) format
        """
        if data is None:
            data = self.feed
        loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
        env = jinja2.Environment(loader=loader)
        template = env.get_template(template_name)
        html_data = template.render(data=data)
        return html_data

    def __prepare_feed(self, feed):
        """
        Receives rss feed and replaces all human-readable link and image elements with a and img tags.
        :return:
        """
        logging.info("Removing all unnecessary symbols from feed description")
        if isinstance(feed, str):
            feed = json.loads(feed)
        for item in feed["items"]:
            description = item["description"]
            if description.lower() == "empty":
                continue
            patterns_items = [
                re.compile(r'\[Link_\d*]\[Image_\d+]\[]'),
                re.compile(r'\[Image_\d\]'),
                re.compile(r"\[Link_\d\]"),
                re.compile(r"\[]")
            ]
            for pattern in patterns_items:
                while re.search(pattern, description):
                    if pattern is patterns_items[0] or pattern is patterns_items[1]:
                        string = ""
                    elif pattern is patterns_items[2]:
                        url_index = int(re.search(pattern, description).group(0)[1:-1].split("_")[1])
                        string = f"<a href='{item['urls'][url_index - 1]}' target='_blank'>"
                    else:
                        string = "</a>"
                    description = re.sub(pattern, string, description, count=1)
            item["description"] = description
        self.feed = feed
