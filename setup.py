# import setuptools
from setuptools import setup, find_packages

with open("README.md") as file:
    read_me_description = file.read()

setup(
    name="rss_reader",
    version="0.0.2",
    author="Andrey Ozerets",
    description="Super rss-reader.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader.__main__:main',
        ]
    },
    install_requires=[
        "requests==2.28.0",
        "beautifulsoup4 == 4.11.1",
        "lxml==4.9.0",
    ],
    # packages=['FT'],
    packages=find_packages(exclude=['test*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
