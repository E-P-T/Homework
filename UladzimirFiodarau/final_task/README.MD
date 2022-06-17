## CREATION GOAL
The rss-reader has been created as a final task for graduating EPAM March 2022 Python Foundation course.
My personal goal was to create a rss-reader using OOP and with minimum third-party libraries to lessen external dependencies.
Processing of rss URLs and various ways of output are split into corpuscular functions to allow easy changes of inner logic through inheritance. 

## PRODUCT VERSION
Current rss-reader version is 1.4

## REQUIREMENTS

The current version of the product requires only Python 3.9 or higher to run. The product hasn't been tested on earlier versions of Python interpreter.

Please be aware that many Operating Systems come with Python pre-installed but those Python installations may be out of date or even lack some of builtin packages.
If errors caused by such things happen please update your Python interpreter. A quick guide for updating in on Ubuntu, for example, can be found here:
https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/

## NOTABLE MOMENTS
All commands listed in this README file may vary according to your system settings.
The most common difference may be in Python calling with console commands, as it can be done with keyword 'python' or 'py' or 'py3' and so on.
Script has been tested on a clean machine with python 3.9.13, so change commands accordingly to your system settings if needed.

## INSTALLATION
Rss-reader is crossplatform and has been tested on Windows an UNIX-based systems (Ubuntu). 

The current version of the product can be used with or without installation.
By default, the root directory of the script is called 'final_task', and the script directory is 'rss_reader'.
If you change them while using script - adjust your commands appropriately.

1. Installation as script:
```
1.1. copy or extract root directory of script (final_task) with all files and subdirectories to a local directory

1.2. Install and activate virtual environment, to do it use following command while being in root directory of the script:

1.2.1. $ python -m venv venv (for UNIX-based systems) 
       or 	
       python -m venv venv (for Windows)

1.2.2. $ source venv/bin/activate  (for UNIX-based systems) 
       or
       venv\Scripts\activate.bat or venv\Scripts\activate.ps1 (for Windows)
       
1.3. Install required packages to your fresh virtual environment, to do it use following command while being in root directory of the script:

1.3.1. $ pip install -r requirements.txt (for UNIX-based systems) 
       or 	
       pip install -r requirements.txt (for Windows)
```

2. Installation as a CLI utility:
Installation as a CLI utility requires previous steps in part 1 of INSTALLATION section finished
```
2.1. In your command line terminal navigate to the root directory of the script

1.2. While in root directory install the script by executing a command:
       $ python setup.py install (for UNIX-based systems) 
       or 	
       python setup.py install (for Windows)  
```

## USING RSS-READER

Rss-reader is a Command Line Interface application. Still it can be used in three different ways, differing only in a way to call the script:
1. Using as a script 
Rss-reader as a script can be called in two similar ways by putting a command in command line interface, that can be shown by calling the script in command line with --help argument.

1.1. While being in root directory of the script (if the name of the script directory hasn't been changed) it can be called using the following command:

     python rss_reader [-h] [--version] [--verbose] [--json] [--pdf] [--html] [--limit LIMIT] [--date DATE] *source*
	 
1.2 While being in script directory it can be called using the following command:

     python rss_reader.py [-h] [--version] [--verbose] [--json] [--pdf] [--html] [--limit LIMIT] [--date DATE] *source*	

2. Using as a CLI utility
	 
2.1. While being in root directory of the script, if it was previously installed as a CLI utility, as described above, it can be called using the following command:

     rss_reader [-h] [--version] [--verbose] [--json] [--pdf] [--html] [--limit LIMIT] [--date DATE] *source*
While calling the script in any of the before-mentioned ways, following arguments can be used:	 
```

positional arguments:
  source         RSS-feed URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info and exit
  --verbose      Outputs verbose status messages
  --json         Print result as JSON in stdout
  --pdf          Save result as PDF file
  --html         Save result as HTML file
  --limit LIMIT  Limit news topics if this parameter provided
  --date DATE    Date for news selection, must be in %Y%m%d format (YYYYMMDD)

source is a mandatory argument but can only be skipped when using rss_reader with:
1) --help (-h) or --version arguments, as these two arguments stop the script after printing corresponding messages
2) --date DATE argument, and in such case will get all the available news published on the given date from all cached URLs

--help (-h)  argument is used to print script's help information (listed above) and exit script
--version  argument is used to print script's version and exit script
--verbose argument is used for verbose logging while running the script
--json argument is used to convert news data to JSON format and print JSON to user. The structure of JSON is described later in this file
--pdf argument is used to convert news data to PDF format and save as file
--html argument is used to convert news data to HTML format and save as file
		Both --pdf and --html arguments result in saving news file in chosen format in directory 'output' in script directory
--limit LIMIT argument is used to set the quantity of news, that are shown to the user:
		LIMIT must be a positive integer, which shows how many news are going to be shown from the feed.
		No --limit set or LIMIT equal to 0, or LIMIT set as a negative integer, all mean that user will get all available news from the feed.
		A LIMIT, which surpasses number of news in feed, will also result in user getting all available news from the feed.
		Passing a non-integer LIMIT will raise an Exception and stop the Script run.
		While limiting news using --limit, the script chooses most recent news according to their publishing date in the feed.
--date DATE argument is used to load previously cached news. If it is given, the rss-reader doesn't require Internet connection to work.
		DATE argument must be a string of digits in %Y%m%d format (YYYYMMDD), e.g. 20220601 (which is 1 June 2022)
		Combination of --date DATE and source arguments result in only news that were fetched from the source will be loaded from cache.
		If --date DATE argument is given without source, news from all sources for the date from local cache will be loaded.
		If there are no news in cache that match the given date, the script will raise and handle an exception.
```

Arguments can be used in combinations, e.g.:
```
python rss_reader.py --version
python rss_reader.py --version --verbose --limit 1000 https://www.buzzfeed.com/world.xml (only --version is run)
python rss_reader.py --help --verbose --limit 1000 https://www.buzzfeed.com/world.xml (only --help is run)
python rss_reader.py --verbose --limit 3 https://www.buzzfeed.com/world.xml 
python rss_reader.py --verbose --limit 1000 https://www.buzzfeed.com/world.xml
python rss_reader.py --json --limit 0 https://www.buzzfeed.com/world.xml
python rss_reader.py --json --verbose --limit 5 --date 20220601 https://www.buzzfeed.com/world.xml
python rss_reader.py --json --verbose --limit 5 --date 20220601
python rss_reader.py --json --verbose --pdf --html --limit 5 --date 20220601
```

## BASIC FUNCTIONALITY

Class RssReader is the class for fetching news from rss-feeds, caching them and processing for later output. 
Child class RssReaderCached is for loading news from cache and processing for later output if they match given conditions.

The rss-reader collects news from a given feed and forms a dictionary of the following structure called news_cache:
```
{'feed_description': 'The text of RSS-feed description tag',
 'feed_link': 'URL of RSS-feed',
 'feed_media': {'url': 'URL of feed media attachment'},
 'feed_title': 'title of RSS-feed',
 'feed_pubDate': 'publication date of RSS-feed',
 'feed_items': {'%Y:%m:%d %H:%M:%S': {'description': 'news item description',
                                      'link': 'news item link',
                                      'media': {'type': 'type (or type/format)',
                                                'url': 'URL of news item media attachment'},
                                      'pubDate': 'publication date of news item',
                                      'title': 'news item title'},
                '%Y:%m:%d %H:%M:%S':  {...},						
                }
}						
```
Note:
Keys are not formed in dictionary if no corresponding data is found by the script.


### JSON STRUCTURE
During runtime, the script converts gathered news data into JSON when script is used with --json argument. 
The structure of JSON is the same as that of news_cache dictionary, but the number of news in JSON object is affected by --limit argument if it is provided.
```
{"feed_description": "The text of RSS-feed description tag",
 "feed_link": "URL of RSS-feed",
 "feed_media": {"url": "URL of feed media attachment"},
 "feed_title": "title of RSS-feed",
 "feed_pubDate": "publication date of RSS-feed",
 "feed_items": {"%Y:%m:%d %H:%M:%S": {"description": "news item description",
                                      "link": "news item link",
                                      "media": {"type": "type (or type/format)",
                                                "url": "URL of news item media attachment"},
                                      "pubDate": "publication date of news item",
                                      "title": "news item title"},
                "%Y:%m:%d %H:%M:%S":  {...},						
                }
}	
```
JSON output has been tested for being a valid JSON using online service JSON Online Validator and Formatter - JSON Lint (https://jsonlint.com)
on english and russian feeds, e.g.:
```
https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
https://feeds.simplecast.com
https://vse.sale/news/rss
https://money.onliner.by
```

### CACHING

Cache is saved in subdirectory 'cache/' of the root directory of the script. 
Its structure is similar to the before-mentioned news_cache structure with the news_cache dictionary as a value in a pair and 'URL of RSS-feed 'as its key 
It is saved in form of JSON file, the structure of cache and JSON is shown on the following example:
```
{
 "URL of RSS-feed": {
        "feed_title": "title of RSS-feed",
        "feed_link": "URL of RSS-feed",
        "feed_description": "The text of RSS-feed description tag",
        "feed_pubDate": "publication date of RSS-feed",
        "feed_items": {
            "%Y:%m:%d %H:%M:%S": {
                "title": "news item title",
                "link": "news item link",
                "description": "news item description",
                "pubDate": "publication date of news item",
                "media": {
                    "url": "URL of news item media attachment"
                }
            }
        }
    },
 "URL of RSS-feed": {
        "feed_title": "title of RSS-feed",
        "feed_link": "URL of RSS-feed",
        "feed_description": "The text of RSS-feed description tag",
        "feed_media": {
            "url": "URL of feed media attachment"
        },
        "feed_items": {
            "%Y:%m:%d %H:%M:%S": {
                "title": "news item title",
                "description": "The text of RSS-feed description tag",
                "media": {
                    "url": "URL of news item media attachment"
                },
                "link": "news item link",
                "pubDate": "publication date of news item"
                
            }
        }
    }
}
```

### DEFAULT OUTPUT STRUCTURE			
- With source argument provided the Feed tags are formed from the feed information in news dictionary.
- If script is used with --date DATE argument and no source argument the Feed tags are formed as a set of universal tags.
- If --json argument is provided the print is done in a dictionary form, similar to before-mentioned JSON structure.
- If --json is not provided, the script by default makes a user-friendly print of news of the following structure:
```
========================================================================================================================
Feed title: title of RSS-feed
Feed description: The text of RSS-feed description tag
Feed URL: URL of RSS-feed
Last update: latest feed publication date
========================================================================================================================
Title: news item title
Link: news item link
Publication date: publication date of news item

news item description

Media (type/format) link:
URL of news item media attachment
------------------------------------------------------------------------------------------------------------------------
Title: news item title
Link: news item link
...
...
------------------------------------------------------------------------------------------------------------------------
```
Note:
there are filler messages prepared for printing data, which was not found in rss-feed, and thereby is not presented in the news dictionary.



### CONVERSION TO FILE
If --pdf or --html argument is provided the script converts news to a file of corresponding format. File contains pictures and links, if they existed in the original article and if rss-reader managed to find them and process while conversion.

Default destination of output directory differs depending on the way rss-reader is used:
1. Using as a script 
When using rss-reader as script the output directory is the 'output' directory in script directory. If there is no such directory in script directory it will be created upon first conversion done.
2. Using as a CLI utility
When using rss-reader as CLI utility the output directory is also the 'output' directory, but it's location depends on virtual environment settings. 

For example if virtual environment is set to a directory:
```
 'some_path/venv/'
```
 output directory will be located in directory 
```
'some_path/venv/lib/site-packages/rss_reader-?-py?.egg/rss_reader/output/'
```
For easier finding, rss-reader will print path to converted files after conversion.

## Logging
By default, logging is not enabled. Providing --verbose argument on script call results in logging enabling.
Default logging settings are listed in root directory of the script in file rss_logger.py and contain the following:
```
logger_info = logging
log_format = "%(levelname)s %(asctime)s - %(message)s"
logger_info.basicConfig(level=logging.INFO,
                        stream=sys.stdout,
                        format=log_format,
                        datefmt='%Y:%m:%d %H:%M:%S',
                        )
```

## TESTING
Unittests for the script are located in script directory, which is by default the 'rss_reader' directory in the root directory of the script in file test_rss_reader.py.
Unittests require test files to operate correctly, those files are located in subdirectory 'test_examples' of root script directory.
To run unittests for the script user can use following command while being in root directory of the script:
```
$ python -m unittest test_rss_reader.py (for UNIX-based systems) 
or
python -m unittest test_rss_reader.py (for Windows)
```

### Script has been tested on following feeds:
```
https://www.latimes.com/local/rss2.0.xml
https://www.usda.gov/rss/latest-releases.xml
https://www.yahoo.com/news/rss
https://cdn.feedcontrol.net/8/1114-wioSIX3uu8MEj.xml
https://moxie.foxnews.com/feedburner/latest.xml
https://feeds.simplecast.com/54nAGcIl
http://news.rambler.ru/rss/politics/
https://www.goha.ru/rss/mmorpg
https://money.onliner.by/feed
http://www.gazeta.ru/export/gazeta_rss.xml
https://vse.sale/news/rss
https://news.google.com/rss/
https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml
https://www.cnbc.com/id/100727362/device/rss/rss.html
https://www.cbsnews.com/latest/rss/world
https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
https://auto.onliner.by/feed
http://feeds.bbci.co.uk/news/world/rss.xml
https://www.buzzfeed.com/world.xml
https://www.kommersant.ru/RSS/news.xml
```