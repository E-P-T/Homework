#!/usr/bin/python

import argparse
import logging
import json
import os.path

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging as log

import version
import utility


def init_arguments():
    """
    All operations regarding the arguments of CLI, like adding and parsing
    :return: Parsed Arguments from CLI
    """
    parser = argparse.ArgumentParser(
        prog="rss_parser",
        usage="rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]",
        description="Pure Python command-line RSS reader.")
    parser.add_argument("source", help="RSS URL", nargs="?")
    parser.add_argument("--date", help="Publishing date of the news. Format of the input: %Y%m%d", action="store",
                        nargs="?")
    parser.add_argument("-v", "--version", help="Print version info", action="store_true")
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_true")
    parser.add_argument("--limit", help="Limit news topics if this parameter provided", action="store", type=int)
    parser.add_argument("--tp-pdf", help="Convert to pdf", action="store_true")
    parser.add_argument("--to-html", help="Convert to html", action="store_true")
    try:
        parser.parse_args()
    except Exception as e:
        error_verbose(str(e))
    return parser.parse_args()


def verbose(info):
    """
    Displaying logging info if --verbose is set
    :param info: infor to be printed
    :return: no return
    """
    args = init_arguments()
    if args.verbose:
        log.getLogger().setLevel(logging.INFO)
        log.info("{date} {info}".format(date=str(datetime.now()), info=info))
    else:
        pass


def error_verbose(err):
    """
    Displaying error messages
    :param err: Error message to be displayed
    :return:
    """
    log.getLogger().setLevel(logging.ERROR)
    log.error("{date} {error}".format(date=str(datetime.now()), error=err))


class RSSFeed:
    """
    Class RSSFeed is a class of each fee with its items
    """
    def __init__(self, source):
        self.source = source
        try:
            verbose("Sending request to given source...")
            self.response = requests.get(source)
            self.status_code = self.response.status_code
            verbose("Received response with status code {s_code}".format(s_code=self.status_code))
        except Exception as err:
            error_verbose(str(err))
        try:
            self.soup = BeautifulSoup(self.response.content, features="xml")
        except Exception as err:
            error_verbose(str(err))
        self.articles = self.soup.find_all("item")
        self.feed_link = self.soup.channel.link.string
        self.feed_title = self.soup.channel.title.string


def main():
    """
    Most of the important operations of rss_reader are functioning in this method
    :return: No return
    """
    args = init_arguments()
    log.getLogger().setLevel(logging.INFO)

    feed = RSSFeed(args.source)
    print(feed.feed_title, end='\n\n')

    if not args.source:
        if args.version:
            print("Version of the project: ", version.__version__)
        elif args.date:
            if isDateValid(args.date):
                verbose("This is the correct date string format.")

                with open('storage.json', 'r', encoding='utf-8') as file:
                    print("Accessing local storage...")
                    local_storage_data_dict = json.loads(file.read())

                if args.json:
                    # date, json
                    feed_dict = {"feedTitle": feed.feed_title, "Items": []}
                    for item in local_storage_data_dict["Items"]:
                        if args.date == item["pubDate"]:
                            items_dict = {"Item": item["Item"], "Date": item["pubDate"], "Link": item["Link"],
                                          "Description": item["Description"] if item.description
                                          else "Description is unavailable", "Links": item["Links"]}
                            feed_dict["Items"].append(items_dict)
                        print(json.dumps(feed_dict, indent=4, ensure_ascii=False))
                else:
                    # date
                    for item in local_storage_data_dict["Items"]:
                        if args.date == item["pubDate"]:
                            print("Title: {}".format(item["Item"]))
                            print("Date: {}".format(item["pubDate"]))
                            print("Link: {}".format(item["Link"]))
                            if not item.description:
                                print("Description: No description is available", end="\n\n")
                            else:
                                print("Description: {}".format(item["Description"]), end="\n\n")
                            list_of_links = item["Links"]
                            verbose("Searching for other links...")
                            for i, link in enumerate(list_of_links):
                                print(
                                    f"[{i + 1}]: {link} ({'link' if i == 0 else 'image'})"
                                    , end="\n\n" if i == (len(list_of_links) - 1) else "\n")
        elif not args.date and args.json:
            error_verbose("Wrong set of arguments, empty source!")
        else:
            error_verbose("Invalid Source!")
    else:
        verbose("Validating the given source...")
        if utility.isUrlValid(str(args.source)):
            verbose("Successfully validated!")
            if not args.limit or args.limit > len(feed.articles):
                limit = len(feed.articles)
            else:
                limit = args.limit
            verbose("Extracting data from source...")

            if args.json:
                arr_of_items = feed.articles[:limit]
                if args.date:
                    if isDateValid(args.date):
                        # source, json, date
                        verbose("This is the correct date string format.")

                        arr_of_items.clear()
                        for item in feed.articles[:limit]:
                            if item.pubDate == args.date:
                                arr_of_items.append(item)
                else:
                    # source, json
                    pass
                verbose("Generating JSON...")
                feed_dict = {"feedTitle": feed.feed_title, "Items": []}
                for item in arr_of_items:
                    items_dict = {"Item": item.title.string, "Date": item.pubDate.string, "Link": item.link.string,
                                  "Description": item.description.string if item.description
                                  else "Description is unavailable", "Links": return_links(item)}
                    feed_dict["Items"].append(items_dict)
                print(json.dumps(feed_dict, indent=4, ensure_ascii=False))
            else:
                arr_of_items = feed.articles[:limit]

                # if args.date == True
                if args.date:
                    if isDateValid(args.date):
                        # source, date
                        arr_of_items.clear()
                        for item in feed.articles[:limit]:
                            if datetime.strptime(str(item.pubDate.string), "%a, %d %b %Y %H:%M:%S %z") == args.date:
                                arr_of_items.append(item)
                else:
                    # source
                    dict_from_storage = return_dict_from_storage()
                    if not dict_from_storage:
                        dict_from_storage = {feed.feed_link: []}
                    for item in arr_of_items:
                        print("Title: {}".format(item.title.string))
                        print("Date: {}".format(item.pubDate.string))
                        print("Link: {}".format(item.link.string))
                        if not item.description:
                            print("Description: No description is available", end="\n\n")
                        else:
                            print("Description: {}".format(item.description.string), end="\n\n")
                        list_of_links = return_links(item)
                        verbose("Searching for other links...")
                        for i, link in enumerate(list_of_links):
                            print(
                                "[{index}]: {link} ({type})".format(index=i + 1, link=link,
                                                                    type='link' if i == 0 else 'image')
                                , end="\n\n" if i == (len(list_of_links) - 1) else "\n")
                        # storing in storage
                        items_dict = {"Item": item.title.string, "Date": item.pubDate.string, "Link": item.link.string,
                                      "Description": item.description.string if item.description
                                      else "Description is unavailable", "Links": return_links(item)}
                        dict_from_storage[feed.feed_link].append(items_dict)
                    if write_to_storage_file(dict_from_storage):
                        verbose("Successfully added to storage!")
                    else:
                        error_verbose("Unable to write to storage!")

        else:
            error_verbose("Invalid source, please check link again.")


def return_links(item):
    """
    Parsing other links including main link of item
    :param item: Each item from XML parsed item
    :return: List of found links
    """
    links_arr = [item.link.string]
    if item.content:
        links_arr.append(item.content["url"])
    elif item.enclosure:
        links_arr.append(item.enclosure["url"])
    else:
        pass

    return links_arr


def isDateValid(date):
    """
    Checking for validity of the date
    :param date: pubDate of the parsed XML item
    :return: True if valid else False
    """
    date_format = "%Y%m%d"
    isValidDate = True
    try:
        datetime.strptime(str(date), date_format)
    except ValueError:
        isValidDate = False
        error_verbose("This is the incorrect date string format. It should be YYYY-MM-DD")
    return isValidDate


def return_dict_from_storage():
    """
    Reading and Returning Dictionary type object from storage.json file
    :return: Dictionary
    """
    if os.path.exists("storage.json"):
        with open('storage.json', 'r') as read_file:
            print("Accessing local storage...")
            if not read_file.read():
                local_storage_data_dict = {}
            else:
                local_storage_data_dict = json.load(read_file)
        return local_storage_data_dict


def write_to_storage_file(json_dict):
    """
    Writing to local storage.json file
    :param json_dict: Dictionary type object
    :return: True if writing is successful else False
    """
    success = True
    with open('storage.json', 'w') as file:
        json.dump(json_dict, file, indent=4)
    verbose("Success")

    return success


if __name__ == "__main__":
    main()
