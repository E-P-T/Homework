import os
from json2html import *
from bs4 import BeautifulSoup
import datetime


with open('base.html', 'r', encoding='utf-8') as readfile:
    html_file = readfile.read()

soup = BeautifulSoup(html_file, "html.parser")
readfile.close()


def convert_to_html(dataset,date=None):
     '''Method of data convertion into html'''
     for data in dataset:
          main_div = soup.new_tag('div', **{'class': 'card mb-3 em'})
          body_div = soup.new_tag('div', **{'class': 'card-body'})
          tag_p = soup.new_tag('p', **{'class': 'card-text'})
          body_div.append(tag_p)
          for key, value in data.items():
               if date:
                    img_source = "News image_link:"
                    if key == img_source:
                         img_tag = soup.new_tag(
                         "img", **{'class': 'card-img-top'}, src=value, alt="No image link")
                         main_div.append(img_tag)
               else:
                    dir_path = "img_storage"
                    # list to store files
                    res = []
                    # Iterate directory
                    for path in os.listdir(dir_path):
                    # check if current path is a file
                         if os.path.isfile(os.path.join(dir_path, path)):
                              res.append(path)
                    if key == 'News image_link:':
                         img_name = value.split('/')[-1]
                         for i in res:
                              if img_name == i[:-5]:
                                   img_tag = soup.new_tag(
                                       "img", **{'class': 'card-img-top'}, src=f"../{dir_path}/{img_name}.jpeg", alt="No image link")
                                   main_div.append(img_tag)
               if key == 'News title:':
                    title_h5 = soup.new_tag('h5', **{'class': 'card-title'})
                    title_h5.string = value
                    body_div.append(title_h5)
               if key == "News description:":
                    p_tag = soup.new_tag('p', **{'class': 'card-text'})
                    p_tag.string = value
                    body_div.append(p_tag)
               if key == "News link:":
                    small_tag_link = soup.new_tag(
                         'a', **{'class': 'text-muted links'}, href=value)
                    small_tag_link.string = value
                    tag_p.append(small_tag_link)
                    tag_p.append(soup.new_tag('br'))
               if key == "News date:":
                    small_tag_date = soup.new_tag(
                         'span', **{'class': 'text-muted'})
                    small_tag_date.string = value
                    tag_p.append(small_tag_date)
                    tag_p.append(soup.new_tag('br'))
               if key == "News source:":
                    small_tag_source = soup.new_tag(
                         'a', **{'class': 'text-muted links'}, href=f"{value} <br>")
                    small_tag_source.string = value
                    tag_p.append(small_tag_source)
                    tag_p.append(soup.new_tag('br'))
               if key == "News creator:":
                    small_tag_creator = soup.new_tag(
                         'small', **{'class': 'text-muted'})
                    small_tag_creator.string = value
                    tag_p.append(small_tag_creator)
               if key == "News enclosure:":
                    small_tag_enclosure = soup.new_tag(
                         'small', **{'class': 'text-muted'}, href=value)
                    small_tag_enclosure.string = value
                    tag_p.append(small_tag_enclosure)
          body_div.append(tag_p)
          main_div.append(body_div)
          soup.body.div.append(main_div)
          folder = 'html_convert'
          if date:
              file = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+'(online)'+'.html'
          else:
              file = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+'(offline)'+'.html'
          if os.path.exists(folder):
               pass
          else:
               os.mkdir(folder)
          with open(f'{folder}/{file}', 'w', encoding='utf-8') as writefile:
               writefile.write(str(soup))
               writefile.close()
               print("\n", f"your html file has been successfully saved in the {folder} file with the name {file}", "\n")
