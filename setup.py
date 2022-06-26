from setuptools import setup, find_packages

import src.info as info

setup(
    name=info.shortname,
    version=info.version,
    package_dir={'': 'src'},
    packages=find_packages().append(''),
    install_requres=[
        'colorama',
        'Pillow',
        'python_dateutil'
    ],
    entry_points={
        'console_scripts': [
            'rss_reader = rss_reader:main',
        ]
    }
)
