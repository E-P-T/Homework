"""
Converter - RSS data converter to target formats.
"""

import json
import os

from ebooklib import epub


class FileError(Exception):
    """
    Save file exception.
    """
    pass


class Converter:
    """RSS data converter to target formats."""

    @classmethod
    def to_text(cls, feed_list):
        """
        Convert `feed_list` data to text format for console output.
        """
        # RSS channels list
        channel_list = []

        for feed in feed_list:
            # List of channel data blocks
            channel_data = []

            # Add channel title
            channel_data.append(f"\nFeed: {feed['channel']}\n\n")

            for entry in feed['entries']:
                # Add enty title block
                channel_data.append(f"Title: {entry['title']}\n")

                # Add entry date block
                if entry['date'] is not None:
                    channel_data.append(f"Date: {entry['date']}\n")

                # Add entry link block
                channel_data.append(f"Link: {entry['link']}\n")

                # Add entry description block
                if entry['description'] is not None:
                    channel_data.append(f"\n{entry['description']}\n\n")

                # Add links list block
                channel_data.append(f"\nLinks:\n[1]: {entry['link']} (link)\n")
                if entry['image_link'] is not None:
                    channel_data.append(f"[2]: {entry['image_link']} (image)\n")

                channel_data.append("\n")

            # Merge channel blocks
            channel_list.append(''.join(channel_data))

        return ''.join(channel_list)

    @classmethod
    def to_json(cls, feed_list):
        """
        Convert `feed_list` data to json format.
        """
        # Image data & formatted date shouldn't go to json
        for feed in feed_list:
            for entry in feed['entries']:
                del entry['date_fmt']
                del entry['image_data']

        return json.dumps(feed_list, ensure_ascii=False, indent=4)

    @classmethod
    def save_html(cls, feeds, path):
        """
        Save `feeds` data into html file with images.
        """
        # Separate path and filename
        dir, fname = os.path.split(path)

        # Set dirname for images
        img_dname = f"{fname} - images"

        try:
            # Create directory for images
            if not os.path.exists(os.path.join(dir, img_dname)):
                os.mkdir(os.path.join(dir, img_dname))

            with open(path, "w", encoding='utf-8') as f:
                content = ""
                for feed in feeds:
                    # Add channel title
                    content += f"""<h1><a href="{feed['url']}">{feed['channel']}</a></h1>"""

                    for entry in feed['entries']:
                        # Set entry title & link
                        header = f"""<h2><a href="{entry['link']}">{entry['title']}</a></h2>"""

                        if entry['date']:
                            header += f"<h3>{entry['date']}</h3>"

                        # Set entry description
                        decription = ""

                        if entry['description']:
                            decription = f"""<p>{entry['description']}</p>"""

                        image_fname = str(hash(entry['image_link']))

                        # Save image
                        image = ""

                        if entry['image_data']:
                            with open(os.path.join(dir, img_dname, image_fname), "wb") as img:
                                img.write(entry['image_data'])
                            image = f"""<img src="{img_dname}/{image_fname}" width=200>"""

                        # Merge components
                        content += f"{header}{image}{decription}"

                    # Add channels delimiter
                    content += "<hr>"

                html_template = """<html>
                    <head><title>{}</title></head>
                    <body>{}</body>
                </html>"""

                f.write(html_template.strip().format("RSS news", content))

        except PermissionError:
            raise FileError(f"Permission denied for '{path}'")
        except Exception:
            raise FileError(f"Unable to save html into '{path}'")

    @classmethod
    def save_epub(cls, feeds, path):
        """
        Save `feeds` data into epub file.
        """
        book = epub.EpubBook()
        book.set_title('RSS news')

        chapters = []
        for i, feed in enumerate(feeds):
            # Set channel title & url
            chapter = epub.EpubHtml(title=f"Channel {i}", file_name=f"ch_{i}.xhtml")
            chapter.content = f"""<h1><a href="{feed['url']}">{feed['channel']}</a></h1>"""

            for entry in feed['entries']:
                # Set entry title & link
                header = f"""<h2><a href="{entry['link']}">{entry['title']}</a></h2>"""

                if entry['date']:
                    header += f"<h3>{entry['date']}</h3>"

                # Set entry description
                decription = ""

                if entry['description']:
                    decription = f"""<p>{entry['description']}</p>"""

                # Add image
                image = ""

                if entry['image_data']:
                    image_fname = str(hash(entry['image_link']))
                    img = epub.EpubItem(file_name=image_fname, media_type="ITEM_IMAGE")
                    img.content = entry['image_data']
                    book.add_item(img)
                    image = f"""<div><img src="{image_fname}" width=200></div>"""

                # Merge components
                chapter.content += f"{header}{image}{decription}"

            chapters.append(chapter)
            book.add_item(chapter)

        book.spine = chapters

        try:
            writer = epub.EpubWriter(path, book, {})
            writer.process()
            writer.write()
        except PermissionError:
            raise FileError(f"Permission denied for '{path}'")
        except Exception:
            raise FileError(f"Unable to save epub into '{path}'")
