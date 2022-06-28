import argparse
from py_console import console
from bs4 import BeautifulSoup
import requests
from json_convert_to_pdf import convert_to_pdf
from json_to_html import convert_to_html
from utilty import isValidURL
from html_tag_parse import clean_desc
from datetime import datetime
import json
from database_file.check_database import check_database_avaiable, local_img_storage
from dateutil import parser as date_parse
from uuid import uuid4
import os
VERSION_INFO = "4.3.0"

# get argparse data
def get_args():
    parser = argparse.ArgumentParser(
        description='Pure Python command-line RSS reader.')

    parser.add_argument("-v", "--version", help="Print version info",
                        action="store_true")
    parser.add_argument(
        "--verbose", help="Output verbose status messages", action="store_true")
    parser.add_argument("source", type=str, nargs="?",  help="RSS URL")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true")

    parser.add_argument("--limit", type=int, const=None,
                        help="Limit news topics if this parameter provided", nargs='?')
    parser.add_argument("--date", nargs="?", const=1, type=int,
                        help="Retrieves data from a given date from the cache if this parameter is provided")
    parser.add_argument("--to_html", nargs="?", const='rss_news.html',
                        help="Convert news to .html format and save it by the specified folder path (FOLDER_PATH can be optional).",
                        )
    parser.add_argument("--to_pdf", const='news_rss.pdf', nargs="?",
                        help="Convert news to .pdf format and save it by the specified folder path (FOLDER_PATH can be optional)")

    args = parser.parse_args()
    return args

# console log info
def verbose_caches(status_inf):
    verbose_args = get_args()
    if verbose_args.verbose:
        console.info("INFO " + str(datetime.now())+" "+status_inf)

# console log error
def verbose_caches_error(status_inf):
    verbose_args = get_args()
    if verbose_args.verbose:
        console.error("INFO " + str(datetime.now())+" "+status_inf)


# check verbose without process

# def get_verbose():

#     verbose_args = get_args()
#     verbose_data = []
#     if verbose_args.verbose:
#         date_info = "INFO " + str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
#         # verbose_data.append(date_info)
#         status_debug = "Verbose mode turn on"
#         verbose_data.append(status_debug)
#         if verbose_args.source:
#             if verbose_args.limit:
#                 status_limit = "{}".format(str(verbose_args.limit[0])) + " news were given"
#             else:
#                 status_limit = "limit is not given"
#             verbose_data.append(status_limit)

#             url = "Validating URL "+ "{}".format(verbose_args.source)
#             verbose_data.append(url)
#             if isValidURL(verbose_args.source) is True:
#                 check_url = "URL validated successfully"
#             else:
#                 check_url = "Please enter valid url!"
#             verbose_data.append(check_url)

#             making_request = "Making a URL request"
#             verbose_data.append(making_request)

#             check_ = str(requests.get(verbose_args.source))
#             if "200" in check_:
#                 success_url = "URL request successful. Reading and decoding response data"
#             else:
#                 success_url = "Page not found"
#             verbose_data.append(success_url)

#             if success_url != "Page not found":
#                 url_path = requests.get(verbose_args.source)
#                 tags = "Converting ElementTree. Element object to a dictionary. Searching for tags: ('title', 'creator', 'description', 'link', 'content', 'pubDate', 'image', 'enclosure')"
#                 verbose_data.append(tags)
#                 try:
#                     soup = BeautifulSoup(url_path.content,'xml')
#                     entries = soup.find_all('item')[0]
#                     entries = soup.find_all('title')[0]
#                     success_tags = "Creating separate key-value pairs for item tags"
#                     verbose_data.append(success_tags)
#                     # print(entries,"entrieslar soni")
#                 except:
#                     error_tags = "Unfortunately we could not find his item and feed parts through the link you provided"
#                     verbose_data.append(error_tags)
#         else:
#             no_link = "Link is not given"
#             verbose_data.append(no_link)

#     #print verbose data
#     for data_status in verbose_data:
#         print(date_info+" "+data_status)


# Gives information according to inputted limitation
def get_news():
    # try:
    link_args = get_args()
    data_dicts = []
    data_dict_json = []

    # check inputed url
    validating_url = "Validating URL " + "{}".format(link_args.source)
    # console.log(verbose_caches(validating_url),severe=True)

    verbose_caches(validating_url)

    if link_args.source and isValidURL(link_args.source) is True:
        validated_url = "URL validated successfully"
        verbose_caches(validated_url)
    else:
        validated_url = "URL validated not successfully"
        verbose_caches_error(validated_url)

    # extract data from link
    if link_args.source and (link_args.date is None):
        try:
            url_path = requests.get(link_args.source)
        except:
            print("please check the internet connection")
        try:
            soup = BeautifulSoup(url_path.content, 'xml')
            success_tags = "Creating separate key-value pairs for item tags"
            verbose_caches(success_tags)
        except:
            success_tags = "Unfortunately we could not find his item and feed parts through the link you provided"
            verbose_caches_error(success_tags)

        entries = soup.find_all('item')
        # print(entries,"entrieslar soni")
        if link_args.limit:
            status_limit = "{}".format(
                str(link_args.limit)) + " news were given"
            if link_args.limit >= len(entries):
                post_limit = len(entries)
            else:
                post_limit = link_args.limit
        else:
            status_limit = "Limit is not given"
            post_limit = len(entries)
        verbose_caches(status_limit)
        # gets only Feed!
        try:
            feed = soup.find_all('title')[0].text

        except:
            feed = None
        print(f"\n Feed: {feed}\n")

        title = None
        date = None
        link = None
        source = None
        description = None
        image_link = None
        creator = None
        enclosure = None
        for item in range(post_limit):
            # if content exists this utilty gets data else ignores tag
            if entries[item].title:
                title = entries[item].title.text
            if entries[item].pubDate:
                date = entries[item].pubDate.text
                date = date_parse.parse(date).strftime("%Y-%m-%d %H:%M:%S")
                # date = datetime.strptime(date,'%Y-%m-%d').strftime("%Y%m%d")
            if entries[item].link:
                link = entries[item].link.text
            if entries[item].source:
                source = entries[item].source['url']
            if entries[item].content:
                image_link = entries[item].content['url']

            if entries[item].creator:
                creator = entries[item].creator.text
            if entries[item].enclosure:
                enclosure = entries[item].enclosure['url']
            # if html tags appear in the description, then we can clear the data
            if entries[item].description:
                description = entries[item].description.text
                # Let's check if there is an html tag
                if "</" in str(description):
                    description_list = clean_desc(description)
                    description = ''.join(description_list)

            dict_data = {
                "title": title,
                "date": date,
                "link": link,
                "image_link": image_link,
                "description": description,
                "source": source,
                "creator": creator,
                "enclosure": enclosure,
            }
            # Removing the value which is None value and updating dict_data
            filtered = {k: v for k, v in dict_data.items() if v is not None}
            dict_data.clear()
            dict_data.update(filtered)
            # colleting information
            data_dicts.append(dict_data)
            published_date = date_parse.parse(date).strftime("%Y%m%d")
            data_dict_json.append(
                {"published": published_date, "News Item": dict_data, "source": link_args.source})
            sorted_data = []

    # only offline work
    elif link_args.date:
        parse_data = None
        # read data from base
        with open('database_file/data.json', "r", encoding='utf-8') as file:
            parse_data = json.loads(file.read())
            file.close()
        entries = parse_data

        if link_args.limit:
            status_limit = "{}".format(
                str(link_args.limit)) + " news were given"
            if link_args.limit >= len(entries):
                post_limit = len(entries)
            else:
                post_limit = link_args.limit
        else:
            status_limit = "Limit is not given"
            post_limit = len(entries)
        verbose_caches(status_limit)

        sorted_data = []
        # state not json
        if link_args.json is False:
            # sorted via data and source
            if link_args.source:
                if link_args.date != 1:
                    for data in parse_data:
                        if (link_args.source == data['source']) and (str(link_args.date) == str(data['published'])):
                            sorted_data.append(data)
                        else:
                            continue
                else:
                    for data in parse_data:
                        if (link_args.source == data['source']):
                            sorted_data.append(data)
                        else:
                            continue
            else:
                if link_args.date != 1:
                    for data in parse_data:
                        if str(link_args.date) == str(data['published']):
                            sorted_data.append(data)
                else:
                    for data in parse_data:
                        sorted_data.append(data)

            for data in sorted_data[:post_limit]:
                links = []
                image_link = []

                for k, v in data["News Item"].items():
                    # print key and value from dictionary data
                    print(f"{k}:{v}")

                    if isValidURL(v) == True and (k == "link" or k == "source"):
                        links.append(v)
                    if isValidURL(v) == True and (k == "image_link" or k == "enclosure"):
                        image_link.append(v)

                # printing data
                print("\nlinks: ")
                link_count = 0
                for element in links:
                    link_count += 1
                    print(f"[{link_count}] {element} (link)")
                for element in image_link:
                    link_count += 1
                    print(f"[{link_count}] {element} (image_link)")
                print("\n")

        # state json
        else:
            # sorted via source and date
            if link_args.source:
                # when date becomes values
                if link_args.date != 1:
                    for data in parse_data:
                        if (link_args.source == data['source']) and (str(link_args.date) == str(data['published'])):
                            sorted_data.append(data)
                # when date becomes not values
                else:
                    for data in parse_data:
                        if (link_args.source == data['source']):
                            sorted_data.append(data)

            # sorted via only date
            else:
                # when date becomes values
                if link_args.date != 1:
                    for data in parse_data:
                        if str(link_args.date) == str(data['published']):
                            sorted_data.append(data)
                # when date becomes not values
                else:
                    for data in parse_data:
                        sorted_data.append(data)
            # printed through function
            dict_to_json(sorted_data[:post_limit])

        if link_args.to_html:
            data_dicts_html = []
            for data in sorted_data[:post_limit]:
                data_dicts_html.append(data["News Item"])
            convert_to_html(data_dicts_html, link_args.to_html)
            verbose_caches(
                "The result for given date successfully convert to html")
        if link_args.to_pdf:
            data_dicts_html = []
            for data in sorted_data[:post_limit]:
                data_dicts_html.append(data["News Item"])
            convert_to_pdf(data_dicts_html, link_args.to_pdf)
            verbose_caches(
                "The result for given date successfully convert to pdf")

    else:
        # If the source and date do not match, the card will be empty
        sorted_data = []
        error_source = "source is not given or invalconvert_toid url"
        verbose_caches_error(error_source)

    # check the data avaiable
    if len(sorted_data) == 0:

        verbose_caches("No information on given date")
    else:
        verbose_caches("The result for given date successfully printed")

    # provided data
    if link_args.json is False and (link_args.date is None):
        for i in data_dicts:
            links = []
            image_link = []
            for k, v in i.items():
                # print key and value from dictionary data
                print(f"{k}:{v}")

                if isValidURL(v) == True and (k == "link" or k == "source"):
                    links.append(v)
                if isValidURL(v) == True and (k == "image_link" or k == "enclosure"):
                    image_link.append(v)

            # printing data
            print("\nlinks: ")
            link_count = 0
            for element in links:
                link_count += 1
                print(f"[{link_count}] {element} (link)")
            for element in image_link:
                link_count += 1
                print(f"[{link_count}] {element} (image_link)")

            print("\n")

        if link_args.to_html:
            convert_to_html(data_dicts, link_args.to_html)
            verbose_caches(
                "The result for given date successfully convert to html")
        if link_args.to_pdf:
            convert_to_pdf(data_dicts, link_args.to_pdf)
            verbose_caches(
                "The result for given date successfully convert to pdf")

    elif link_args.json is True and (link_args.date is None):
        if link_args.to_html:
            data_dicts_html = []
            for data in data_dict_json:
                data_dicts_html.append(data["News Item"])
            convert_to_html(data_dicts_html, link_args.to_html)
            verbose_caches(
                "The result for given date successfully convert to html")
        if link_args.to_pdf:
            data_dicts_html = []
            for data in data_dict_json:
                data_dicts_html.append(data["News Item"])
            convert_to_pdf(data_dicts_html, link_args.to_pdf)
            verbose_caches(
                "The result for given date successfully convert to pdf")
        dict_to_json(data_dict_json)
        # request
    if link_args.date is None:
        # save to local storage
        with open('database_file/data.json', 'r+', encoding='utf-8') as file:
            data = json.loads(file.read())
            print("please wait a while the backup process may take some time!")
            verbose_caches_error(
                "please wait a while the backup process may take some time!")
        #     # file.close()
        # local storage save image
            for img in data_dict_json:
                fileName = f'local_image_url/dwnldimagepath{uuid4()}.jpg'
                key = 'image_link'
                if key in img['News Item']:
                    req = requests.get(img['News Item']['image_link'])
                # print(req.iter_content(100000),"req nima u akalr")
                    file_image = open(fileName, 'wb')
                    for chunk in req.iter_content(100000):
                        file_image.write(chunk)
                    file_image.close()
                    img['News Item'].update({"image_link_local": fileName})

            # check news exists in database
            for news in data_dict_json:
                check_exists_data_in_local_storage = True
                if len(data) != 0:
                    for item in data:
                        if news["News Item"]['title'] == item["News Item"]['title']:
                            check_exists_data_in_local_storage = False
                    if check_exists_data_in_local_storage:
                        data.append(news)
                else:
                    data.append(news)
            file.seek(0)

            json.dump(data, file, ensure_ascii=False, indent=4)
            file.close()


def dict_to_json(data_dict_json):
    json_args = get_args()
    if json_args.json:
        verbose_caches("Data succussfully converted into json")
        for i in data_dict_json:
            # dict to json and print result
            print(json.dumps(i, ensure_ascii=False), "\n")


# print version
def get_version():

    if get_args().version:
        print(VERSION_INFO)


def main():
    check_database_avaiable()
    local_img_storage()
    get_version()
    get_news()


if __name__ == '__main__':
    main()
    
