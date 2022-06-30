import requests
from lxml import etree
import xml.etree.ElementTree as elementTree
from bs4 import BeautifulSoup
import time
from dateutil import parser
import json
import logging as log
import argparse
import os
import rss_reader.database_handler as handler
from datetime import datetime
from ebooklib import epub



def get_content(url: str):

    """Get request from the url and depending on a flag returns corresponding xml etree or html soup"""

    log.info(f"Try in to retrieve information from {url}")
    try:
        r = requests.get(url)
        log.info(f"Connection to {url} established!")
        if is_xml(r.content):
            root = etree.fromstring(r.content)
            log.info("XML content downloaded and parsed.")
            return root[0]
        else:
            raise AttributeError()
    except requests.exceptions.RequestException as exc:
        print(f"Error Occurred: {exc}")
    except AttributeError:
        print("Site that you entered is not RSS, because it doesn't contain XML!")


def is_xml(value):

    """Check value containing XML content"""

    try:
        elementTree.fromstring(value)
    except elementTree.ParseError:
        log.info("Received data isn't XML.")
        return False
    else:
        log.info("Received data is XML content.")
        return True


def get_feed(root):

    """Return feed string"""

    feed = root.find("title").text
    return feed


def get_news_db(root, num=None):

    """Get all "item" elements and return list or slice of the list from root if num specified."""

    news_db = root.findall("item")

    if num is not None:
        news_slice = news_db[:num]
        log.info("Retrieved user defined number of news.")
        return news_slice
    else:
        log.info("Retrieved all amount of news.")
        return news_db


def inf_generator(news_db):

    """Get information from the "item" list and yield it as a list
     next format [title, link, date, description]"""

    log.info("Retrieving information from item branches.")
    for bunch in news_db:
        title = bunch.find("title").text
        link = link_handler(bunch.find("link"))
        date = date_handler(bunch.find("pubDate"))
        description = description_handler(bunch.find("description"))
        inf_lst = [title, link, date, description]
        log.info("Branch retrieved successful!")
        yield inf_lst


def date_handler(date_inf):

    """Return date in weekday, daynumber month year hours:minutes:seconds timezone"""

    if date_inf is None:
        log.info("RSS doesn't provide date field!")
        return "Date field doesn't provided!"
    else:
        date = date_inf.text
        pure_date = parser.parse(date)
        return_date = pure_date.strftime("%a, %d %b %Y %H:%M:%S %z")
        log.info("Date retrieved successfully!")
        return return_date


def link_handler(inf):

    """Handles absence of link in RSS."""

    if inf is None:
        log.info("RSS doesn't provide news link!")
        return "Link field doesn't provided!"
    else:
        log.info("Link retrieved successful.")
        link = inf.text
        return link


def description_handler(inf):

    """Handles absence of link in RSS and gets HTML from the string."""

    if inf is None:
        log.info("RSS doesn't provide description!")
        return "There is no description!"
    else:
        description = inf.text
        if description is None:
            log.info("RSS doesn't provide description!")
            return "There is no description"
        elif "<" in description:
            soup = BeautifulSoup(description, "html.parser")
            data = soup.text
            log.info("Description retrieved successful from HTML text.")
            return data
        else:
            log.info("Description retrieved successful.")
            return description


def printer(feed, news_db):

    """Printing in the console news in next format:
    Feed:[title of the rss site where you get news]
    
    Title: [fact's title]
    Date: [date of that fact]
    Link: [link to the fact]
    Description: [fact's short summary]
    """""

    log.info("Printing information to console!")
    print(f"Feed: {feed}", "\n")
    gen = inf_generator(news_db)
    for inf in gen:
        print(f"Title: {inf[0]}")
        print(f"Date: {inf[2]}")
        print(f"Link: {inf[1]}")
        print(f"Description: {inf[3]}", end="\n")
        print('\n')


def news_to_json(feed, news_db):

    """Collect information form the site into dict "news feed" and return it as a json string"""

    log.info("Collection information to json format.")
    news_feed = {feed: []}
    gen = inf_generator(news_db)
    for inf in gen:
        fact_dict = {"Title": inf[0],
                     "Link": inf[1],
                     "Date": inf[2],
                     "Description": inf[3],
                     }
        news_feed[feed].append(fact_dict)
    log.info("Collecting JSON completed successful!")
    return json.dumps(news_feed, ensure_ascii=False, indent=4)


def output_form(main_title, news_data, form):

    """Printing return the output to console if form specified (console/json)"""

    if form not in ["console", "json"]:
        log.error("Entered unavailable format!")
        raise AttributeError("Choose between console or json!")
    elif form == "console":
        log.info("Printing information to console....")
        printer(main_title, news_data)
    elif form == "json":
        log.info("Printing json information to console....")
        news_json = news_to_json(main_title, news_data)
        print(news_json)


def create_path(path):

    """Creates path if it not exist"""

    if not os.path.exists(path):
        os.mkdir(path)
        log.info(f"Path {path} created")


def html_adder(nw_title, db, head=None):

    """Creates HTML text from database and title."""

    log.info("Start creating HTML text!")
    if head is None:
        head = datetime.now().strftime("%d%m%y %H:%M")
        log.info("Created head for HTML text!")

    header = f"""<!DOCTYPE html>
              <html lang="en">
              <head>
                <meta charset="UTF-8">
                <title>{head}</title>
              </head>
              <body>"""

    end = """</body>
            </html>"""

    html_text = header

    h1 = f"""<h1>Feed: {nw_title}</h1>"""
    html_text += h1
    gen = inf_generator(db)
    for inf in gen:
        p = f"""<p>
        <a><b>Title:</b> {inf[0]}</a><br>
        <a><b>Link:</b> <a href  = "{inf[1]}">clickable link</a></a><br>
        <a><b>Date:</b> {inf[2]}</a><br>
        <a><b>Description:</b> {inf[3]}</a><br>
        <hr>
        </p>"""
        html_text += p
    html_text += end
    log.info("HTML text creation complieted!")
    return html_text

def write_html_file(path, html_text, html_name=None):

    """Write HTML text to file, than saves file to the path,
    also this programm automatically gives name to files."""

    log.info("Starting writing HTML to the file!")
    if html_name is None:
        html_name = datetime.now().strftime("%d%m%y%H%M") + ".html"
        log.info("Created name for HTML file!")
    if not html_name.endswith(".html"):
        html_name = html_name + ".html"
        log.info("Added .html extention to file name!")
    full_path = os.path.join(path, html_name)
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(html_text)
        log.info("HTML file created!")
    print(f"HTML file saved to to path: {full_path}")


def write_epub_file(path, html_text, epub_name=None):

    """Write ePub file, than saves file to the path,
        also this programm automatically gives name to files."""

    log.info("Starting writing HTML to the ePub file!")
    if epub_name is None:
        epub_name = datetime.now().strftime("%d%m%y%H%M") + ".epub"
        log.info("Created name for ePub file!")
    if not epub_name.endswith(".epub"):
        epub_name = epub_name + ".epub"
        log.info("Added .epub extention to file name!")
    file_path = os.path.join(path, epub_name)
    book = epub.EpubBook()
    book.add_author('Nurmatov Farrukh')    # you found easter egg
    c1 = epub.EpubHtml(title='News', file_name='chap_01.xhtml')
    c1.content = html_text
    book.add_item(c1)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    book.spine = ['nav', c1]
    epub.write_epub(file_path, book, {})
    log.info("ePub file created!")
    print(f"Epub file saved to: {file_path}")


def main():
    parser = argparse.ArgumentParser(description="This program gets information from RSS-channel "
                                                 "and returns in user friendly format.")
    parser.add_argument("source", type=str, nargs="?", help="RSS link for your information", default=None)
    parser.add_argument("--date", type=str, help="Get news form the database by date.")
    parser.add_argument("-v", "--version", action="version", version="Version 1.4.0",
                        help="Print program version and exit.")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages.")
    parser.add_argument("--to-html", action="store_true", help="Return HTML file to C:\\rss_reader\\html_files",
                        dest="to_html")
    parser.add_argument("--to-epub", action="store_true", help="Return HTML file to C:\\rss_reader\\epub_files",
                        dest="to_epub")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout.")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided.")

    args = parser.parse_args()
    rss_url = args.source
    date = args.date
    verbose = args.verbose
    html = args.to_html
    epub = args.to_epub
    print_json = args.json
    limit = args.limit

    parent_dir = "C:/"
    root_dir = "rss_reader"
    db_dir = "data_base"
    html_dir = "html_files"
    epub_dir = "epub_files"

    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    sys_path = os.path.join(parent_dir, root_dir)
    create_path(sys_path)
    db_path = os.path.join(sys_path, db_dir)
    create_path(db_path)
    html_path = os.path.join(sys_path, html_dir)
    create_path(html_path)
    epub_path = os.path.join(sys_path, epub_dir)
    create_path(epub_path)
    db = os.path.join(db_path, handler.data_base)
    base = handler.DataBaseHandler(db)
    base.create_table()

    try:
        if date is not None:
            if base.emptiness_checker():
                raise AttributeError
            base_inf = base.retrieve_data(date, rss_url, limit)
            html_data = base.data_to_html(date)
            if print_json and html:
                print(base.data_to_json(date))
                write_html_file(html_path, html_data, date)
            elif print_json and epub:
                print(base.data_to_json(date))
                write_epub_file(epub_path, html_data, date)
            elif print_json:
                print(base.data_to_json(date))
            elif html:
                write_html_file(html_path, html_data, date)
                base.data_to_print(date)
            elif epub:
                write_epub_file(epub_path, html_data, date)
                base.data_to_print(date)
            else:
                base.data_to_print(date)
        else:
            xml_content = get_content(rss_url)
            feed = get_feed(xml_content)
            news_db = get_news_db(xml_content, limit)
            sql_gen = inf_generator(news_db)
            html_inf = html_adder(feed, news_db)

            for inf in sql_gen:
                base.add_data(rss_url, *inf)

            if print_json and html:
                output_form(feed, news_db, "json")
                write_html_file(html_path, html_inf)
            elif print_json and epub:
                output_form(feed, news_db, "json")
                write_epub_file(epub_path, html_inf)
            elif print_json:
                output_form(feed, news_db, "json")
            elif html:
                write_html_file(html_path, html_inf)
                output_form(feed, news_db, "console")
            elif epub:
                write_epub_file(epub_path, html_inf)
                output_form(feed, news_db, "console")
            else:
                output_form(feed, news_db, "console")
    except ValueError:
        print(f"There is no data in database on date {date}.")
    except AttributeError:
        print(f"There is not data in the database. You should fill the database first.")


if __name__ == "__main__":
    main()
