

# Python RSS reader

`rss-reader` is a command line utility that makes it easy to view RSS feeds in a readable format.

***Python 3.8 and above prefferable***

***Tested on Windows and MacOS***

## Installation and usage

You can install it by running the following command:

    pip install ...

Now, you can run the utility by this command:

    rss_reader {YOUR ARGUMENTS} 

*OR*

1. Clone github repository:

       git clone https://github.com/Boburshoh-oss/Final_task

2. Change directory to `Final_task`.

       cd .../Final-task

3. Install necessary dependencies:

       pip install -r requirements.txt

Now, provided, your current directory is `/Final_task`, you can run `rss_reader` as a
package:

    rss_reader

or, provided, your current directory is `/Final_task/rss_reader`, you can directly run the
module:

    python rss_reader.py

## Functionality

To see help message, please, use `-h/--help` argument: `rss_reader -h`.

    usage: rss_reader [-h] [--verbose] [--version -v] [--json] [-limit LIMIT] [--date DATE] [--to_html [FOLDER_PATH/filename (optional)]] [--to_pdf [FOLDER_PATH/filename (optional)]]
                     [source]

    Pure Python command-line RSS reader.
    
    positional arguments:
      source                   RSS URL
    
    optional arguments:
      -h, --help               Show this help message and exit.
      -v, --version            Print version info.
      --verbose                Output verbose status messages.
      --json                   Print news as JSON.
      --limit LIMIT            Limit news amount to be processed.
      --date DATE              Get news published on a specific date from cache for further processing.
      --to-html [FOLDER_PATH]  Convert news to .html format and save it by the specified folder path (FOLDER_PATH/filename can be optional).
      --to-pdf [FOLDER_PATH]   Convert news to .pdf format and save it by the specified folder path (FOLDER_PATH/filename can be optional).
     
     

*Some notes*:
-- There is a smaller form inside your html file created by --to_html so you can send me a message through it and I will be happy. I also have my telegram address in the footer section and   contact me through it


## Logging

If `--verbose` argument is  **PASSED**, messages with either `INFO` or `ERROR` severities
of `rss_reader` are printed to console,

If `--verbose` argument is passed, then all `rss_reader` logs are printed console. 



## Configuration

Application creates several files:
+ converted to supported formats directories and files: 
  Folders:
    `html_files`/,
    `pdf_files`/,
    `local_image_url`/,
  Files:
    `database_file/data.json`
Application uses `template\beautiful_news.html` file as core of html stucture and uses it for creating new html formatted files    
By default, the application files are stored inside home directory in a freshly created `Final Task` folder:

    - Windows: C:\Users\User\Final Task
        or C:\Users\Final Task
    - Linux and MacOS: /home/Final Task



## Cache JSON structure

Cache represents a dictionary of URLs with according lists of dictionaries of items, preceded by a dictionary of feed
info.

*Example:*

    [
    {
        "published": "20220625",
        "News Item": {
            "title": "Abortion Ruling Poses New Questions About How Far Supreme Court Will Go",
            "date": "2022-06-25 03:43:15",
            "link": "https://www.nytimes.com/2022/06/25/us/supreme-court-abortion-contraception-same-sex-marriage.html",
            "image_link": "https://static01.nyt.com/images/2022/06/24/us/politics/24dc-assess1/24dc-assess1-moth.jpg",
            "description": "The decision overruling Roe v. Wade exposed internal divisions among conservative justices about reconsidering other rights.",
            "creator": "Charlie Savage",
            "image_link_local": "local_image_url/dwnldimagepath3826a56d-db95-4372-ad4c-7a50d67f57e3.jpg"
        },
        "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    },
    {
        "published": "20220625",
        "News Item": {
            "title": "In 6-to-3 Ruling, Supreme Court Ends Nearly 50 Years of Abortion Rights",
            "date": "2022-06-25 03:03:05",
            "link": "https://www.nytimes.com/2022/06/24/us/roe-wade-overturned-supreme-court.html",
            "image_link": "https://static01.nyt.com/images/2022/06/24/us/politics/24dc-scotus1/24dc-scotus1-moth.jpg",
            "description": "The decision will lead to all but total bans on the procedure in about half of the states.",
            "creator": "Adam Liptak",
            "image_link_local": "local_image_url/dwnldimagepath628248fd-d493-4343-bbfc-0342e0b3f336.jpg"
        },
        "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    },
    {
        "published": "20220625",
        "News Item": {
            "title": "Kavanaugh Gave Private Assurances on Roe v. Wade. Collins Says He ‘Misled’ Her.",
            "date": "2022-06-25 02:39:41",
            "link": "https://www.nytimes.com/2022/06/24/us/roe-kavanaugh-collins-notes.html",
            "image_link": "https://static01.nyt.com/images/2022/06/24/us/politics/24dc-cong-court/merlin_142618041_4c772ae1-fdfa-4c1e-9eb1-f88fd94494ab-moth.jpg",
            "description": "“I am a don’t-rock-the-boat kind of judge,” the justice told the senator in a discussion on Roe, according to notes from a meeting before his confirmation.",
            "creator": "Carl Hulse",
            "image_link_local": "local_image_url/dwnldimagepathe16dcc7f-c0a0-410e-9abd-212383b5e926.jpg"
        },
        "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    },
    {
        "published": "20220625",
        "News Item": {
            "title": "Century-Old State Laws Could Determine Where Abortion Is Legal",
            "date": "2022-06-25 09:00:18",
            "link": "https://www.nytimes.com/2022/06/25/us/abortion-laws-wisconsin-arizona-roe-overturned.html",
            "image_link": "https://static01.nyt.com/images/2022/06/23/us/00oldlaws-01/00oldlaws-01-moth.jpg",
            "description": "In Wisconsin, Michigan and other states, abortion bans that were long considered dormant could determine if access to the procedure survives the overturning of Roe.",
            "creator": "Julie Bosman",
            "image_link_local": "local_image_url/dwnldimagepathe5edd33c-1a72-4b9c-b9df-b702e728845e.jpg"
        },
        "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    },
    {
        "published": "20220624",
        "News Item": {
            "title": "June 24, 2022: The Day Chief Justice Roberts Lost His Court",
            "date": "2022-06-24 22:54:35",
            "link": "https://www.nytimes.com/2022/06/24/us/abortion-supreme-court-roberts.html",
            "image_link": "https://static01.nyt.com/images/2022/06/24/us/politics/24dc-roberts-1/24dc-roberts-1-moth.jpg",
            "description": "Outflanked by five impatient and ambitious justices to his right, the chief justice has become powerless to pursue his incremental approach.",
            "creator": "Adam Liptak",
            "image_link_local": "local_image_url/dwnldimagepath17d8de2b-05bd-4036-a3a9-efc05a95b7c8.jpg"
        },
        "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    },
            ...
        ...

*Some notes*:

+ `--json`-printed results are different from ones, stored in cache; as the cache file is just json formatted file the user can easily explore and
  modify it (modifing is not reccomended), whereas `--json` argument is a part of the user interface, that's why its output is user-friendly.

`--json` output example:

     
                    {"published": "20180814", "News Item": {"title": "When We Eat, or Don’t Eat, May Be Critical for Health", "date": "2018-08-14 19:50:35", "link": "https://www.nytimes.com/2018/07/24/well/when-we-eat-or-dont-eat-may-be-critical-for-health.html", "image_link": "https://static01.nyt.com/images/2018/07/24/autossell/24sci_circadian/24sci_circadian-moth.jpg", "description": "A growing body of research suggests that our bodies function optimally when we align our eating patterns with our circadian rhythms.", "creator": "Anahad O’Connor"}, "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"}

                    {"published": "20220624", "News Item": {"title": "Buck Ellison’s Great White Society", "date": "2022-06-24 14:18:18", "link": "https://www.nytimes.com/2022/06/24/arts/design/buck-ellison-white-men.html", "image_link": "https://static01.nyt.com/images/2018/07/24/autossell/24sci_circadian/24sci_circadian-moth.jpg", "description": "From the driving range to the dude ranch, an artist stages intimate, alluring portraits of U.S. hegemony from within its walls.", "creator": "Travis Diehl"}, "source": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"}
                    ...
            ...

Why is there a list of feeds inside `--json` structure, not just a single feed? Inside cache file there may be items
with the same `pubDate`, but they may belong to different feeds. So, when there are such items and a user
passes `--date DATE` argument which represents this exact date, then these several items are returned and attributed to
several newly created `Feed` instances. After that, these `Feed` instances are printed. Printing returned news could be
implemented without respect to the feeds they belong to, but in this case it would be hard to distinguish them.

## Parsing XML

XML is parsed by parser implemented from scratch, it exploits the idea of XML *tokenization*, dom-tree is created from
tokens.

*Features*:

+ `XML CDATA` parsing support: whenever CDATA is encountered in XML, it gets recursively parsed and substituted by a
  normal text in the final form.
  \
  XML CDATA example link: https://rss.art19.com/apology-line
+ detecting `invalid XML`: parser notifies user with a wide range of messages whenever invalid syntax or some mistake
  was encountered in XML document.
  \
  Invalid XML example: http://feeds.bbci.co.uk/news/world/rss.xml
  \
  Its fragment (notice tags order):

      In some rss formatted urls there are not given some items like image_link, creator, description... so they are ommited and the utility prints oup the existed ones

## Tested RSS links

+ `<` char inside text is parsed correctly, as well as `commented pieces` are skipped properly:

  https://defenseofthepatience.libsyn.com/rss



+ `Empty XML document` is handled correctly:

  https://www.joindota.com/feeds/news


+ `Big channels` are parsed correctly:

  https://feeds.megaphone.fm/WWO3519750118

  https://feeds.simplecast.com/54nAGcIl


+ `CDATA` is parsed correctly:

  https://rss.art19.com/apology-line


+ `Image` is parsed correctly:

  https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml


+ Feeds in `Russian` are handled completely correctly:

  https://rss.dw.com/xml/rss-ru-rus

  https://people.onliner.by/feed

  https://brestcity.com/blog/feed

  https://rss.dw.com/xml/rss-ru-news

  https://lenta.ru/rss/top7

  https://www.liga.net/tech/battles/rss.xml

  https://vse.sale/news/rss


+ Some others:

  https://news.yahoo.com/rss/

  https://www.liquiddota.com/rss/news.xml


+ Please, see `Known problems` section below:

  https://www.theguardian.com/international/rss

  https://www.hyprgame.com/blog/category/dota2/feed/

## Testing

Modules tested:

+ to_html.py
+ to_pdf.py
+ rss_reader.py
    (
      Name                              Stmts   Miss  Cover   
      database_file\check_database.py      20      9    55%   
      html_tag_parse.py                    18      0   100%
      json_convert_to_pdf.py               59     13    78%   
      json_to_html.py                     100     26    74%   
      rss_reader.py                       279    115    59%   
      test.py                              57      1    98%   
      utilty.py                             9      1    89%   
      -------------------------------------------------------
      TOTAL                               542    165    70%

    )
  In order to see the testing results in table use these commands below:
    -coverage run -m unittest discover
    -coverage report -m
***Test coverage is 70%.***

In order to run tests, please, install dependencies:
    
    python.exe -m unittest test.py


install wkhtmltopdf for Windows(http://wkhtmltopdf.org/downloads.html)
pip install pdfkit
Documentation about pdfKit can be found here: https://pypi.python.org/pypi/pdfkit

linux 
sudo apt-get install wkhtmltopdf
sudo apt install wkhtmltopdf