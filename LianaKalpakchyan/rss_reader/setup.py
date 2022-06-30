#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="rss_reader",
    version="0.4.0",
    description=" Python RSS-reader",
    author="Liana Kalpakchyan",
    author_email="kalpakchyanliana@gmail.com",
    install_requires=['argparse',
                      'requests',
                      'bs4',
                      'dateparser',
                      'datetime',
                      'lxml',
                      'xhtml2pdf',
                      'html5lib'
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['rss_reader=rss_reader.rss_reader:main']
    },
)

