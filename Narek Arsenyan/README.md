
# Feed Format

---

**`Feed:`**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Feed source title

&nbsp;

**`Title:`**&nbsp;&nbsp;&nbsp;&nbsp;Title of the new

**`Date:`**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Publishing date of the new

**`Link:`**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Link of the new

&nbsp;

### `Content of the new`

&nbsp;

**`Links:`**


`[1]: Link 1` (type of source)

`[2]: Link 2` (type of source)

.

.

.

`[n]: Link n` (type of source)


---

# Feed Format (JSON)

---

```json
{
    "source_title": "Feed source title",
    "source_url": "Feed source url",
    "title": "Title of the new",
    "date": "Publishing date of the new",
    "link": "Link of the new",
    "content": "Content of the new",
    "non_media_links": [
        {
            "href": "url of link used in the new",
            "link_type": "link type of the link"
        }
    ],
    "media_links": [
        {
            "href": "url of media used in the new",
            "link_type": "type of media"
        }
    ]
}
```

---

# Feed caching

---

Previously fetched feeds are cached in user cache directory.

**For macOS:**

>/Users/[USER]/Library/Caches/RSSReader

**For Linux:**

>/home/[USER]/.cache/RSSReader

**For Windows 7:**

>C:\Users\[USER]\AppData\Local\nmac99\RSSReader\Cache

## Format of caching

Fetched feeds are stored in `[DATE].json` files, where `[DATE]` is the date of publication of the feed.

Inside `.json` file is JSON object where keys are fetched feeds' sources and values are feeds' data list in JSON format.

**Example:**

`2022-06-11.json`

```json
{
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms": [
        "{\n    \"source_title\": Times of India,\n    \"source_url\": \"https://timesofindia.indiatimes.com/rssfeedstopstories.cms\",\n    \"title\": \"Presidential polls: Mamata invites 22 oppn CMs, leaders for joint meeting on June 15\",\n    \"date\": \"2022-06-11T16:22:36+05:30\",\n    \"link\": \"https://timesofindia.indiatimes.com/india/presidential-polls-mamata-invites-22-oppn-cms-leaders-for-joint-meeting-on-june-15/articleshow/92146582.cms\",\n    \"content\": \"With the Rajya Sabha results exposing dissension and lack of cohesion among opposition parties, West Bengal chief minister Mamata Banerjee on Saturday reached out to her counterparts and other leaders to participate in a meeting in Delhi on June 15 to discuss the upcoming presidential polls, which are scheduled for July 18.\",\n    \"non_media_links\": [\n        {\n            \"href\": \"https://timesofindia.indiatimes.com/india/presidential-polls-mamata-invites-22-oppn-cms-leaders-for-joint-meeting-on-june-15/articleshow/92146582.cms\",\n            \"link_type\": \"link\"\n        }\n    ],\n    \"media_links\": []\n}"
    ]
}
```
&nbsp;

3 types of cache checks are implemented:

1. When cache files for dates are exceeding count of 10, the earliest date cache file is deleted
2. When cache sources in one cache file are exceeding count of 10, the first source is deleted with its content
3. When cached feeds in one cache source are exceeding count of 10, the first cached feed in that source is deleted

&nbsp;

When reading from cache, JSON objects are being converted to normalized Feed objects

---

# Feeds conversion

---

Currently, there are **2 types** of conversion available:

1. HTML
2. EPUB

&nbsp;

You can easily convert your feeds to these 2 formats, whether they are newly fetched or were read from cache.

Converted files will be saved in your provided directory, however if that directory does not exist, files will be saved
in user data directory.

**For macOS:**

>/Users/[USER]/Library/Application Support/RSSReader

**For Linux:**

>/home/[USER]/.local/share/RSSReader

**For Windows 7:**

>C:\Users\[USER]\AppData\Local\nmac99\RSSReader
