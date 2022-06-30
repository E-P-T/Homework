import os
from setuptools import find_packages, setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name='RSS_reader',
    version='2.0.0',
    description='Pure Python command-line RSS reader.',
    long_description=read("README.md"),
    python_requires=">=3.7",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent",
                 "License :: OSI Approved :: MIT License"],
    author='Sardorbek Bobomurodov',
    author_email='sardorbekbobomurodov.sh@gmail.com',
    url='https://github.com/sardords/Homework',
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={'console_scripts': ['rss_reader=rss_reader:main']},
    keywords=['Rss_reader'],
    install_requires=['beautifulsoup4 == 4.11.1',
                      'lxml == 4.9.0',
                      'py-console == 0.1.4',
                      'requests == 2.28.0',
                      'python-dateutil==2.8.2', ],
)
