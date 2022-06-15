from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    description = readme.read()

with open("requirements.txt", "r", encoding="utf-8") as reqs:
    requirements = reqs.read()


setup(
    name='rss-reader',
    version='1.4',
    author='Uladzimir Fiodarau',
    author_email='ufiodarau@gmail.com',
    description='Python RSS parser',
    long_description=description,
    packages=find_packages(),
    package_data={'': ['*.txt', '*.xml']
                  },
    install_requires=[requirements],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'rss_reader=rss_reader.rss_reader:main',
        ],
    },
)
