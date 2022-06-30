## RSS_reader

Pure Python command-line RSS reader.

The project requires [**`python 3.9`**](https://www.python.org/downloads/) interpreter
with [**`pip`**](https://pypi.org/project/pip/) installing
tool, [**`setuptools`**](https://pypi.org/project/setuptools/) installing tool for using the project.

## Specification

The project works with Command Line Arguments.

```shell
usage: __main__.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
  --date  DATE      Publishing date of the news. Forma of the input: %Y%m%d
  --to-pdf       Converting to pdf
  --to-html      COnverting to html

```

The textbox below provides an example of how you can use different arguments:

```shell
source --limit LIMIT --date DATE --json --to-pdf
```

## Dependencies

- [**`beautifulsoup4`**](https://pypi.org/project/beautifulsoup4/) `4.11.1` — Web-scraping library
- [**`lxml`**](https://pypi.org/project/lxml/) `4.8.0` — Powerful and Pythonic XML processing library combining
  libxml2/libxslt with the ElementTree API
- [**`requests`**](https://pypi.org/project/requests/) `2.26.0` — Library for sending requests to websites

## JSON Format

```python
{
    "https://www.yahoo.com/news": [
        {
            "Item": "Researchers caution beachgoers ahead of white shark season",
            "Date": "2022-06-29T19:30:51Z",
            "Link": "https://news.yahoo.com/researchers-caution-beachgoers-ahead-white-193051023.html",
            "Description": "Description is unavailable",
            "Links": [
                "https://news.yahoo.com/researchers-caution-beachgoers-ahead-white-193051023.html",
                "https://s.yimg.com/uu/api/res/1.2/ykqmnXesQXwm5.L8QhthDQ--~B/aD0yNDExO3c9MzYxNjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/3b7c0a4dbc713cf2b1b70c5b34a664f8"
            ]
        },
        {
            "Item": "'Diehard' Nintendo fan spent over $40,000 buying stock and then asked top executives why the company won't make more of a fan-favorite series",
            "Date": "2022-06-30T17:27:41Z",
            "Link": "https://news.yahoo.com/diehard-nintendo-fan-spent-over-172741706.html",
            "Description": "Description is unavailable",
            "Links": [
                "https://news.yahoo.com/diehard-nintendo-fan-spent-over-172741706.html",
                "https://s.yimg.com/uu/api/res/1.2/764kQnDLXCrYLFqopgCZAA--~B/aD0zMTIyO3c9NDE2NDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_888/aafd91889bdbdf38c0ce2305c03192f5"
            ]
        }
    ]
}
```




