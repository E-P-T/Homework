"""
Converter - RSS data converter to target formats.
"""

import json


class Converter:
    """RSS data converter to target formats."""

    @classmethod
    def to_text(cls, feed):
        """
        Convert channel's `feed` data to text format for console output.
        """
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

        return ''.join(channel_data)

    @classmethod
    def to_json(cls, feed):
        """
        Convert channel's `feed` data to json format.
        """
        return json.dumps(feed, ensure_ascii=False, indent=4)
