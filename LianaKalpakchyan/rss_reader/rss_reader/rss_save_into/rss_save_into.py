#!/usr/bin/env python3
from xhtml2pdf import pisa
import logging
import datetime
import os


class Converter:
    """
    A class to convert news into html, pdf formats

    ...

    Attributes
    ----------
    template: str
        Keeps html template

    Methods
    -------
    make_html_template():
        Receives news as items and creates a html template based on them

    create_path():
        Receives file extension and file path. Currently it can only save html and pdf files
    """

    def __init__(self):
        self.template = ''

    def make_html_template(self, items):
        """
        This function receives news as items from news feed creates a html template and styles it.
        :param items
        :returns ready template
        """
        logging.debug('"make_html_template" function is activated')
        main_html = ''
        style = """<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"> 
    <style type="text/css"> 
            *{
                font-family: monospace; 
                word-break: break-word;
                text-align: center;
            }
            body{
                margin: 20px;
                background: #A3AB78;
            }
            .news{
                width: 60%;
                margin: 20px auto;
                padding: 20px;
                box-sizing: border-box;
                border: 5px solid #BDE038;
                border-radius: 25px;
                background: #10454F;
                color: #BDE038;
            }
            .news img{
                width: 50%;
                transition: 0.5s;
            }
            .news img:hover{
                filter: sepia(100%)
            }
            .news_date{
                font-style: italic;  
            } 
            a{
                color: white;
                text-decoration: none;
            }
            a:hover{
                text-decoration: underline;
            }
    </style>
</head>"""
        for item in items:
            open_div = '<div class="news">'
            title = f'<h2>{item["title"]}</h2>'
            link = f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>'
            pubdate = f'<p class="news_date">{item["pubDate"]}</p>'
            description = f'<p>{item["description"]}</p>'
            image = item['image']
            if image == 'No image found':
                image = f'<p>"NO IMAGE"</p>'
            else:
                image = f'<p><img alt="" src="{image}"></p>'
            close_div = '</div>'

            pre_html = f"""
    {open_div}
        {title}
        {link} 
        {pubdate}
        {description}
        {image}
    {close_div}"""
            main_html += pre_html
        self.template = f'<!DOCTYPE html>\n<html>\n{style}\n<body>\n' + main_html + '\n</body>\n</html>'
        return self.template

    @staticmethod
    def create_path(file_path, extension):
        """
        This function receives file extension and file path. It can save html and pdf files in provided path.
        There are default folder html_files for html and pdf_files for pdf. These folder are saved in rss_folder.
        If optional --path argument receives path file will be saved there.
        :params file_path, extension
        :returns path_to_save, final_path
        """
        logging.debug('"create_path" function is activated')
        default_file_name = str(datetime.datetime.now()).replace(':', '_')
        path_to_save = os.path.join(file_path, default_file_name + extension)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        final_path = os.path.abspath(path_to_save)

        return path_to_save, final_path

    def convert_to_html(self, file_path):
        """
        This function generates an html real file and prints where it is saved
        :param file_path
        :returns None
        """
        logging.debug('"convert_to_html" function is activated')
        path_to_save, final_path = self.create_path(file_path, '.html')

        with open(path_to_save, 'w+', encoding='utf-8') as file:
            file.write(self.template)

        print(f'Address for the html file: {final_path}')

    def convert_to_pdf(self, file_path):
        """
        This function generates an pdf real file and prints where it is saved
        :param file_path
        :returns None
        """
        logging.debug('"convert_to_pdf" function is activated')
        path_to_save, final_path = self.create_path(file_path, '.pdf')

        with open(path_to_save, "w+b") as pdf_file:
            pisa.CreatePDF(self.template, dest=pdf_file, encoding='UTF-8')

        print(f'Address for the pdf file: {final_path}')
