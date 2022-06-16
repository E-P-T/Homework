from setuptools import setup

setup(
    name="rss_reader",
    version="2.1",
    author="Alena Kniazeva",
    author_email="elena.n.kniazeva@gmail.com",
    description="RSS-reader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'requests>=2.26.0',
    'lxml>=4.9.0',
    'beautifulsoup4>=4.11.1'
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader:main',
        ],
    }
)