import os
from setuptools import find_packages, setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()
setup(
    name="rss_reader",
    version="4.0",
    author="Maya Voyshnis",
    author_email="vvvoyshnism@gmail.com",
    description='Python RSS Parser',
    # long_description=open('README.txt').read(),
    packages=find_packages(),
    install_requires=[
        "wheel",
        "setuptools",
        "argparse",
        "requests",
        "beautifulsoup4",
        "python-dateutil",
        "loguru"
    ],
    entry_points={
        'console_scripts': [
            'rss_reader=rss_reader.main:main'
        ],
    }
)
