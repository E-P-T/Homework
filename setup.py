from setuptools import setup

setup(
    name='rss_reader',
    version='2.0',
    py_modules=['rss_reader'],
    install_requires=[
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'certifi==2022.5.18.1',
        'charset-normalizer==2.0.12',
        'idna==3.3',
        'lxml==4.9.0',
        'python-dateutil==2.8.2',
        'requests==2.28.0',
        'six==1.16.0',
        'soupsieve==2.3.2.post1',
        'urllib3==1.26.9'
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader:main'
        ]
    }
)
