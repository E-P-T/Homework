## CREATION GOAL
The rss-reader has been created as a final task for graduating EPAM March 2022 Python Foundation course.
My personal goal was to create a rss-reader using OOP while trying to lessen external dependencies.
Processing of rss URLs and various ways of output are split into modular functions to allow easy changes of inner logic through inheritance. 

The rss-reader is presented in repo in two forms - a CLI utility and a web-service on Django 4 Framework and PostgreSQL base.

## NOTABLE MOMENTS

All commands listed in this README file may vary according to your system settings.
The most common difference may be in Python calling with console commands, as it can be done with keyword 'python' or 'python3' or 'py' and so on.
Script has been tested on a clean machine with python 3.9.13, so change commands accordingly to your system settings if needed.


# CLI UTILITY DOCUMENTATION

## PRODUCT VERSION
Current CLI utility rss-reader version is 1.5

## REQUIREMENTS

The current version of the product requires Python 3.9 or higher to run. The product hasn't been tested on earlier versions of Python interpreter.

Please be aware that many Operating Systems come with Python pre-installed but those Python installations may be out of date or even lack some of built-in packages.
If errors caused by such things happen please update your Python interpreter. 
- On Windows it is easily done by installation of a setup file downloaded from  http://www.python.org. 
- A quick guide for updating it on Ubuntu can be found here:
https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/

Required third-party packages with versions used while developing rss-reader (can be found in requirements_cli.txt file in 'final_task' directory):
```
setuptools~=62.3.3 *is installed by default in Python 3.4 and higher
aiohttp~=3.8.1
colorama~=0.4.4
fpdf~=1.7.2
Pillow~=9.1.1
Pygments~=2.12.0
tqdm~=4.64.0
```

## INSTALLATION

Rss-reader is cross-platform and has been tested on Windows and UNIX-based systems (Ubuntu). 

The current version of the product can be used with or without installation.
By default, the root directory of the script is called 'final_task', and the script directory is 'rss_reader'.
If you change them while using script - adjust your commands appropriately.

1. Installation as script:
```
1.1. copy or extract root directory of script (final_task) with all files and subdirectories to a local directory and open terminal

1.2. Install and activate virtual environment, to do it, use following commands while being in root directory of the script:

1.2.1. $ python -m venv venv (for UNIX-based systems) 
       or 	
       python -m venv venv (for Windows)

1.2.2. $ source venv/bin/activate  (for UNIX-based systems) 
       or
       venv\Scripts\activate (for Windows)
       
1.3. Install required packages to your fresh virtual environment, to do it use following command while being in root directory 
of the script:

1.3.1. $ pip install -r requirements_cli.txt (for UNIX-based systems) 
       or 	
       pip install -r requirements_cli.txt (for Windows)
```

2. Installation as a CLI utility:
Installation as a CLI utility requires previous steps 1.1 and 1.2 in part 1 of INSTALLATION section finished

NOTE! On MSYS2/MinGW64 Python (Windows) a problem with installation of Pillow package was encountered. To solve it, 
execute instructions in step 1.3 before continuing with step 2
```
2.1. In your command line terminal navigate to the root directory of the script

2.1.1. While in root directory install the script by executing a command:
       $ python setup.py install (for UNIX-based systems) 
       or 	
       python setup.py install (for Windows)  
```

## USING RSS-READER

Rss-reader is a Command Line Interface application, which possible options can be shown by calling the script in command line with -h (--help) argument. It can be used in three ways, differing only in a way of calling the script:

1. Using as a script - can be called in two similar ways:

1.1. While being in root directory of the script (if the name of the script directory hasn't been changed) it can be called using the following command:

     python rss_reader [-h] [--version] [--verbose] [--colorize] [--json] [--pdf [PDF]] [--html [HTML]] [--limit LIMIT] [--date DATE] *source*
	 
1.2 While being in script directory it can be called using the following command:

     python rss_reader.py [-h] [--version] [--verbose] [--colorize] [--json] [--pdf [PDF]] [--html [HTML]] [--limit LIMIT] [--date DATE] *source*	

2. Using as a CLI utility
	 
2.1. While being in root directory of the script, if it was previously installed as a CLI utility, as described above, it can be called using the following command:

     rss_reader [-h] [--version] [--verbose] [--colorize] [--json] [--pdf [PDF]] [--html [HTML]] [--limit LIMIT] [--date DATE] *source*
While calling the script in any of the before-mentioned ways, following arguments can be used:	 
```

positional arguments:
  source         RSS-feed URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info and exit
  --verbose      Outputs verbose status messages
  --colorize     Enables colored output mode
  --json         Print result as JSON in stdout
  --pdf [PDF]    Save result as PDF file, can take path to a directory as argument
  --html [HTML]  Save result as HTML file, can take path to a directory as argument
  --limit LIMIT  Limit news topics if this parameter provided
  --date DATE    Date for news selection, must be in %Y%m%d format (YYYYMMDD)

source is a mandatory argument that can only be skipped when using rss_reader with:
1) --help (-h) or --version arguments, as these two arguments stop the script after printing corresponding messages
2) --date DATE argument, and in such case will get all the available news published on the given date from cached URLs

--help (-h) argument is used to print script's help information (listed above) and exit script
--version argument is used to print script's version and exit script
--verbose argument is used for verbose logging while running the script
--colorize argument is used to enable colored output mode (colored default output, JSON output and logging messages)
--json argument is used to convert news data to JSON format and print JSON to user, its structure is described later
		
--pdf [PDF] argument is used to convert news data to PDF format and save as file
--html [HTML] argument is used to convert news data to HTML format and save as file
		- Both --pdf [PDF] and --html [HTML] arguments result in saving news in correspondent file format.
		- [PDF] and [HTML] are optional arguments which take path to a directory where user wants to save converted files.
		- NOTE that [PDF] and [HTML] save paths in Command Line commands SHOULD NOT contain surrounding quotes, usual for 
		strings in Python
		- If [PDF] / [HTML] is not provided with corresponding argument or not a valid directory (incorrect path or path 
		to a file instead of a directory) converted file will be saved in default directory 'output' in script directory.
		- If [PDF] / [HTML] is a nonexisting directory, rss-reader will try to create full path to such directory for user 
		and will use default directory 'output' in script directory if creation fails.
		- It is recomended to use absolute paths as [PDF] and [HTML] arguments, relative path are processed by script 
		according to the directory script is called from, and can lead to unexpected paths, though to help handle such 
		situations save path is printed after file successfully saved.
		- Although --pdf and --html can be used without [PDF] / [HTML] optional arguments, in such case in command they 
		both shouldn't be positioned directly before *source* argument, as any of them will in such case use *source* 
		argument as its [PDF] / [HTML] argument, which will result in rss-reader failure or incorrect result.
		
--limit LIMIT argument is used to set the quantity of news, that are shown to the user:
		- LIMIT must be a positive integer, which shows how many news are going to be shown from the feed.
		- No --limit set, LIMIT equal to 0, or LIMIT set as a negative integer all mean that user will get all available
		 news from the feed.
		- A LIMIT, which surpasses number of news in feed, will also result in user getting all available news.
		- Passing a non-integer LIMIT will raise an Exception and stop the Script run.
		- While limiting news using --limit, the script chooses most recent news according to their publishing date.
		
--date DATE argument is used to load previously cached news of the given date (with no need in Internet connection to work).
		- Providing --date argument results in news being sorted by publication time in descending order.
		- DATE argument must be a string of digits in %Y%m%d format (YYYYMMDD), e.g. 20220601 (which is 1 June 2022).
		- Combination of --date DATE and source arguments result in only news that were fetched from the source will be 
		loaded from cache.
		- If --date DATE argument is given without source, news from all sources from local cache will be loaded.
		- If there are no news in cache that match the given date, the script will raise and handle an exception.
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
python rss_reader.py --json --verbose --pdf D:/user/output/ --html output/final --limit 5 --date 20220601
python rss_reader.py --json --verbose --colorize --pdf --limit 2 --date 20220601 
```

## BASIC FUNCTIONALITY

Class RssReader is the class for fetching news from rss-feeds, caching them and processing for later output. 
Child class RssReaderCached is for loading news from cache and processing for later output if they match given conditions.

When getting news from rss-URL rss-reader collects news from given feed, downloads images from media URLs for later caching 
(to speed up process downloads are made in async mode) and forms a dictionary of the following structure called news_cache:
```
{'feed_description': 'The text of RSS-feed description tag',
 'feed_link': 'URL of RSS-feed',
 'feed_media': {'url': 'URL of feed media attachment'},
 'feed_title': 'title of RSS-feed',
 'feed_pubDate': 'publication date of RSS-feed',
 'feed_items': {'%Y:%m:%d %H:%M:%S': {'description': 'news item description',
                                      'link': 'news item link',
                                      'media': {'type': 'type (or type/format)',
                                                'url': 'URL of news item media attachment',
                                                'contains': 'a string of base64 encoded image data'},
                                      'pubDate': 'publication date of news item',
                                      'title': 'news item title'},
                '%Y:%m:%d %H:%M:%S':  {...},						
                }
}						
```
Note:
Keys are not formed in dictionary if no corresponding data is found by the script.

### Default output structure
- With source argument provided the Feed tags are formed from the feed information in news dictionary.
- If script is used with --date DATE argument and no source argument, the Feed tags are formed as a set of universal tags
and news are formed from all available cached sources
- If --json argument is provided the print is done in form of later described JSON object.
- If --json is not provided, the script by default makes a user-friendly print of news of the following structure (the number 
of news printed is affected by --limit argument if it is provided):
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

News item description

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

### Json output structure
During runtime, the script converts gathered news data into JSON when script is used with --json argument. 
The number of news in JSON object is affected by --limit argument if it is provided.
```
{
 "Feed title": "title of RSS-feed",
 "Feed description": "The text of RSS-feed description tag",
 "Feed URL": "URL of RSS-feed",
 "Last update": "publication date of RSS-feed",
        "%Y:%m:%d %H:%M:%S": {
            "Title": "news item title",
            "Link": "news item link",
            "Publication date": "publication date of news item",
            "Description": "news item description",
            "Media link": "URL of news item media attachment"
        },
        "%Y:%m:%d %H:%M:%S":  {...},
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

### Caching
Cache is saved in subdirectory 'cache' of the root directory of the script. 
Its structure is similar to the before-mentioned news_cache structure with the news_cache dictionary as a value in a pair and 'URL of RSS-feed 'as its key 
It is saved in form of JSON file, the structure of cache JSON is shown on the following example:
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
                    "url": "URL of news item media attachment",
                    "contains": "a string of base64 encoded image data"}
            }
        }
    },
 "URL of RSS-feed": {
        "feed_title": "title of RSS-feed",
        "feed_link": "URL of RSS-feed",
        "feed_description": "The text of RSS-feed description tag",
        "feed_media": {
            "url": "URL of feed media attachment",
            "contains": "a string of base64 encoded image data"
        },
        "feed_items": {
            "%Y:%m:%d %H:%M:%S": {
                "title": "news item title",
                "description": "The text of RSS-feed description tag",
                "media": {
                    "url": "URL of news item media attachment",
                    "contains": "a string of base64 encoded image data"},
                "link": "news item link",
                "pubDate": "publication date of news item"
                
            }
        }
    }
}
```

### Conversion and saving to files
If --pdf or --html argument is provided the script converts news to a file of corresponding format (the number of news converted is affected 
by --limit argument if it is provided). File will contain pictures and links, if they existed in the original article and if rss-reader managed 
to find them and process while conversion. To improve user experience progress bars are shown while conversion takes place, and removed after 
it finishes.

Default destination of output directory differs depending on the way rss-reader is used:
1. Using as a script 

When using rss-reader as script the output directory is the 'output' directory in script directory. If there is no such directory in script directory 
it will be created upon first conversion done.
2. Using as a CLI utility

When using rss-reader as CLI utility the output directory is also the 'output' directory, but its location depends on virtual environment settings. 
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
A decorator is used to make colored logging messages output if --colorize argument is passed to the script.

## CLI UTILITY TESTING

Unittests for the script are located in script directory, which is by default the 'rss_reader' directory in the root directory of the script in file test_rss_reader.py.
Unittests require test files to operate correctly, those files are located in subdirectory 'test_examples' of root script directory.
To run unittests for the script user can use following command while being in script directory:
```
$ python -m unittest test_rss_reader.py (for UNIX-based systems) 
or
python -m unittest test_rss_reader.py (for Windows)
```
Test coverage for current version is:
```
Name                 Stmts   Miss  Cover
----------------------------------------
rss_exceptions.py       12      0   100%
rss_logger.py           15      6    60%
rss_output.py          178     88    51%
rss_reader.py          437    168    62%
test_rss_reader.py     209      1    99%
----------------------------------------
TOTAL                  851    263    69%
```


# WEB SERVICE DOCUMENTATION


## REQUIREMENTS

To build and run the web-service docker-compose installation is required. Docker images are formed on base of python:3.9.13-slim-buster and postgres:14.3-alpine3.16.

Required third-party packages with versions used while developing (can be found in requirements.txt file in 'final_task' directory):
```
Django~=4.0.5
reportlab~=3.6.10
xhtml2pdf~=0.2.8
psycopg2~=2.9.3  
```

## RUNNING A WEB SERVICE

To run a web service rss-reader :
```
1.1. copy or extract root directory of script (final_task) with all files and subdirectories to a local directory and open terminal

1.2. Create docker container with rss-reader and database images by executing following command:

1.2.1. $ sudo docker-compose build (for UNIX-based systems) 
       or 	
       docker-compose build (for Windows)
       
1.3. run the container with web service by executing following command:

1.3.1. $ sudo docker-compose up (for UNIX-based systems) 
       or 	
       docker-compose up (for Windows)
```
After all components being downloaded and set up, you will see server start message
```
src_1  | Starting development server at http://0.0.0.0:8000/
src_1  | Quit the server with CONTROL-C.
```

## USING WEB SERVICE

To start using rss-reader web service open following URL in browser while server running:
```
http://127.0.0.1:8000/reader/start/
```
It will open you a start page with basic information about service and links to two main menus - reading news from URL and reading cached news.
Navigation can also be done through navigation panel in header of every page.

### Reading fresh news
To read fresh news use navigation panel button "FreshNews" or following URL:
```
http://127.0.0.1:8000/reader/fresh_news/ 
```
Enter an RSS feed URL and number of news to read to correspondent form fields and press "Read News" button. If exception is raised while 
reading news from URL, message "Couldn't get news from {URL}" will float.

### Reading cached news
News are automatically cached after reading fresh news and can be added to cache with "Add another RSS URL" form on CachedNews page.
To get to the page use navigation panel button "CachedNews" or following URL:
```
http://127.0.0.1:8000/reader/cached_news/
```
Enter an RSS feed URL, number of news to read and date of news you would like to filter to correspondent form fields and press "Read News" button.
At the bottom of the screen user can see all currently tracked RSS feed URLs. If there are currently no tracked feeds user will see "No tracked feeds yet" message.
If exception is raised while reading news from cache, message "Couldn't get news from cache" will float.

### Adding RSS URLs to cache
To add an RSS feed to tracking list use "Add another RSS URL" form on CachedNews page. Enter an RSS feed URL to the form field and press "Track Feed". 
If feed added successfully, message "URL successfully added" will float, if not - message "Couldn't add {URL} to tracking list".

### Updating cached RSS sources
To simultaneously update all tracked (cached) RSS feeds use "Update Cache" button on CachedNews page. 
For each tracked URL, if updated successfully - message "{URL} successfully added", and if update fails for some reasons - message "Couldn't update {URL}" will float.

### Saving news
While reading news user can save and download them in HTML or PDF formats by clicking correspondent buttons. Note that saving as PDF may take some 
time due to necessity of downloading and converting images from news source.

### User model - not logged in
Registration of users is available using email. On current stage of development registration is not obligatory for using service.
To register a user use navigation panel button "Register" or following URL:
```
http://127.0.0.1:8000/accounts/register/
```

After successful registration, user may log in using logging form.
To log in user can use navigation panel button "Log In" or following URL:
```
http://127.0.0.1:8000/accounts/login/
```

### User model - logged in 
After logging in, user may log out using navigation panel button "Log Out" or can open his settings menu by using navigation panel button "UserSettings'
or following URL:
```
http://127.0.0.1:8000/accounts/settings/
```
User can change and save settings in settings menu (at current level of developing the web service one checkbox setting generated for testing is available).
After saving settings message "User settings saved" will float.

User can also delete his user profile by pressing a button "Delete User". Which will also cause message "User deleted" to float.


## Both CLI utility and web service have been tested on following feeds:
```
https://www.kommersant.ru/RSS/news.xml
https://www.latimes.com/local/rss2.0.xml
https://www.usda.gov/rss/latest-releases.xml
https://www.yahoo.com/news/rss
https://cdn.feedcontrol.net/8/1114-wioSIX3uu8MEj.xml
https://moxie.foxnews.com/feedburner/latest.xml
https://feeds.simplecast.com/54nAGcIl
http://news.rambler.ru/rss/politics/
https://www.goha.ru/rss/mmorpg
https://money.onliner.by/feed
https://vse.sale/news/rss
https://news.google.com/rss/
https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml
https://www.cnbc.com/id/100727362/device/rss/rss.html
https://www.cbsnews.com/latest/rss/world
https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
https://auto.onliner.by/feed
http://feeds.bbci.co.uk/news/world/rss.xml
https://www.buzzfeed.com/world.xml
```