import warnings
from rss_parser.parsers import Parser

warnings.filterwarnings("ignore", module="bs4")


def main():
    parser = Parser()
    try:
        result = parser.start_parse()
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
