# RSS reader

Pure Python command-line RSS reader.

## Requirements

The utility requires [**`python 3.9`**](https://www.python.org/downloads/) interpreter with [**`pip`**](https://pypi.org/project/pip/) installing tool.

On the command line the interpreter can be typed as `python`, `python3`, `python3.9` (depending on OS, version, etc.).

To be specific this readme has decided to use the name `python`.

## Dependencies

All extra packages listed in the `requirements.txt`:

- [**`beautifulsoup4`**](https://pypi.org/project/beautifulsoup4/) `4.11.1` — Screen-scraping library
- [**`coverage`**](https://pypi.org/project/coverage/) `6.2` — Code coverage measurement for Python
- [**`lxml`**](https://pypi.org/project/lxml/) `4.8.0` — Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API
- [**`requests`**](https://pypi.org/project/requests/) `2.26.0` — Python HTTP for Humans

To install extra packages automatically set the working directory to the project root `rss_reader/` and execute*:

```sh
> python -m pip install -r requirements.txt
```

**Super user privileges may be required to install extra packages. If so, then use* `sudo` *command on Linux or run terminal as administrator on Windows.*

## Usage

The utility can handle multiple arguments.

To show help message below use `-h/--help` argument.

```sh
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [source]

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
```

## Examples:

Set the working directory to the project root `rss_reader/` and execute:

- Show utility version:
  ```sh
  > python rss_reader.py --version
  Version 1.1
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

## JSON format

The utility can export the feed into JSON format for console output.
The structure is shown below:

```python
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
```

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
