from reportlab.pdfgen import canvas
import os
import textwrap
import datetime


info = "News successfully converted and saved into 'pdf_convert' directory with 'local datetime' name"
def convert_to_pdf(infoFromJson, date=None):
    '''Method of data convertion into html'''
    folder = 'pdf_convert'
    if os.path.exists(folder):
        pass
    else:
        os.mkdir(folder)
    if date:
        file = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+'(offline)'+'.pdf'
    else:
        file = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")+'(online)'+'.pdf'
    can = canvas.Canvas(f'PDF_convert/{file}')
    dir_path = "img_storage"
    for item in infoFromJson:
        x = 10
        y = 800
        for k, v in item.items():
            img_source = "img_storage"
            if img_source in item:

                img_name= item[img_source].split('/')[-1]
                can.drawImage(f"{dir_path}/{img_name}"+'.jpeg', 30, 300, width=250, height=200)
            text = f"{k}: {v}"
            wrap_text = textwrap.wrap(text, width=100)
            can.drawString(x, y, wrap_text[0])
            try:
                y -= 25
                can.drawString(x+50, y, wrap_text[1])
            except:
                pass

            y -= 25

        can.showPage()

    can.save()
    print("\n", info, "\n")

