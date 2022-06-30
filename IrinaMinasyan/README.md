## RSS_Reader
RSS reader is a command-line utility which receives RSS URL and prints results in human-readable format.

**Utility provides the following interface:**

```
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     [--date DATE] [--to_html TO_HTML] [--to_pdf TO_PDF]
                     [source]
Performs a variety of operations on a file.

positional arguments:
  source             RSS URL
  
optional arguments:
  -h, --help         show this help message and exit.
  --version          Print version info.
  --json             Print result as JSON in stdout.
  --verbose          Outputs verbose status messages.
  --limit LIMIT      Limit news topics if this parameter provided.
                     In case of --limit greater than amount of received news - all available news will be displayed.               
  --date DATE        Read cached news for provided URL. If not provided source prints all cached news for this date.
                     It takes a date in %Y%m%d format.              
  --to-html TO_HTML  Converts news to html format and save it.
  --to-pdf TO_PDF    Convert news to pdf format and save it.
```

## Requirements

The API was created using Python 3.6. To run the APP you need to install with pip packages listed in [requirements.txt]
(better to use virtual environment):

```
pip install -r requirements.txt
```

## Usage of RSS-reader

For usage the utility use followed option:

clone current repository and install the requirements (see the description above), it's better to use isolated environment with virtualenv. 
The entire application is contained within the rss_reader.py file. For running the utility use previously listed command line arguments. For example:

```
rss_reader https://news.yahoo.com/rss/ --limit 3
```

The output would be the following structure:

```
Title: WNBA star Brittney Griner ordered to trial Friday in Russia

Date: 2022-06-27T07:41:55Z

Link: https://news.yahoo.com/us-basketball-star-griner-due-074155275.html

Article: MOSCOW (AP) — Shackled and looking wary, WNBA star Brittney Griner was ordered
Monday to stand trial by a court near Moscow on cannabis possession charges,
about 4 1/2 months after her arrest at an airport while returning to play for
a Russian team.
The Phoenix Mercury center and two-time U.S. Olympic gold medalist also was
ordered to remain in custody for the duration of her criminal trial, which was
to begin Friday. Griner could face 10 years in prison if convicted on charges
of large-scale transportation of drugs. Fewer than 1% of defendants in Russian
criminal cases are acquitted, and unlike in the U.S., acquittals can be
overturned.

Image link: https://s.yimg.com/uu/api/res/1.2/1THMVZDeZ0z7PVXchxklYw--~B/aD00MDAwO3c9NjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/9f3f122d6d91ff94f9613b5d97409f0f
```

## Description

#### [rss_reader/rss_reader.py]

In rss_reader.py RSS reader utility is initialized and configured. The utility provides the following features:

#### *Data caching:*

The RSS news are stored in the local storage while reading. For this purpose [shelve](https://docs.python.org/3/library/shelve.html), dictionary-like object, was used.
With the optional argument ```--date %Y%m%d``` (for example: ```--date 20220624```) the cashed news can be read. Also, adding URL make the displayed news sorted by date and link. 
If the news are not found - should be returned error.

#### *Data conversion to .pdf and .html:*

The RSS reader utility provides news converter to .pdf and .html formats. It can be done with the following optional arguments: ```--to_pdf``` and
```--to_html```. Both arguments receive the path where file would be saved. The name of the file generates automatically.

There are two options for news conversion:

*convert from cache*

For this case news conversion doesn't depend on internet. With ```rss_reader.py --date 20220625 --limit 1 --to_html ~/finaltask/reader``` one news for the specified day would
be converted (the same with ```--to_pdf```), and file with it would be generated in the specified PATH.There would be clickable links to the full article 
and image.

*convert news from the Internet*

For this case Internet is required. With ```rss_reader.py https://news.yahoo.com/rss/ --limit 1 --to_html ~/finaltask/reader``` one news from listed link
would be converted (the same with ```--to_pdf```), and file with it would be generated in the specified PATH. There would be clickable links to the full
article and image.
