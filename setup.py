import os
from setuptools import find_packages, setup
def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name='RSS_reader',
    version='4.3',
    description='python rss_reader, helps to read and get information from xml and rss formatted urls ',
    long_description=read("README.md"),
    python_requires=">=3.7",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent",
                 "License :: OSI Approved :: MIT License"],
    author='Doniyorbek Karimov',
    author_email='doniyorkarimoff96@gmail.com',
    url='https://github.com/karimoff96/Final-task',
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={'console_scripts': ['rss_reader=rss_reader:read_defs']},
    keywords=['Rss_reader'],
    # install_requires=read("requirements.txt").splitlines(),
    install_requires=['beautifulsoup4 == 4.11.1',
                      'certifi == 2022.5.18.1',
                      'charset-normalizer == 2.0.12',
                      'colorama == 0.4.4',
                      'decorator == 5.1.1',
                      'idna == 3.3',
                      'lxml == 4.9.0',
                      'py-console == 0.1.4',
                      'requests == 2.28.0',
                      'soupsieve == 2.3.2.post1',
                      'urllib3 == 1.26.9',
                      'validators == 0.20.0',
                      'python-dateutil==2.8.2',
                      'reportlab==3.6.10',
                      'json2html==1.3.0',
                      ],
)
