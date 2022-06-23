# Python RSS Parser for EPAM Training Center

## About

`rss-parser` - command line utility that parses entered RSS URL and returns clean data (human readable)

## Installation

```bash
git clone https://github.com/KirylLitoshka/Homework.git
pip install . # or python setup.py install
```
or
```bash
pip install -r requirements.txt
```


## Usage
#### For usage without installation, after changing directory you can use
```bash
python rss_parser.py ...args #see Usage directory
```

After installing the package, use `rss_parser [args]` command in console, if you haven't installed the package, use `python rss_parser.py [args]` 
from downloaded folder 
```bash
usage: rss_parser [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] [source] 

positional arguments:
  source         RSS URL

options:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
  --date DATE    Print result with actual publishing date of the news
```
Notification: `--date` argument accept date in YYYYMMDD format only (Example: 20220618). Also, each RSS feed parsing is saved to directory depending on entered command
(see `rss_parser/storage/local` if `python rss_parser.py [args]` is used and `{env}\lib\rss_parser\storage\local` for installed version)