from setuptools import setup, find_packages

from src.info import shortname, version

setup(
    name=shortname,
    version=str(version),
    package_dir={'': 'src'},
    packages=find_packages('src').append(''),
    install_requires=[
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader:main',
        ]
    }
)
