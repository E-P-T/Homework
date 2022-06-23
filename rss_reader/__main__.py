"""Program entry point."""


from rss_reader.starter.base import (create_logger,
                                     init_arguments_functionality as iaf)


def main():
    args = iaf()


if __name__ == "__main__":
    main()
