RSS reader
=========

This is RSS reader version 1.0.

rss_reader.py is a python script intended to get RSS feed from given source URL
and write its content to standart output.

Please be carefull with redirecting output to files. In this case CPython implementation
of Python interpreter will change encoding from UTF-8 to
the system locale encoding (i.e. the ANSI codepage).

This script will try to install all required packages from PyPI with pip in
the current environment.

Tests
------

To launch tests run

on Windows

```shell
python -m unittest tests.py
```

on Linux 

```bash
python3 -m unittest tests.py
```

To check test coverage run

on Windows

```shell
python -m coverage run --source=rss_reader -m unittest tests.py
python -m coverage report -m
```

on Linux

```bash
python3 -m coverage run --source=rss_reader -m unittest tests.py
python3 -m coverage report -m
```

All specified above commands should be used when current directory is the directory with rss_reader.py

How to execute without installation
------

Before installation there are two ways to start RSS reader

1. Using module loading. Run from directory with rss_reader.py file the following command

	on Windows

	```shell
	python -m rss_reader ...
	```

	on Linux

	```bash
	python3 -m rss_reader ...
	```

2. Specifying the script file. Run from directory with rss_reader.py file the following command

	on Windows

	```shell
	python rss_reader.py ...
	```

	on Linux

	```bash
	python3 rss_reader.py ...
	```

Installation
------

To install the script as site-package to python environment run the following command

on Windows

```shell
python setup.py install
```

on Linux

```bash
python3 setup.py install
```

How to execute after installation
------

Before installation there are three ways to start RSS reader

1. Using module loading. Run from any directory

	on Windows

	```shell
	python -m rss_reader ...
	```

	on Linux

	```bash
	python3 -m rss_reader ...
	```

2. Specifying the script file. Run from directory with rss_reader.py file the following command

	on Windows

	```shell
	python rss_reader.py ...
	```

	on Linux

	```bash
	python3 rss_reader.py ...
	```

3. Using entry point. Run from any directory

	```shell
	rss_reader ...
	```

Command line format
-------

    usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                        source

    Pure Python command-line RSS reader.

    positional arguments:
    source         RSS URL

    optional arguments:
    -h, --help     show this help message and exit
    --version      Print version info
    --json         Print result as JSON in stdout
    --verbose      Outputs verbose status messages
    --limit LIMIT  Limit news topics if this parameter provided


JSON representation
-------

```json
{
 "title": Title of the feed,
 "link": URL of feed,
 "description": Description of the feed,
 "items": [
  {
   "title": Item title if present,
   "pubDate": Publication date if present,
   "link": URL of the item if present,
   "description": Description of the item,
   "links": [
    [
     Link URL,
     Link type
    ],
    ...
   ]
  },
  ...
 ]
}
```
