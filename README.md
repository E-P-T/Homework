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

       git clone https://github.com/karimoff96/Final-task

2. Change directory to `karimoff96/Final-task`.

       cd .../Final-task

3. Install necessary dependencies:

       pip install -r requirements.txt

Now, provided, your current directory is `/Final_task`, you can run `rss_reader` as a
package:

    rss_reader {your arguments}

or, provided, your current directory is `/Final_task/rss_reader`, you can directly run the
module:
    python rss_reader.py {your arguments}


!!! Before using short command (rss_reader {your arguments}) generate distribution packages for the package. These are archives that are uploaded to the Python Package Index and can be installed by pip.
Make sure you have the latest version of PyPA’s build installed:

  >>>pip install --upgrade build

Now run this command from the same directory where pyproject.toml is located: 

  >>>python -m build    

This command should output a lot of text and once completed should generate two files in the dist directory:
    dist/
      RSS_reader-4.2-py3-none-any.whl
      RSS_reader-4.2.tar.gz
      
The tar.gz file is a source distribution whereas the .whl file is a built distribution. Newer pip versions preferentially install built distributions, but will fall back to source distributions if needed. You should always upload a source distribution and provide built distributions for the platforms your project is compatible with. In this case, our example package is compatible with Python on any platform so only one built distribution is needed.

  >>>pip install --editable .

This command will install the package in develop mode, meaning it will just link back to where the sources are. If by any chance the sources are moved or deleted, importing the package will fail.

## Functionality

To see help message, please, use `-h/--help` argument: `rss_reader -h`.

    usage: rss_reader [-h] [--verbose] [--json] [-limit LIMIT] [-date DATE] [--to-html] [--to-pdf]  [source]

    Pure Python command-line RSS reader.
    
    positional arguments:
      source                   RSS URL
    
    optional arguments:
      -h, --help               Show this help message and exit.
      --version                Print version info.
      --verbose                Output verbose status messages.
      --json                   Print news as JSON.
      --limit LIMIT            Limit news amount to be processed.
      --date DATE              Get news published on a specific date from cache for further processing.
      --to-html                Convert news to .html format and save it by the specified folder path (FOLDER_PATH=pdf_convert, FILE_NAME=current datetime).
      --to-pdf                 Convert news to .pdf format and save it by the specified folder path (FOLDER_PATH=pdf_convert, FILE_NAME=current datetime).


## Logging
If `--verbose` argument is  **PASSED**, messages with either `INFO` or `ERROR` severities
of `rss_reader` are printed to console,

If `--verbose` argument is passed, then all `rss_reader` logs are printed console. 

## Configuration

Application creates several files:
+ converted to supported formats directories and files: 
  Folders:
    `html_convert`/,
    `pdf_convert`/,
    `img_storage`/,
  Files:
    `local_storage.json`
Application uses `base.htm` file as core of html stucture and uses it for creating new html formatted files    
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
          "Source": "https://news.yahoo.com/rss/",
          "News title:": "More than 1 million voters switch to GOP in warning for Dems",
          "News date:": "2022-06-27 04:08:17",
          "News link:": "https://news.yahoo.com/more-1-million-voters-switch-040817454.html",
          "News source:": "http://www.ap.org/",
          "News image_link:": "https://s.yimg.com/uu/api/res/1.2/j8.JKTuo4zusFSxicKl6iw--~B/aD00MDAwO3c9NjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/f2da5e0ede64ea49e83215a3895b1ac5"
      },
      {
          "Source": "https://news.yahoo.com/rss/",
          "News title:": "The impact of Kavanaugh's confirmation on the 2018 elections may reveal how the reversal of Roe v. Wade could impact this year's midterms",
          "News date:": "2022-06-27 00:36:15",
          "News link:": "https://news.yahoo.com/impact-kavanaughs-confirmation-2018-elections-003615363.html",
          "News source:": "https://www.insider.com/",
          "News image_link:": "https://s.yimg.com/uu/api/res/1.2/XEOtLfPIRULP6UAqNAihlA--~B/aD00NDgwO3c9NTk3MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/insider_articles_922/9ef49ef9b6cfe0e457ff6a2ebc08d87f"
      },
      {
          "Source": "https://news.yahoo.com/rss/",
          "News title:": "\"It's a terrible scene\": At least 21 teens die in tavern mystery",
          "News date:": "2022-06-26 18:06:00",
          "News link:": "https://news.yahoo.com/terrible-scene-least-21-teens-180658249.html",
          "News source:": "https://www.cbsnews.com/",
          "News image_link:": "https://s.yimg.com/uu/api/res/1.2/7fJJnU5hoPxnY6a5h0Ki5g--~B/aD0yNTYwO3c9Mzg0MDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/cbs_news_897/0086668e97cf2885e4decaffd9611be7"
      },
      {
          "Source": "https://news.yahoo.com/rss/",
          "News title:": "Officials: Georgia man sentenced to die kills self in prison",
          "News date:": "2022-06-27 12:50:43",
          "News link:": "https://news.yahoo.com/officials-georgia-man-sentenced-die-125043110.html",
          "News source:": "http://www.ap.org/",
          "News image_link:": "https://s.yimg.com/uu/api/res/1.2/zEeBoPLQVzw1u2VjZt.THA--~B/aD03NDk7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap.org/5cf8e923a8d9dec8758480785184f376"
      },
      {
          "Source": "https://news.yahoo.com/rss/",
          "News title:": "Navy SEALs 'Hell Week' autopsy reveals cause of death of Manalapan man four months later",
          "News date:": "2022-06-26 09:00:34",
          "News link:": "https://news.yahoo.com/navy-seals-hell-week-autopsy-090034460.html",
          "News source:": "https://www.app.com",
          "News image_link:": "https://s.yimg.com/uu/api/res/1.2/Gw1CaDrK1F6QV9TZjnZ8bw--~B/aD0xNjAwO3c9MjQwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/app-com-asbury-park-press/ad51ae10218c6faadf835e52e3616c42"
      }
    ...

*Some notes*:

+ `--json`-printed results are different from ones, stored in cache; as the cache file is just json formatted file the user can easily explore and
  modify it (modifing is not reccomended), whereas `--json` argument is a part of the user interface, that's why its output is user-friendly.

`--json` output example:

    {
      "Feed title": "Yahoo News - Latest News & Headlines",
      "Feed link": "https://www.yahoo.com/news",
      "Feed description:": "The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
      "Feed date:": "Mon, 27 Jun 2022 10:05:03 -0400",
      "Feed items": [
            {
                "Source": "https://news.yahoo.com/rss/",
                "News title:": "Officials: Georgia man sentenced to die kills self in prison",
                "News date:": "2022-06-27 12:50:43",
                "News link:": "https://news.yahoo.com/officials-georgia-man-sentenced-die-125043110.html",
                "News source:": "http://www.ap.org/",
                "News image_link:": "https://s.yimg.com/uu/api/res/1.2/zEeBoPLQVzw1u2VjZt.THA--~B/aD03NDk7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/ap.org/5cf8e923a8d9dec8758480785184f376"
            },
            {
                "Source": "https://news.yahoo.com/rss/",
                "News title:": "13 daring looks celebrities wore on the BET Awards red carpet",
                "News date:": "2022-06-27 12:35:18",
                "News link:": "https://news.yahoo.com/13-daring-looks-celebrities-wore-123518632.html",
                "News source:": "https://www.insider.com/",
                "News image_link:": "https://s.yimg.com/uu/api/res/1.2/28ulMokGwYz3HLNudzDI_A--~B/aD0xOTk5O3c9MjY2NjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/insider_articles_922/f18744f132d7bb2db49022dae6704f4d" 
            },
            {
                "Source": "https://news.yahoo.com/rss/",
                "News title:": "Navy SEALs 'Hell Week' autopsy reveals cause of death of Manalapan man four months later",
                "News date:": "2022-06-26 09:00:34",
                "News link:": "https://news.yahoo.com/navy-seals-hell-week-autopsy-090034460.html",
                "News source:": "https://www.app.com",
                "News image_link:": "https://s.yimg.com/uu/api/res/1.2/Gw1CaDrK1F6QV9TZjnZ8bw--~B/aD0xNjAwO3c9MjQwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/app-com-asbury-park-press/ad51ae10218c6faadf835e52e3616c42"
            }
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

## Testing

Modules tested:

+ to_html.py
+ to_pdf.py
+ rss_reader.py
    (
      test_convert_to_html(),
      test_convert_to_pdf(),
      test_url_validation(),
      test_args_limit(),
      test_args_source(),
      test_args_date(),
      test_clean_desc()

    )
Before testing please pay attention to notes inside the functions. Some test require folders or images which are stored locally. Best sollution is to run the utility couple of times checking with different arguments and optins. 
project is tested for the file convertions, url validation, argparse options and decoding the html functions.

In order to run tests, please, install dependencies:

    pip install - r requirements.txt
