from setuptools import find_packages, setup
import os

# Optional rss_reader_package description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(
            os.path.join(current_directory, "../README.md"),
            encoding="utf-8") as f:
        long_description = f.read()
except Exception as e:
    print(e)
    long_description = ""
setup(
    # Project name:
    name="RSS Reader",

    # Packages to include in the distribution:
    packages=find_packages(','),

    # Project version number:
    version="1.5.0",

    # List a license for the project, eg. MIT License
    license="MIT License",

    # Short description of your library:
    description="Pure Python command-line RSS reader",

    # Long description of your library:
    long_description=long_description,
    long_description_content_type='text/markdown',

    # Your name:
    author="Narek Arsenyan",

    # Your email address:
    author_email="narekarsenyan99@gmail.com",

    # Link to your github repository or website:
    url="https://github.com/NMac99",

    # Download Link from where the project can be downloaded from:
    download_url="",

    # List of keywords:
    keywords=[],

    # List project dependencies:
    install_requires=["appdirs", "yattag", "EbookLib", "beautifulsoup4", "requests"],

    # https://pypi.org/classifiers/
    classifiers=[],
    entry_points={"console_scripts": [
            "rss-reader=rss_reader_package.rss_reader:rss_reader_func"
        ]}
    )
