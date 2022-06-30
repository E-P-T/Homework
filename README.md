RSS reader
=========

This is RSS reader version 4.0.

rss_reader.py is a python script intended to get RSS feed from given source URL
and write its content to standart output also it's can convert content to .json and .html files.


To use this script you  should install all required packages from requirements.txt
```shell
pip install {name of package}
```



How to execute after installation
------

Specifying the script file. Run from directory with rss_reader.py file the following command


Windows
```shell
python rss_reader.py ...
```

Linux
```bash

python3 rss_reader.py ...
```

Command line format
-------

	usage: python rss_reader.py [-h] [-v] [--json] [--verbose] [--limit LIMIT] [--date DATE] [--to-html ]
						 source

	Pure Python command-line RSS reader.

	positional arguments:
	  source               RSS URL

	optional arguments:
	  -h, --help           show this help message and exit
	  --version            Print version info
	  --json               Print result as JSON
	  --verbose            Outputs verbose status messages. Prints logs.
	  --limit LIMIT        Limit news topics. If it's not specified, then you get all available feed.

	  --date DATE          It should take a date in %Y%m%d format.The new from the specified day will be printed out.
	  --html         It convert data to HTML-format in file output.html.

Сonsole representation
-------

```json
Name of the feed
Title from news
PubDate

Summary description

Source link

------------
Title from news
PubDate
...
.....


```
JSON representation
-------

```json
{
    "name": Name of the feed,
    "size": Number of available news,
    "title": [Names of available news],
    "pubDate": [Dates of publication news],
    "description": [Summary description],
    "link": [Link of source]
}
```

Cache storage format
------

News cache is stored in file data.json in current working directory.


Command example
------


```shell
python rss_reader.py "https://www.onliner.by/feed" --limit 1 --html

python rss_reader.py "https://www.buzzfeed.com/quizzes.xml" --limit 2 --json --verbose

python rss_reader.py "https://www.buzzfeed.com/quizzes.xml" --limit 3

python rss_reader.py  "https://feeds.fireside.fm/bibleinayear/rss" --limit 3 --verbose

python rss_reader.py --date 20220620
```