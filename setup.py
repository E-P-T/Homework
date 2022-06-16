import os
from setuptools import find_packages, setup

def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name='RSS_reader',
    version='2.1',
    license='',
    description='Really good lib',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    python_requires=">=3.9",
    classifiers=["Programming Language :: Python :: 3.9"],
    author='Doniyor Karimov',
    author_email='doniyorkarimoff96@gmail.com',
    url='github.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rss_reader=rss_reader:read_defs'
        ]
    },
    download_url='https://github.com/karimoff96/Homework',
    keywords=['rss_reader'],
    include_package_data=True,
    install_requires=read("requirements.txt").splitlines(),
    zip_safe=False,
)
