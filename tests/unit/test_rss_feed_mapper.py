from datetime import datetime, timezone

from rss_parse.parse.rss_feed import RssItem, RssFeed
from rss_parse.parse.rss_mapper import RssJsonMapper


def test_rss_json_mapper_to_json():
    rss_feed = RssFeed([
        RssItem("title1", "description1", datetime(2020, 11, 11, tzinfo=timezone.utc), "link1", "image_url1",
                source="source1"),
        RssItem("title2", "description2", datetime(2020, 10, 10, tzinfo=timezone.utc), "link2", "image_url2",
                source="source2"),
    ])
    expected = '{"item": [' \
               '{"title": "title1", "link": "link1", "pubDate": "2020-11-11 00:00:00", ' \
               '"description": "description1", "image": "image_url1", "source": "source1"}, ' \
               '{"title": "title2", "link": "link2", "pubDate": "2020-10-10 00:00:00", ' \
               '"description": "description2", "image": "image_url2", "source": "source2"}' \
               ']}'

    actual = RssJsonMapper().to_json(rss_feed)

    assert actual == expected


def test_rss_json_mapper_from_json():
    expected = RssFeed([
        RssItem("title1", "description1", datetime(2020, 11, 11, tzinfo=timezone.utc).astimezone(), "link1",
                "image_url1", source="source1"),
        RssItem("title2", "description2", datetime(2020, 10, 10, tzinfo=timezone.utc).astimezone(), "link2",
                "image_url2", source="source2"),
    ])
    rss_json = '{"item": [' \
               '{"title": "title1", "link": "link1", "pubDate": "2020-11-11 00:00:00", ' \
               '"description": "description1", "image": "image_url1", "source": "source1"}, ' \
               '{"title": "title2", "link": "link2", "pubDate": "2020-10-10 00:00:00", ' \
               '"description": "description2", "image": "image_url2", "source": "source2"}' \
               ']}'

    actual = RssJsonMapper().from_json(rss_json)

    assert actual == expected
