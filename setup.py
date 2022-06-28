import os
from setuptools import find_packages, setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


# requirements = read('requirements.txt')

# entry_points = {'gui_scripts': ['rss_reader=rss_reader:main']}
entry_points = {'console_scripts': ['rss_reader=rss_reader:main']}


# if os.name == "nt":
#     entry_points = {'console_scripts': ['rss_reader=rss_reader:main']}

setup(
    name='RSS_reader',
    version='4.3.0',
    # license='',
    description="RSS-reader, which can help you to read news "
                "from the source you will give it.",
    # long_description=read("README.md"),
    long_description_content_type='text/markdown',
    python_requires=">=3.8",
    classifiers=["Programming Language :: Python :: 3.9"],
    author='Boburbek Botirov',
    author_email='BoburbekBotirov868@gmail.com',
    url='https://github.com/Boburshoh-oss/Final_task/',
    packages=find_packages(),
    entry_points=entry_points,
    # download_url='https://github.com/Boburshoh-oss/Final_task/',
    keywords=['rss reader', 'rss reader modul'],
    include_package_data=True,
    install_requires=['autopep8==1.6.0', 'beautifulsoup4==4.11.1', 'build==0.8.0', 'certifi==2022.5.18.1', 'charset-normalizer==2.0.12', 'colorama==0.4.4', 'cycler==0.11.0', 'fonttools==4.33.3', 'fpdf==1.7.2', 'idna==3.3', 'JPype1==1.4.0', 'json2html==1.3.0', 'kiwisolver==1.4.3', 'ldap3==2.9.1', 'lxml==4.9.0', 'matplotlib==3.5.2', 'numpy==1.23.0', 'packaging==21.3', 'pandas==1.4.3',
                      'pdf-writer==0.1', 'pdfkit==1.0.0', 'pdfrw==0.4', 'pep517==0.12.0', 'Pillow==9.1.1', 'py-console==0.1.4', 'pyasn1==0.4.8', 'pycodestyle==2.8.0', 'pydirectory==0.1.15', 'pyparsing==3.0.9', 'pyPdf==1.13', 'python-dateutil==2.8.2', 'pytz==2022.1', 'reportlab==3.6.10', 'requests==2.27.1', 'six==1.16.0', 'soupsieve==2.3.2.post1', 'toml==0.10.2', 'tomli==2.0.1', 'urllib3==1.26.9'],
    zip_safe=False,
)
