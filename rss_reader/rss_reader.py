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
import database_handler as handler




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
        log.info(f"Path {path} created")
        os.mkdir(path)


def main():
    parser = argparse.ArgumentParser(description="This program gets information from RSS-channel "
                                                 "and returns in user friendly format.")
    parser.add_argument("source", type=str, nargs="?", help="RSS link for your information", default=None)
    parser.add_argument("--date", type=str, help="Get news form the database by date.")
    parser.add_argument("-v", "--version", action="version", version="Version 1.3.0",
                        help="Print program version and exit.")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages.")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout.")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided.")

    args = parser.parse_args()
    rss_url = args.source
    date = args.date
    verbose = args.verbose
    print_json = args.json
    limit = args.limit

    parent_dir = "C:/"
    root_dir = "rss_reader"
    db_dir = "data_base"

    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    sys_path = os.path.join(parent_dir, root_dir)
    create_path(sys_path)
    db_path = os.path.join(sys_path, db_dir)
    create_path(db_path)
    db = os.path.join(db_path, handler.data_base)
    base = handler.DataBaseHandler(db)
    base.create_table()

    try:
        if date is not None:
            if base.emptiness_checker():
                raise AttributeError
            base_inf = base.retrieve_data(date, rss_url, limit)
            if print_json:
                print(base.data_to_json(date))
            else:
                base.data_to_print(date)
        else:
            xml_content = get_content(rss_url)
            feed = get_feed(xml_content)
            news_db = get_news_db(xml_content, limit)
            sql_gen = inf_generator(news_db)

            for inf in sql_gen:
                base.add_data(rss_url, *inf)

            if print_json:
                output_form(feed, news_db, "json")
            else:
                output_form(feed, news_db, "console")
    except ValueError:
        print(f"There is no data in database on date {date}.")
    except AttributeError:
        print(f"There is not data in the database. You should fill the database first.")


if __name__ == "__main__":
    main()
