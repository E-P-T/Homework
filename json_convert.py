# importing the required module
import pdfkit
import os
import tempfile
from shutil import which
import sys
import os


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


# config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
options = {"enable-local-file-access": None, "quiet": ""}


def convert_to_pdf():
    # converting html file to pdf file
    # running for windows
    if get_platform() == "Windows":
        config = pdfkit.configuration(
            wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfkit.from_file('html_files/rss_news.html', 'pdf_files/output.pdf',
                         configuration=config, options=options, verbose=True)
        print("your pdf file has been saved in the 'pdf_files' folder as 'output.pdf'")
    # running for linux
    elif get_platform() == "Linux":
        pdfkit.from_file('html_files/rss_news.html',
                         'pdf_files/output.pdf', options=options, verbose=True)
        print("your pdf file has been saved in the 'pdf_files' folder as 'output.pdf'")


# apt-get install wkhtmltopdf
