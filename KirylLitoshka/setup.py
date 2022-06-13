from setuptools import setup, find_packages

setup(
    name="rss_parser",
    version=1.2,
    author="Kiryl Litoshka",
    author_email="kirill.litoshko@gmail.com",
    description='Python RSS Parser',
    # long_description=open('README.txt').read(),
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.11.1",
        "bs4==0.0.1",
        "certifi==2022.5.18.1",
        "charset-normalizer==2.0.12",
        "coverage==6.4.1",
        "idna==3.3",
        "requests==2.28.0",
        "soupsieve==2.3.2.post1",
        "urllib3==1.26.9"
    ],
    entry_points={
        'console_scripts': [
            'rss_parser=rss_parser.main:main'
        ],
    }
)
