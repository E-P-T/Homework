import requests
from lxml import etree
import xml.etree.ElementTree as elementTree
from bs4 import BeautifulSoup
import json
import logging as log
import argparse


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
        date = bunch.find("pubDate").text
        description = description_handler(bunch.find("description"))
        inf_lst = [title, link, date, description]
        log.info("Branch retrieved successful!")
        yield inf_lst


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
        log.info("Description retrieved successful.")
        if "<" in description:
            soup = BeautifulSoup(description, "html.parser")
            data = soup.text
            return data
        else:
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
        printer(main_title, news_data)
    elif form == "json":
        news_json = news_to_json(main_title, news_data)
        print(news_json)


def main():
    parser = argparse.ArgumentParser(description="This program gets information from RSS-channel "
                                                 "and returns in user friendly format.")
    parser.add_argument("source", type=str, help="RSS link for your information")
    parser.add_argument("-v", "--version", action="version", version="Version 1.0.0",
                        help="Print program version and exit.")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages.")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout.")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided.")

    args = parser.parse_args()
    rss_url = args.source
    verbose = args.verbose
    print_json = args.json
    limit = args.limit

    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    xml_content = get_content(rss_url)
    feed = get_feed(xml_content)
    news_db = get_news_db(xml_content, limit)
    if print_json:
        output_form(feed, news_db, "json")
    else:
        output_form(feed, news_db, "console")


if __name__ == "__main__":
    main()
