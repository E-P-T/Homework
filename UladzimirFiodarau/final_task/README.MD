## CREATION GOAL
The rss-reader has been created as a final task for graduating EPAM March 2022 Python Foundation course.
My personal goal was to create a rss-reader using OOP and without third-party libraries to lessen external dependencies.
Processing of rss URLs and various ways of output are split into corpuscular functions to allow easy changes of inner logic through inheritance. 

## PRODUCT VERSION
Current rss-reader version is 1.2

## REQUIREMENTS

The current version of the product requires only Python 3.9 or higher to run. The product hasn't been tested on earlier versions of Python interpreter

## NOTABLE MOMENTS
All commands listed in this README file may vary according to your system settings.
The most common difference may be in Python calling with console commands, as it can be done with keyword 'python' or 'py' or 'py3' and so on.
Script has been tested on a clean machine with python 3.9.13, so change commands accordingly to your system settings if needed.

## INSTALLATION

The current version of the product can be used with or without installation.
By default, the root directory of the script is called final_task, if you change it while using script - adjust your commands appropriately.

1. Installation as script:
```
1.1. copy or extract root directory of script (final_task) with all files and subdirectories to a local directory

1.2. Install and activate virtual environment, to do it use following command while being in root directory of the script:

1.2.1. $ python -m venv venv (for UNIX-based systems) 
       or 	
       python -m venv venv (for Windows)

1.2.2. $ source venv/bin/activate  (for UNIX-based systems) 
       or
       venv\Script\activate.bat or venv\bin\activate.ps1 (for Windows)
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

1.1. While being in root directory of the script, if the name of the script directory, which is by default the 'rss_reader' directory hasn't been changed, it can be called using the following command:

     python rss_reader [-h] [--version] [--json] [--verbose] [--limit LIMIT] *source*
	 
1.2 While being in script directory, which is by default the 'rss_reader' directory in the root directory of the script, it can be called using the following command:

     python rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] *source*	
	 
1.3. While being in root directory of the script, if it was previously installed as a CLI utility, as described above, it can be called using the following command:

     rss_reader [-h] [--version] [--json] [--verbose] [--limit LIMIT] *source*
While calling the script in any of the before-mentioned ways, following positional arguments can be used:	 
```

  source        RSS-feed URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided}

source is a mandatory argument and can only be skipped when using rss_reader.py with --help (-h) or --version arguments, as these two arguments stop the script after printing corresponding messages
--help (-h)  argument is used to print script's help information (listed above) and exit script
--version  argument is used to print script's version and exit script
--json argument is used to convert news data to JSON format. The structure of JSON is described later in this file
--verbose argument is used for verbose logging while running the script
--limit LIMIT argument is used to set the quantity of news, that are shown to the user:
		LIMIT must be a positive integer, which shows how mane news are going to be shown from the feed.)
		If LIMIT is a negative integer, no news will be displayed (feed information will still be printed to the user)
		No --limit set or LIMIT equal to 0 both mean that user will get all available news from the feed.
		A LIMIT, which surpasses number of news in feed, will also result in user getting all available news from the feed.
		While limiting news using --limit, the script chooses most recent news according to their publishing date in the feed.

Arguments can be used in combinations, e.g.:

python rss_reader.py --version
python rss_reader.py --version --verbose --limit 1000 https://www.buzzfeed.com/world.xml (only --version is run)
python rss_reader.py --verbose --limit 3 https://www.buzzfeed.com/world.xml 
python rss_reader.py --verbose --limit 1000 https://www.buzzfeed.com/world.xml
python rss_reader.py --json --limit 0 https://www.buzzfeed.com/world.xml
python rss_reader.py --json --verbose --limit 5 https://www.buzzfeed.com/world.xml
```

## BASIC FUNCTIONALITY

The rss-reader collects news from a given feed and forms a cache dictionary of the following structure:
```
{'feed_description': 'The text of RSS-feed description tag',
 'feed_link': 'URL of RSS-feed',
 'feed_media': {'url': 'URL of feed media attachment'},
 'feed_title': 'title of RSS-feed',
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
'feed_media' and 'media' keys are not mandatory and are not formed in dictionary in no media data found by the script. Others keys are however mandatory and if not presented in feed are paired with corespondent text notifications in feed_ section and None value in items section.

### JSON STRUCTURE
During runtime, the script converts gathered news data into JSON when script is used with --json argument. 
The structure of JSON is the same as that of cache dictionary, but the number of news in JSON object is affected by --limit argument if it is provided.
```
{"feed_description": "The text of RSS-feed description tag",
 "feed_link": "URL of RSS-feed",
 "feed_media": {"url": "URL of feed media attachment"},
 "feed_title": "title of RSS-feed",
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
### DEFAULT OUTPUT STRUCTURE										
If --json is not provided, the script by default makes a user-friendly print of news of the following structure:
```
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