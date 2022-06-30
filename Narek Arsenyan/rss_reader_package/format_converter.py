"""
Module for converting feeds to specific format

exports FormatConverter
"""

import os
import uuid
import utils.config as config
from utils.config import print
from appdirs import user_data_dir
from yattag import Doc, indent
from ebooklib import epub
from datetime import datetime
from feed import Feed
from utils.count_files import count_files_by_type
from utils.exceptions import NotSupportedConversionFormat

SUPPORTED_FORMATS = ["html", "epub"]

# Global css that is used for html conversion
CSS = """
#feed-images-container { width: 100%; overflow-x: auto; display: flex; flex-direction: row; }
img { height: 200px; width: auto; margin: 0 10px; }
"""


class FormatConverter:
    """
    Class for working with conversion of feeds
    """
    @staticmethod
    def convert_feeds(feeds: [Feed], convert_format: str or None, destination_path: str or None, print_json: bool):
        """
        Function that processes conversion. Does generic part, which is used in all conversion types

        Args:
            feeds:              Feed objects, that should be converted
            convert_format:     conversion format. Supported formats are "epub" and "html"
            destination_path:   location of file, where converted feeds should take place. If destination_path is not
                                provided, user data directory will be used as location (See DOCS)
            print_json:         if feeds should be printed in JSON format in stdout during conversion

        Raises:
            NotSupportedConversionFormat
        """

        config.verbose_print(f"Starting conversion to '{convert_format}'", "bold")
        if convert_format is None or convert_format not in SUPPORTED_FORMATS:
            raise NotSupportedConversionFormat(f"Conversion format '{convert_format}' is not supported")
        else:
            if destination_path is None or not os.path.exists(destination_path):
                print("Warning: Specified directory is wrong or does not exist. "
                      "Falling back for user data directory", "warn")
                destination = user_data_dir(config.appname, config.appauthor)
            else:
                destination = destination_path
            if convert_format == "html":
                FormatConverter.feeds_to_html(feeds, destination)
            elif convert_format == "epub":
                FormatConverter.feeds_to_epub(feeds, destination)
            if print_json:
                config.verbose_print("Printing feeds in JSON format in stdout", "bold")
                for feed in feeds:
                    print(feed.to_json())

    @staticmethod
    def feeds_to_html(feeds: [Feed], destination_path: str):
        """
        Function that converts feeds to html format file in specified directory

        Args:
            feeds:              Feed objects, that will be included in html file
            destination_path:   location, where converted html file will be saved
        """

        config.verbose_print("Creating html file for feeds", "bold")
        html_files_count = count_files_by_type(destination_path, ".html")
        doc, tag, text = Doc().tagtext()
        with tag("html"):
            with tag("head"):
                with doc.tag('style', type='text/css'):
                    config.verbose_print("Applying css", "bold")
                    doc.asis(CSS)
                doc.stag("meta", charset="UTF-8")
            with tag("body"):
                config.verbose_print("Appending feeds to html", "bold")
                for feed in feeds:
                    doc.asis(FormatConverter.single_feed_to_html_content(feed, False))
        config.verbose_print("Saving html file", "bold")
        with open(os.path.join(destination_path, f"Feeds {html_files_count + 1}.html"), "w") as html_file:
            html_file.write(indent(doc.getvalue()))
        print(f"Html file saved in {destination_path}", "green")

    @staticmethod
    def feeds_to_epub(feeds: [Feed], destination_path: str):
        """
        Function that converts feeds to epub format file in specified directory

        Args:
            feeds:              Feed objects, that will be included in html file
            destination_path:   location, where converted html file will be saved
        """

        config.verbose_print("Creating html file for feeds", "bold")
        epub_files_count = count_files_by_type(destination_path, ".epub")
        new_file_name = f"Feeds {epub_files_count + 1}"
        book = epub.EpubBook()

        book.set_identifier(str(uuid.uuid4()))
        book.set_title(new_file_name)

        book.add_author(config.appauthor)

        spine = ["nav"]

        config.verbose_print("Creating chapters for epub book", "bold")
        for i in range(0, len(feeds)):
            doc, tag, text = Doc().tagtext()
            with tag("html"):
                with tag("head"):
                    with doc.tag('style', type='text/css'):
                        doc.asis(CSS)
                with tag("body"):
                    doc.asis(FormatConverter.single_feed_to_html_content(feeds[i], True))
            chapter = epub.EpubHtml(title=feeds[i].title, file_name=f"chap_{i + 1}.xhtml")
            chapter.content = indent(doc.getvalue())
            book.add_item(chapter)
            spine.append(chapter)

        config.verbose_print("Creating Table of Contents", "bold")
        book.toc = tuple(spine[1::])

        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        book.spine = spine

        config.verbose_print("Saving epub book", "bold")
        epub.write_epub(os.path.join(destination_path, new_file_name + ".epub"), book, {})
        print(f"Epub book saved in {destination_path}", "green")

    @staticmethod
    def single_feed_to_html_content(feed: Feed, for_book: bool) -> str:
        """
        Function that converts single Feed object to html body content. Used for both .epub and .html file conversions

        Args:
            feed:       Feed object
            for_book:   argument, that specifies if converting is for book type conversion or no

        Returns:
            str:        Feed object converted to html string, which contains Feed data
        """

        config.verbose_print(f"Creating feed content in html format (Feed: {feed.title})", "bold")
        doc, tag, text = Doc().tagtext()
        with tag("h3"):
            text(feed.title)
        with tag("p"):
            text(str(datetime.strptime(feed.date, "%a, %d %b %Y %H:%M:%S %z").__format__("%d.%m.%Y, %H:%M")))
        doc.stag("br")
        if not for_book:
            with tag("div", id="feed-images-container"):
                if len(feed.media_links) < 1:
                    text("No media was provided")
                else:
                    for media_link in feed.media_links:
                        if media_link.link_type == "image":
                            doc.stag("img", src=media_link.href, klass="feed-image")
                        if media_link.link_type == "audio":
                            doc.stag("audio", controls=True, src=media_link.href)
                        if media_link.link_type == "video":
                            with tag("video", controls=True):
                                doc.stag("source", src=media_link.href)
        doc.stag("br")
        doc.asis(feed.content)
        doc.stag("br")
        with tag("a", href=feed.link, target="_blank"):
            text("Read full article")
        doc.stag("br")
        doc.stag("br")
        with tag("span"):
            with tag("strong"):
                text("Related links:")
        with tag("div"):
            for i in range(0, len(feed.non_media_links)):
                with tag("div"):
                    with tag("span"):
                        text(f"[{i + 1}]")
                    with tag("a", href=feed.non_media_links[i].href, target="_blank"):
                        text(feed.non_media_links[i].href)
        if not for_book:
            for i in range(0, 5):
                doc.stag("br")
        doc.stag("hr")

        return doc.getvalue()
