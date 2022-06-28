from setuptools import setup, find_packages

setup(
    name='rss_reader',
    version='1.0',
    url='https://github.com/rubenispiryan/Homework/blob/final_task/',
    author='Ruben Ispiryan',
    packages=['rss_reader_pckg', 'rss_reader_pckg.rss', 'rss_reader_pckg.tests'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml',
    ],
    entry_points={'console_scripts': ['rss_reader=rss_reader_pckg.rss_reader:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
