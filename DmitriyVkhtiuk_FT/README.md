## CREATION GOAL
The rss-reader has been created as a final task for graduating EPAM March 2022 Python Foundation course.
My personal goal was to create a rss-reader using OOP and try to think of every issue that can only happen when the script is running.

## PRODUCT VERSION
Current rss-reader version is 1.5

## NOTABLE MOMENTS
All commands listed in this README file may vary according to your system settings.
The most common difference may be in Python calling with console commands, as it can be done with keyword 'python' or 'python3' or 'py' and so on.
Script has been tested on a clean machine with python 3.9.13, so change commands accordingly to your system settings if needed.

## REQUIREMENTS

The current version of the product requires Python 3.9 or higher to run. The product hasn't been tested on earlier versions of Python interpreter.

Please be aware that many Operating Systems come with Python pre-installed but those Python installations may be out of date or even lack some of built-in packages.
If errors caused by such things happen please update your Python interpreter. 
- On Windows it is easily done by installation of a setup file downloaded from  http://www.python.org. 
- A quick guide for updating it on Ubuntu can be found here:
https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/

Required third-party packages with versions used while developing rss-reader (can be found in requirements.txt file in 'final_task' directory):
```
setuptools~=62.3.3 *is installed by default in Python 3.4 and higher
arabic-reshaper==2.1.3
asn1crypto==1.5.1
beautifulsoup4==4.11.1
certifi==2022.6.15
cffi==1.15.0
charset-normalizer==2.0.12
click==8.1.3
colorama==0.4.5
coverage==6.4.1
cryptography==37.0.2
cssselect2==0.6.0
future==0.18.2
html5lib==1.1
idna==3.3
Pygments==2.12.0
lxml==4.9.0
numpy==1.23.0
oscrypto==1.3.0
pandas==1.4.3
Pillow==9.1.1
pycparser==2.21
pyHanko==0.13.1
pyhanko-certvalidator==0.19.5
PyPDF3==1.0.6
python-bidi==0.4.2
python-dateutil==2.8.2
pytz==2022.1
pytz-deprecation-shim==0.1.0.post0
PyYAML==6.0
qrcode==7.3.1
reportlab==3.6.10
requests==2.28.0
six==1.16.0
soupsieve==2.3.2.post1
svglib==1.3.0
tinycss2==1.1.1
tqdm==4.64.0
tzdata==2022.1
tzlocal==4.2
uritools==4.0.0
urllib3==1.26.9
webencodings==0.5.1
xhtml2pdf==0.2.8
```

## INSTALLATION
Rss-reader is cross-platform and has been tested on Windows and UNIX-based systems (Ubuntu). 

The current version of the product can be used with or without installation.
By default, the root directory of the script is called 'final_task', and the script directory is 'rss_reader'.
If you change them while using script - adjust your commands appropriately.

1. Installation as script:
```
1.1. copy or extract root directory of script (final_task) with all files and subdirectories to a local directory

1.2. Install and activate virtual environment, to do it, use following commands while being in root directory of the script:

1.2.1. $ python -m venv venv (for UNIX-based systems) 
       or 	
       python -m venv venv (for Windows)

1.2.2. $ source venv/bin/activate  (for UNIX-based systems) 
       or
       venv\Scripts\activate.bat or venv\Scripts\activate.ps1 or venv\Scripts\activate (for Windows)
       
1.3. Install required packages to your fresh virtual environment, to do it use following command while being in root directory 
of the script:

1.3.1. $ pip install -r requirements.txt (for UNIX-based systems) 
       or 	
       pip install -r requirements.txt (for Windows)
```

2. Installation as a CLI utility:
Installation as a CLI utility requires previous steps 1.1 and 1.2 in part 1 of INSTALLATION section finished
```
2.1. In your command line terminal navigate to the root directory of the script

2.2. While in root directory install the script by executing a command:
       $ python setup.py install (for UNIX-based systems) 
       or 	
       python setup.py install (for Windows)  
```

## USING RSS-READER

Rss-reader is a Command Line Interface application, which possible options can be shown by calling the script in command line with -h (--help) argument. It can be used in two ways, differing only in a way of calling the script:

1. Using as a script - can be called in this way:

	 
1.1 While being in script directory it can be called using the following command:

     python rss_reader.py  [-h] [--limit LIMIT] [--json] [--verbose] [--version] [--date DATE] [--html HTML_PATH] [--pdf PDF_PATH] [--colorized] [source]

2. Using as a CLI utility
	 
2.1. While being in root directory of the script, if it was previously installed as a CLI utility, as described above, it can be called using the following command:

     rss_reader [-h] [--limit LIMIT] [--json] [--verbose] [--version] [--date DATE] [--html HTML_PATH] [--pdf PDF_PATH] [--colorized] [source]

While calling the script in any of the before-mentioned ways, following arguments can be used:	 
```

positional arguments:
  source            RSS URL

options:
  -h, --help        show this help message and exit
  --limit LIMIT     Limit news topics if this parameter provided. (MUST expect one argument)
  --json            print result as JSON in stdout.
  --verbose         Outputs verbose status messages
  --version         Print version info
  --date DATE       Fetch news from local cache by date
  --html HTML_PATH  Convert news to .html
  --pdf PDF_PATH    Convert news to .pdf
  --colorized       Outputs in colorize mode


source is the positional argument but can be skipped, because it takes nargs="?" and default value for source is None.
in this case, if --date is not specified, script will print the message(error), that user should check the RSS URL, 
which is given and try again because request has a bad status code.


--help (-h) argument is used to print script's help information (listed above) and exit script
--version argument is used to print script's version and exit script
--verbose argument is used for verbose logging while running the script
--json argument is used to convert news data to JSON format and print JSON to user, its structure is described later
--colorized argument is used to enable colored output mode
--pdf PDF_PATH  argument is used to convert news data to PDF format and save as file
--html HTML_PATH argument is used to convert news data to HTML format and save as file
		- Both [pdf PDF_PATH] and [html HTML_PATH] arguments result in saving news in correspondent file format.
		- [pdf PDF_PATH] and [html HTML_PATH] are optional arguments which take paths to a directory or directory/file where user wants to save converted files.
		- If [pdf PDF_PATH] / [html HTML_PATH] is not provided with corresponding argument or not a valid directory or permission denied to change the given      directory, converted file will be saved in default "default_dir" directory in current directory.
		- If [pdf PDF_PATH] / [html HTML_PATH] is a nonexisting directory, rss-reader will try to create full path to such directory for user 
		and will use default directory "default_dir" in script directory if creation fails.
		- It is recomended to use absolute paths as [pdf PDF_PATH] and [html HTML_PATH] arguments, relative path are processed by script 
		according to the directory script is called from, and can lead to unexpected paths, though to help handle such 
		situations save path is printed after file successfully saved.
		
		
--limit LIMIT argument is used to set the quantity of news, that are shown to the user:
		- LIMIT must be a positive integer, which shows how many news are going to be shown from the feed.
		- No --limit set, user will get all available news from the feed.
              - If --limit <=0, "limit must be a positive number" will be printed and exit.
		- A LIMIT, which surpasses number of news in feed, will also result in user getting all available news.
		- Passing a non-integer LIMIT will print user-oriented message of error and stop the Script run.
		- While limiting news using --limit, the script chooses most recent news according to their publishing date.
		
--date DATE argument is used to load previously cached news of the given date (with no need in Internet connection to work).
		- Providing --date argument, results in news being sorted by publication time in descending order.
		- DATE argument must be a string of digits in %Y%m%d format (YYYYMMDD), e.g. 20210613 (which is 13 June 2021).
		- Combination of --date DATE and source arguments result in only news that were fetched from the source will be 
		loaded from cache.
		- If --date DATE argument is given without source, news from all sources from local cache will be loaded.
		- If there are no news in cache that match the given date, script will print error message and stop the script run.
```

Arguments can be used in combinations, e.g.:
```
python rss_reader.py
python rss_reader.py --version
python rss_reader.py --version --verbose --limit 1000 https://news.yahoo.com/rss/ 
python rss_reader.py --help --verbose --limit 1000 https://news.yahoo.com/rss/
python rss_reader.py --verbose --limit 3 https://news.yahoo.com/rss/
python rss_reader.py --verbose --limit 1000 https://news.yahoo.com/rss/
python rss_reader.py --json --verbose --limit 5 --date 20220617 https://news.yahoo.com/rss/
python rss_reader.py --json --verbose --limit 5 --date 20220621
python rss_reader.py --json --verbose --pdf --html --limit 5 --date 20220613
python rss_reader.py --json --verbose --pdf c:/users/dviht/converted --html output/final --limit 5 --date 20220610
python rss_reader.py --json --verbose --pdf c:/users/dviht/converted --html output/final --limit 5 https://news.yahoo.com/rss/

```

## BASIC FUNCTIONALITY

Class NewsBrain is the base class of rss-reader, gathers required information from rss-feeds and prints a dictionary with valuable data.
Caches gathered news for later use, using pandas lib.
Provides methods for printing data in stdout with option of converting to JSON format.
Provides converters functionality, enable logger, if --verbose argument is specified.
Reformat news dates in cache to provide easy search for news, which date was specified in --date argument.


### JSON OUTPUT STRUCTURE
During runtime, the script converts gathered news data into JSON when script is used with --json argument. 
The number of news in JSON object is affected by --limit argument if it is provided.
```
 {
   "index_of_new" : {
       "Source": "RSS URL of Feed",
       "Feed": "Title of Feed",
       "Title":"Title of article",
       "Date": "pubDate of article",
       "Link": "Link to the article"
       "Description": "description of article",
       "Image": : "article image"

    }
}
```
### CACHING
Cache location differing in a way of calling the script:

1. Using as a script:

1.1.
       cache.csv file with cache appears in the script directory.

2. Using as a CLI utility:

2.1.
       Cache is saved in some_path/venv/lib/site-packages/rss_reader-?-py?.egg/rss_reader/cache.csv.

News is stored in the csv file and processed using pandas lib.
If --date argument is specified and is valid, dates of all cached news will be reformatted in %Y%m%d format to make search for news with specified pubDate really easy.
If some dates in cache can not be reformatted, they will be ignored and not reformatted and message "can't reformat the date {problem date}" will be printed. 
```
Source,Feed,Title,Date,Link,Description,Image
https://news.yahoo.com/rss/,Yahoo News - Latest News & Headlines,Officials: Georgia man sentenced to die kills self in prison,2022-06-27T12:50:43Z,https://news.yahoo.com/officials-georgia-man-sentenced-die-125043110.html,"JACKSON, Ga. (AP) — A Georgia man who was recently sentenced to death in the killings of two corrections officers during an escape attempt five years ago has died in prison of an apparent suicide, corrections officials said.Prison guards found Ricky Dubose unresponsive in his cell at the Georgia Diagnostic and Classification Prison in Jackson around 4:45 p.m. Sunday, according to a Department of Corrections news release. The guards called for medical help and began rendering aid. The coroner at the prison declared Dubose dead at 5:56 p.m.",https://s.yimg.com/uu/api/res/1.2/zEeBoPLQVzw1u2VjZt.THA--~B/aD03NDk7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap.org/5cf8e923a8d9dec8758480785184f376
https://news.yahoo.com/rss/,Yahoo News - Latest News & Headlines,Chinese father breaks down after son he tutored daily for a year scores a 6/100 on math exam,2022-06-28T23:18:34Z,https://news.yahoo.com/chinese-father-breaks-down-son-231834062.html,"A Chinese father who reportedly tutored his son daily for a year went viral for bursting into tears after his son scored six out of 100 points on a math exam.The child’s parents from Zhengzhou, Henan Province, received his test score on June 23. Upon learning that their son had only received six points for his final math test, the father burst into tears, as seen in a video posted to Weibo by Qilu Evening News. ",https://s.yimg.com/uu/api/res/1.2/JUWswwp8z.axCjm0RqxLoQ--~B/aD00MjU7dz04MDA7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/nextshark_articles_509/1b639cbcb8324799b67404180a9fddcd
```

### DEFAULT OUTPUT STRUCTURE			
- With source argument provided the Feed tags are formed from the feed information in news dictionary.
- If script is used with --date DATE argument and no source argument, news dictionary is formed from pandas.DataFrame with reformatted dates in %Y%m%d format.
- If --json argument is provided the print is done in form of before-mentioned JSON object.
- If --json is not provided, the script by default makes a print of news of the following structure (the number 
of news printed is affected by --limit argument if it is provided):
```

    Source: "RSS URL of Feed",
    Feed: "Title of Feed",
    Title:"Title of article",
    Date: "pubDate of article",
    Link: "Link to the article"
    Description: "Description of article",
    Image: : "article image"

```



### CONVERSION TO FILE
If --pdf or --html argument is provided the script converts news to a file of corresponding format (the number of news converted is affected 
by --limit argument if it is provided). File will contain pictures and links, if they existed in the original article and if rss-reader managed 
to find them and process while conversion. 

Default destination of output directory, when using rss-reader as script or as CLI utility , is the 'default_dir' directory in current local directory. If there is no such directory in script directory or in root directory of the script, it will be created upon first conversion with invalid path done.
For easier finding, rss-reader will print path to converted files after conversion.

## Logging
By default, logging is not disabled, but printing logs to console depends on the --verbose argument. If specified, logs will be displayed in the console.
Default logging settings are listed in script directory in module news_brain.py and contain the following:
```        
        log_format = "%(asctime)s - %(message)s \n"
        log.basicConfig(level=log.DEBUG, format=log_format)
        logger = log.getLogger()
        return logger
    
```

## TESTING
Unittests for the script are located in script directory, which is by default the 'rss_reader' directory in the root directory of the script in file tests.py.
Unittests require test files to operate correctly, those files are located in subdirectory 'test_files' in the script directory.
To run unittests for the script user can use following command while being in script directory:
```
$ python -m unittest tests.py (for UNIX-based systems) 
or
python -m unittest tests.py (for Windows)
```
Test coverage for current version is:
```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
font\__init__.py             0      0   100%
modified_argparser.py       28      8    71%   12-13, 31-32, 34-35, 42, 45
news_brain.py              285     93    67%   64-65, 73-76, 87-88, 107, 149-150, 153-154, 157-158, 161-162, 169-178, 185-186, 195-196, 210-218, 225-226, 238-241, 296-297, 329, 341, 352-363, 366-398, 437-438, 441-447, 452, 458, 463-464
template.py                  1      0   100%
test_files\__init__.py       0      0   100%
tests.py                   110      1    99%   246
------------------------------------------------------
TOTAL                      424    102    76%

```

### Script has been tested on following feeds:
```

https://www.latimes.com/local/rss2.0.xml
https://www.usda.gov/rss/latest-releases.xml
https://www.yahoo.com/news/rss
https://cdn.feedcontrol.net/8/1114-wioSIX3uu8MEj.xml
https://moxie.foxnews.com/feedburner/latest.xml
https://feeds.simplecast.com/54nAGcIl
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