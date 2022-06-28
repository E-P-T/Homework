from bs4 import BeautifulSoup
from uuid import uuid4
from json2html import *
import os
import requests
from database_file.check_database import check_database_avaiable
check_database_avaiable()
url = "https://www.epam.com/"
timeout = 5

try:
    request = requests.get(url, timeout=timeout)
    online = True
except (requests.ConnectionError, requests.Timeout) as exception:
    online = False

with open('template/beautiful_news.html', 'r', encoding='utf-8') as readfile:
    html_file = readfile.read()

soup = BeautifulSoup(html_file, "html.parser")
readfile.close()


def convert_to_html(dataset, filename=None):
    for data in dataset:
        print()
        main_div = soup.new_tag('div', **{'class': 'card mb-3'})
        body_div = soup.new_tag('div', **{'class': 'card-body'})
        p_tag_small = soup.new_tag('p', **{'class': 'card-text'})
        body_div.append(p_tag_small)
        for k, v in data.items():

            # print(data,'\n')
            if online:
                img_source = "image_link"
                if k == img_source:
                    img_tag = soup.new_tag(
                        "img", **{'class': 'card-img-top'}, src=v, alt="No image link")
                    main_div.append(img_tag)
            else:
                img_source = "image_link_local"
                if k == img_source:
                    img_tag = soup.new_tag(
                        "img", **{'class': 'card-img-top'}, src=f"../{v}", alt="No image link")
                    main_div.append(img_tag)

            if k == 'title':
                title_h5 = soup.new_tag('h5', **{'class': 'card-title'})
                title_h5.string = v
                body_div.append(title_h5)
            if k == "description":
                p_tag = soup.new_tag('p', **{'class': 'card-text'})
                p_tag.string = v
                body_div.append(p_tag)

            if k == "link":
                small_tag_link = soup.new_tag(
                    'a', **{'class': 'text-muted'}, href=v)
                small_tag_link.string = v
                p_tag_small.append(small_tag_link)
                br = soup.new_tag('br')
                p_tag_small.append(br)
            if k == "date":
                small_tag_date = soup.new_tag(
                    'span', **{'class': 'text-muted'})
                small_tag_date.string = v
                p_tag_small.append(small_tag_date)
                br = soup.new_tag('br')
                p_tag_small.append(br)
            if k == "source":
                small_tag_source = soup.new_tag(
                    'a', **{'class': 'text-muted'}, href=v)
                small_tag_source.string = v
                p_tag_small.append(small_tag_source)
                br = soup.new_tag('br')
                p_tag_small.append(br)
            if k == "creator":
                small_tag_creator = soup.new_tag(
                    'small', **{'class': 'text-muted'})
                small_tag_creator.string = v
                p_tag_small.append(small_tag_creator)
                br = soup.new_tag('br')
                p_tag_small.append(br)
            if k == "enclosure":
                small_tag_enclosure = soup.new_tag(
                    'small', **{'class': 'text-muted'}, href=v)
                small_tag_enclosure.string = v
                p_tag_small.append(small_tag_enclosure)

        main_div.append(body_div)
        # print(main_div,"\n")
        soup.body.div.append(main_div)
    if '/' in str(filename):
        new_folder = filename.split('/')[0]
        file = filename.split('/')[1]
        if '.html' == file[-5:]:
            pass
        else:
            file += '.html'
    else:
        new_folder = 'html_files'
        file = str(filename)
        if '.html' == file[-5:]:
            pass
        else:
            file += '.html'
    try:
        os.mkdir(new_folder)
    except:
        pass
    try:
        if filename:
            with open(f'{new_folder}/{file}', 'w', encoding='utf-8') as writefile:
                writefile.write(str(soup))
                writefile.close()
            print(
                "\n", f"your html file has been successfully saved in the {new_folder} file with the name {file}", "\n")
        else:
            with open('html_files/rss_news.html', 'w', encoding='utf-8') as writefile:
                writefile.write(str(soup))
                writefile.close()
            print("\n", "your html file has been successfully saved in the html_files file with the name rss_news", "\n")
        
        return "OK"
    except Exception as e:
        return e
