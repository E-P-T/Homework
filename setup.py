from setuptools import setup

setup(
    name='rss_reader',
    version='2.0',
    py_modules=['rss_reader'],
    install_requires=[
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'certifi==2022.6.15',
        'charset-normalizer==2.1.0',
        'defusedxml==0.7.1',
        'fpdf2==2.5.5',
        'idna==3.3',
        'lxml==4.9.0',
        'Pillow==9.1.1',
        'python-dateutil==2.8.2'
        'requests==2.28.1',
        'soupsieve==2.3.2.post1',
        'urllib3==1.26.9',
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader:main'
        ]
    }
)
