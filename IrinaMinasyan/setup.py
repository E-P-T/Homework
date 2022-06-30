from setuptools import setup

setup(
    name="rss_reader",
    version="1.5",
    author="Irina Minasyan",
    author_email="irina71757@gmail.com",
    description="RSS-reader, which can help you to read news "
                "from the source you will give it.",
    install_requires=['requests', 'bs4', 'html2text', 'pytest',  'python-dateutil', 'dominate', 'fpdf2'],

    packages=['reader'],
    python_requires='>=3.6',
    entry_points={
       'console_scripts': ['rss_reader=reader.rss_reader:main']
    },
    include_package_data=True,
)
