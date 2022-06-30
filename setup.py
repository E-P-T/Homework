from setuptools import setup, find_packages
from rssreader import cnf

setup(
    name=cnf.__package__,
    version=cnf.__version__,
    description="command-line RSS reader",
    long_description="All information in the Readme",
    author="Qayumjon Ergashaliyev",
    author_email="king97queen99@gmail.com",
    packages=find_packages(),
    python_requires=">=3.9.6",
    install_requires=[
        "bs4", "feedparser", "nose", "pymongo", "coverage",
        "fpdf", "requests", "colored"],
    entry_points={
        "console_scripts":
            [f"{cnf.__package__} = rssreader.__main__:main"]
        }
)
