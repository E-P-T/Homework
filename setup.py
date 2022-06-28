from setuptools import setup, find_packages

import re

VERSION_FILE = 'rss_parse/__init__.py'


def version():
    _version_re = re.compile(r'^\s*__version__\s*=\s*[\'"](.*)[\'"]\s*$')

    with open(VERSION_FILE, 'r') as f:
        res = _version_re.search(f.read())
        if res is None:
            raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")
        ver = res.group(1)

    return ver


setup(
    name='rss_reader',
    version=version(),
    description='Pure Python command-line RSS reader.',
    author='Aleksandra Khorosheva',
    zip_safe=False,
    author_email='alexa.horoschewa@gmail.com',
    keywords=['RSS Reader', 'RSS Feed Parser'],
    install_requires=[
        'setuptools~=57.0.0',
        'requests~=2.27.1',
        'xmltodict~=0.13.0',
        'python-dateutil~=2.8.0',
        'html2text>=2020.1.16',
    ],
    python_requires=">=3.9",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rss_reader=rss_parse.rss_reader:main_wrapper',
        ],
    },
)
