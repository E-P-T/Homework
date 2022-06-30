import argparse
import sys
from loguru import logger

from reader import Reader
from printer import Printer
from converter import Converter

VERSION = '4.0'

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Choose type of the interface")
    parser.add_argument("-v", "--version", action="store_true", help="Print version info")
    parser.add_argument("--json", action="store_true", help="Print result as JSON")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages.Print logs.")
    parser.add_argument("--limit", type=int,
                        help="Limit news topics. If it's not specified, then you get all available feed")
    parser.add_argument("--date", type=str,
                        help="It should take a date in Ymd format.The new from the specified day will be printed out.")
    parser.add_argument("--html", action="store_true", help="It convert data to HTML-format in file output.html.")
    parser.add_argument("source", nargs="?", type=str, help="RSS URL")
    args = parser.parse_args()
    return args


def date_search(data: dict, date: str) -> dict:
    if len(date) < 7 or not (date.isdigit()):
        logger.info(f"Invalid date.{date}!")
        print(f"Invalid date.{date}. Use pattern YMD!")
        raise sys.exit()

    logger.debug("Start data searching (debug)!")
    new_dates = []
    month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
             "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    for d in data["pubDate"]:
        for key in month.keys():
            if key in d:
                new_dates.append(d.replace(key, month[key]))
    new_date = date[6::] + ' ' + date[4:6:] + ' ' + date[:4:]
    list_of_index = []

    for i in range(len(new_dates)):
        if new_date in new_dates[i]:
            list_of_index.append(i)
    if len(list_of_index) == 0:
        logger.info(f"No information found.{date}!")
        print(f"No information found.{date}.")
        raise sys.exit()
    new_data = {"name": data["name"],
                "size": len(list_of_index),
                "title": [data["title"][i] for i in list_of_index],
                "pubDate": [data["pubDate"][i] for i in list_of_index],
                "description": [data["description"][i] for i in list_of_index],
                "link": [data["link"][i] for i in list_of_index]
                }
    return new_data


def main():
    if not args().verbose:
        logger.remove()
    if args().version:
        logger.debug("Version call (debug)!")
        print('Version:' + VERSION)
        logger.info("Print version (info)!")
        sys.exit()
    elif args().date and args().source == None:
        converter = Converter()
        logger.debug("Convert to json call (debug)!")
        converter.to_JSON(date_search(converter.from_json(), args().date))
        logger.info("Succesful data search (info)!")
        logger.info("Save to json file (info)!")
        printer = Printer(converter.from_json())
        print(printer)
    else:
        logger.debug("Reader call (debug)!")
        my_reader = Reader(args().source, args().limit) if args().limit else Reader(args().source)
        converter = Converter(my_reader)
        logger.debug("Convert to json call (debug)!")
        converter.to_JSON()
        logger.info("Save to json file (info)!")
        if args().date:
            date_search(converter.from_json(), args().date)
            converter.to_JSON(date_search(converter.from_json(), args().date))
            logger.info("Succesful data search (info)!")
        else:
            converter.to_JSON()
            logger.info("Save to json file (info)!")
        logger.debug("Printer call (debug)!")
        printer = Printer(converter.from_json())
        print(printer)
        logger.info("Print  information (info)!")

    if args().json:
        logger.debug("Json-style call (debug)!")
        print("Json style:\n")
        print(converter.from_json())
        logger.info("Print json-style information (info)!")

    if args().html:
        try:
            converter.to_HTML()
        except Exception:
            logger.error(f"Error with HTML-file(error)!")
            print('Error: convert to HTML-file does not work with this URL ')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.error(f"Unexpected error (error)!")
        print(f"Unexpected error")
        raise sys.exit()

# python f.py "https://www.onliner.by/feed" --limit 1        +
# python rss_reader.py "https://www.buzzfeed.com/quizzes.xml" --limit 2 --json --verbose

# python rss_reader.py "https://www.buzzfeed.com/quizzes.xml" --limit 3
# python rss_reader.py  "https://feeds.fireside.fm/bibleinayear/rss" --limit 3    +
# python rss_reader.py  "https://feeds.simplecast.com/qm_9xx0g" --limit 1   +


# python rss_reader.py  "https://realpython.com/atom.xml" --limit 3
# python rss_reader.py --date 20220620
# python rss_reader.py --json