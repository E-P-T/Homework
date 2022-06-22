import os
from setuptools import find_packages, setup
def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()

setup(
    name='RSS_reader',
    version='2.2',
    license='',
    description='Really good lib',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3.10"],
    author='Doniyorbek Karimov',
    author_email='doniyorkarimoff96@gmail.com',
    url='https://github.com/karimoff96/Final-task',
    packages=find_packages(),
    entry_points={'console_scripts': ['rss_reader=rss_reader:read_defs']},
    download_url='www.pypi.com',
    keywords=['Rss_reader'],
    include_package_data=True,
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
                      'validators == 0.20.0'],
    zip_safe=False,
)
