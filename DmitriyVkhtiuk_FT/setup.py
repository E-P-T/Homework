from setuptools import setup, find_packages

package_data = \
    {'': ['*']}

with open("requirements.txt", "r", encoding="utf-8") as reqs:
    requirements = reqs.read()
entry_points = \
    {'console_scripts': ['rss_reader = rss_reader.rss_reader:main']}

setup_kwargs = {
    'name': 'rss-reader',
    'version': 1.4,
    'description': 'A simple CLI rss reader',
    'author': 'DVikhtiuk',
    'author_email': 'dimastol1ca@gmail.com',
    'packages': find_packages(),
    'package_data': package_data,
    'install_requires': requirements,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}

setup(**setup_kwargs)
