from setuptools import setup, find_packages

setup(
    name="rss_parser",
    version="1.3",
    author="Kiryl Litoshka",
    author_email="kirill.litoshko@gmail.com",
    description='Python RSS Parser',
    # long_description=open('README.txt').read(),
    packages=find_packages(),
    install_requires=[
        "wheel",
        "setuptools",
        "argparse",
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        'console_scripts': [
            'rss_parser=rss_parser.main:main'
        ],
    }
)
