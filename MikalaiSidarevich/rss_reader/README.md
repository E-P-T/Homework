# RSS reader

Pure Python command-line RSS reader.

## Requirements

The utility requires [**`python 3.9`**](https://www.python.org/downloads/) interpreter with [**`pip`**](https://pypi.org/project/pip/) installing tool, [**`setuptools`**](https://pypi.org/project/setuptools/) installing tool.

On the command line the interpreter can be typed as `python`, `python3`, `python3.9` (depending on OS, version, etc.).

To be specific this readme has decided to use the name `python`.

## Dependencies

All extra packages listed in the `requirements.txt`:

- [**`beautifulsoup4`**](https://pypi.org/project/beautifulsoup4/) `4.11.1` — Screen-scraping library
- [**`EbookLib`**](https://pypi.org/project/EbookLib/) `0.17.1` — Ebook library which can handle EPUB2/EPUB3 and Kindle format
- [**`colorize`**](https://pypi.org/project/colorize/) `1.1.0` — Command line utility to colorize other commands output
- [**`coverage`**](https://pypi.org/project/coverage/) `6.2` — Code coverage measurement for Python
- [**`lxml`**](https://pypi.org/project/lxml/) `4.8.0` — Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API
- [**`requests`**](https://pypi.org/project/requests/) `2.26.0` — Python HTTP for Humans

To install extra packages automatically set the working directory to the project root `rss_reader/` and execute*:

```sh
> python -m pip install -r requirements.txt
```

It's also possible to setup package via **`setuptools`**:

```sh
> python setup.py install
```

**Super user privileges may be required to install extra packages. If so, then use* `sudo` *command on Linux or run terminal as administrator on Windows.*

## Usage

The utility can handle multiple arguments.

To show help message below use `-h/--help` argument.

```sh
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] [--to-epub PATH] [--to-html PATH] [--colorize] [source]

Pure Python command-line RSS reader.

positional arguments:
  source          RSS URL

optional arguments:
  -h, --help      show this help message and exit
  --version       Print version info
  --json          Print result as JSON in stdout
  --verbose       Outputs verbose status messages
  --limit LIMIT   Limit news topics if this parameter provided
  --date DATE     Read cached news by date specified like '%Y%m%d'
  --to-epub PATH  Convert news to epub format
  --to-html PATH  Convert news to HTML format
  --colorize      Colorize console output
```

## Examples:

Set the working directory to the project root `rss_reader/` and execute:

- Show utility version:
  ```sh
  > python rss_reader.py --version
  Version 1.5
  ```

- Show utility version using CLI utility installed:
  ```sh
  > rss_reader --version
  Version 1.5
  ```

- Read 1 news entry from [Yahoo](https://news.yahoo.com/) source:
  ```sh
  > python rss_reader.py https://news.yahoo.com/rss/ --limit 1

  Feed: Yahoo News - Latest News & Headlines

  Title: WNBA star Brittney Griner ordered to trial Friday in Russia
  Date: 2022-06-27T07:41:55Z
  Link: https://news.yahoo.com/us-basketball-star-griner-due-074155275.html

  Shackled and looking wary, WNBA star Brittney Griner was ordered Monday to stand trial by a court near Moscow on cannabis possession charges, about 4 1/2 months after her arrest at an airport while returning to play for a Russian team.  The Phoenix Mercury center and two-time U.S. Olympic gold medalist also was ordered to remain in custody for the duration of her criminal trial, which was to begin Friday.  Griner could face 10 years in prison if convicted on charges of large-scale transportation of drugs.


  Links:
  [1]: https://news.yahoo.com/us-basketball-star-griner-due-074155275.html (link)
  [2]: https://s.yimg.com/ny/api/res/1.2/utfVa4Ach8UgXMMZREmJhg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/uu/api/res/1.2/1THMVZDeZ0z7PVXchxklYw--~B/aD00MDAwO3c9NjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/9f3f122d6d91ff94f9613b5d97409f0f (image)


  ```

- Read from cache 1 news entry for the date `'20220628'` (requires previously stored data):
  ```sh
  > python rss_reader.py --date 20220628 --limit 1

  Feed: Yahoo News - Latest News & Headlines

  Title: Spit, 'disrespect' arrive at Wimbledon as tennis turns ugly
  Date: 2022-06-28T22:01:51Z
  Link: https://news.yahoo.com/spit-disrespect-arrive-wimbledon-tennis-220151441.html

  This is not what one thinks of when pondering the supposedly genteel roots of tennis, and the purportedly proper atmosphere at dates-to-the-1800s Wimbledon, a country club sport being contested at a place officially called the All England Lawn Tennis Club: a player, Nick Kyrgios, capping a first-round victory Tuesday by spitting in the direction of a spectator he said was hassling him.  Like, he literally came to the match to literally just not even support anyone, really.  During the match, which filled the stands at 1,980-seat Court No. 3 — and attracted lengthy lines of folks hoping to eventually be let in, likely owing to the popularity of the anything-can-happen Kyrgios, a 27-year-old from Australia, and the involvement of a local player — Kyrgios asked, without success, to have the fan removed for cursing and sending other verbal abuse his way.


  Links:
  [1]: https://news.yahoo.com/spit-disrespect-arrive-wimbledon-tennis-220151441.html (link)
  [2]: https://s.yimg.com/ny/api/res/1.2/7Oybi_h9sBCC7gjex3GADQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/uu/api/res/1.2/Kn3F_gIJwe0a3uIOU.Tb2w--~B/aD0yMzgxO3c9MzU3MTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/4a35cff443aaabc2b49d94a5e7672369 (image)


  ```
  
- Export all the news entries from [Yahoo](https://news.yahoo.com/) source to the `yahoo.epub` file in the working directory:
  ```sh
  > python rss_reader.py https://news.yahoo.com/rss/ --to-epub yahoo.epub
  ```

## JSON format

The utility can export the feed into JSON format for console output.
The structure is shown below:

```python
[
    {
        "channel": "Channel title",
        "url": "Channel URL",
        "entries": [
            {
                "title": "Entry title",
                "date": "Entry publish date",
                "link": "Entry link",
                "description": "Entry description",
                "image_link": "Entry image link"
            }
        ]
    }
]
```

## Export formats

The utility can export the feed into HTML and Epub formats, use the `--to-html` or `--to-epub` options, respectively.

### HTML format

When export to HTML format the utility saves HTML page into the filepath specified and pictures data into a separate folder named like HTML filepath with suffix ` - images`.

- Produce `yahoo.html` file and `yahoo.html - images/` directory with images  in the `~/rss/` directory:

  ```sh
  > python rss_reader.py https://news.yahoo.com/rss/ --to-html ~/rss/yahoo.html
  ```

### Epub format

When export to Epub format the utility saves Epub file into the filepath specified with pictures data incapsulated.

- Produce `yahoo.epub` in the `~/rss/` directory:

  ```sh
  > python rss_reader.py https://news.yahoo.com/rss/ --to-html ~/rss/yahoo.html
  ```

## Feed cache

RSS feed is cached while reading.

Cache storage is the SQLite3 database, it contains 2 data tables: `channels` and `entries`.

- Table `channels` schema:

  | column  | type   |
  | ------- | ------ |
  | id      | INT PK |
  | channel | TEXT   |
  | url     | TEXT   |

- Table `entries` schema:

  | column      | type   |
  | ----------- | ------ |
  | id          | INT PK |
  | title       | TEXT   |
  | link        | TEXT   |
  | date        | TEXT   |
  | date_fmt    | TEXT   |
  | description | TEXT   |
  | image_link  | TEXT   |
  | image_data  | BLOB   |
  | channel_id  | INT FK |

## Colorized output*

The utility provides colorized console output with `--colorize` option set.

| entity      | color   |                                                             |
| ----------- | ------- | ----------------------------------------------------------- |
| feed title  | magenta | ![FF0090](https://via.placeholder.com/15/FF0090/FF0090.png) |
| entry title | cyan    | ![00FFFF](https://via.placeholder.com/15/00FFFF/00FFFF.png) |
| entry date  | yellow  | ![FFFF00](https://via.placeholder.com/15/FFFF00/FFFF00.png) |
| links       | blue    | ![0000FF](https://via.placeholder.com/15/0000FF/0000FF.png) |
| errors      | red     | ![FF0000](https://via.placeholder.com/15/FF0000/FF0000.png) |

**Colorized mode is enabled on Linux only.*

## Running tests

To run tests set the working directory to the project root `rss_reader/` and execute:

```sh
> python -m unittest
```

To run test coverage checking set the working directory to the project root `rss_reader/` and execute:

```sh
> python -m coverage run -m unittest
> python -m coverage report --include=engine/*
```
