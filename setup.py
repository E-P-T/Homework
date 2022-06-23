from setuptools import setup, find_packages

setup(
    name="rss_reader",
    version="1.2.0",
    description="Simple RSS-reader for console use.",
    author="Farrukh Nurmatov",
    packages=find_packages(),
    install_requires=["beautifulsoup4>=4.11.1",
                      "bs4>=0.0.1",
                      "certifi>=2022.6.15",
                      "charset-normalizer>=2.0.12",
                      "idna>=3.3",
                      "lxml>=4.9.0",
                      "requests>=2.28.0",
                      "soupsieve>=2.3.2.post1",
                      "urllib3>=1.26.9"
                      ],
    python_requires=">=3.9",
    entry_points={
        'console_scripts':
            ['rss_reader = '
             'rss_reader.rss_reader:main', ]}
    )
