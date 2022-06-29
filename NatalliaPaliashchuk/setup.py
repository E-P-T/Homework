import os
from setuptools import setup
from rss_reader import *

os.system('pip install -r requirements.txt')

with open('README.md', encoding="utf8") as readme:
    read_me_description = readme.read()

setup(
    name='rss_reader',
    description='CLI RSS-reader',
    long_description=read_me_description,
    long_description_content_type='text/markdown',
    author=__author__,
    packages=['rss_reader'],
    package_data={'rss_reader': ['templates/*']},
    python_requires='>=3.9',
    entry_points={'console_scripts': ['rss_reader = rss_reader.run:run']})
