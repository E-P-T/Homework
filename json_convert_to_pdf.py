# method 1
from database_file.check_database import check_database_avaiable
from reportlab.pdfgen import canvas
import os
import requests
import textwrap

url = "https://www.epam.com/"
timeout = 5

try:
    request = requests.get(url, timeout=timeout)
    online = True
except (requests.ConnectionError, requests.Timeout) as exception:
    online = False

check_database_avaiable()
# with open('data.json', "r",encoding='utf-8') as file:
#     infoFromJson = json.loads(file.read())


def convert_to_pdf(infoFromJson, filename=None):
    if '/' in str(filename):

        new_folder = filename.split('/')[0]
        file = filename.split('/')[1]

        if '.pdf' == file[-4:]:
            pass
        else:
            file += '.pdf'
    else:
        new_folder = 'pdf_files'
        file = str(filename)
        if '.pdf' == file[-4:]:
            pass
        else:
            file += '.pdf'
    try:
        os.mkdir(new_folder)
    except:

        pass
    try:
        if filename:
            can = canvas.Canvas(f'{new_folder}/{file}')
            info = f"your pdf file has been successfully saved in the {new_folder} file with the name {file}"
        else:
            can = canvas.Canvas('pdf_files/news_rss.pdf')
            info = "your pdf file has been successfully saved in the pdf_files file with the name news_rss.pdf"

        for item in infoFromJson:
            x = 10
            y = 800
            # print(item,"nimaga hato")
            for k, v in item.items():
                if online:
                    img_source = "image_link"
                else:
                    img_source = "image_link_local"
                if img_source in item:
                    can.drawImage(item[img_source], 30, 300, width=100, height=100)
                text = f"{k}: {v}"
                wrap_text = textwrap.wrap(text, width=100)
                can.drawString(x, y, wrap_text[0])
                try:
                    y -= 25
                    can.drawString(x+50, y, wrap_text[1])
                except:
                    pass
                # wraped_text = "\n".join(wrap(text, 30)) #
                # t.textLines(wraped_text)
                # print(wraped_text,"ko'rsat it")

                # can.drawString(x, y, wrap_text[1])
                y -= 25

            can.showPage()

        can.save()
        print("\n", info, "\n")
        return "OK"
    except Exception as e:
        return e

# create_pdf(infoFromJson,"hajme/pjmawdawe")
