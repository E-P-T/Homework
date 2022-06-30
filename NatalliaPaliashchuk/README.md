# RSS reader
Pure Python command-line RSS reader
___
## Installation
The following dependencies are required for installation:
- Python 3.9 or above
- PIP

### Install CLI utility
`# python setup.py install`\
### Using the application without installation of CLI utility
- install all dependencies\
`$ pip install -r requirements.txt`
- run the application using `rss_reader.py` file\
Example:\
`$ python rss_reader.py --version`
___
## Usage
`rss_reader [-h] [--version] [--json] [--to-html FILE] [--verbose] [--to-epub FILE] [--limit LIMIT] [--date DATE] source`

| Positional argument | Description |
|-|-|
| `source` | RSS URL | 

| Options |  Actions |
|-|-|
| `--version` | Print version info |
| `--json` | Print result as JSON in stdout |
| `--to-html FILE` | Convert RSS feed into html and save as a file to the path |
| `--verbose` | Outputs verbose status messages |
| `--to-epub DIRECTORY` | Limit news topics if this parameter provided |
| `--limit LIMIT` | Limit news topics if this parameter provided |
| `--date DATE ` | Extract news from archive. Take a start publish date in format YYYYMMDD |
### Examples
`$ python rss_reader.py --limit 1 http://feeds.bbci.co.uk/news/world/rss.xml
Feed: BBC News - World`
Return example
```bash
Title: Jan 6 hearings: Ex-aide paints devastating picture of Trump
Date: 2022-06-29 03:20:29+00:00
Link: https://www.bbc.co.uk/news/world-us-canada-61970258?at_medium=RSS&at_campaign=KARANGA

Enraged president tried to grab the steering wheel to direct his limousine to the Capitol, ex-aide says.
```
`$ rss_reader --json --limit 1 https://tech.onliner.by/feed`\
Return example
```json
{
  "feed_title": "Технологии Onlíner",
  "feed_items": [
    {
      "item_title": "Чип М2 в новом MacBook может нагреваться до 108 градусов",
      "item_pub_date": "2022-06-30 17:20:10+03:00",
      "item_url": "https://tech.onliner.by/2022/06/30/chip-m2-v-novom-macbook-mozhet-nagrevatsya-do-108-gradusov",
      "item_desc_text": "[1]Новый чип М2 оказался не столь революционным, как его предшественник. Более того, новинка склонна к перегреву и, как следствие, троттлингу, то есть жесткому снижению частот. К таким выводам пришел блогер из Max Tech. Он заполучил новый MacBook Pro на М2 и запустил на нем экспорт видео в формате RAW и с разрешением 8K.[2 Читать далее…]",
      "item_desc_links": [
        {
          "link_pos": 1,
          "link_url": "https://content.onliner.by/news/thumbnail/7b957a17487635c74ef5a743f07ebe75.jpeg",
          "link_type": "image"
        },
        {
          "link_pos": 2,
          "link_url": "https://tech.onliner.by/2022/06/30/chip-m2-v-novom-macbook-mozhet-nagrevatsya-do-108-gradusov",
          "link_type": "link"
        }
      ],
      "item_image_url": "https://content.onliner.by/news/default/7b957a17487635c74ef5a743f07ebe75.jpeg"
    }
  ]
}
```
`$ ./rss_reader.py --limit 1 https://www.dailymail.co.uk/articles.rss`\
`$ ./rss_reader.py --json --date 20000101 https://www.dailymail.co.uk/articles.rss`\
Return example
```json
{
  "feed_title": " Articles | Mail Online",
  "feed_items": [
    {
      "item_title": "Nick Kyrgios admits he spat in the direction of an abusive spectator at Wimbledon",
      "item_pub_date": "2022-06-29 07:48:27+01:00",
      "item_url": "https://www.dailymail.co.uk/sport/sportsnews/article-10962269/Nick-Kyrgios-admits-spat-direction-abusive-spectator-Wimbledon.html?ns_mchannel=rss&ito=1490&ns_campaign=1490",
      "item_desc_text": "The Australian called one line judge 'a snitch' for reporting his abuse and suggested another was in his 90s and 'can't see the ball' during his five-set win over Britain's Paul Jubb.",
      "item_desc_links": [],
      "item_image_url": "https://i.dailymail.co.uk/1s/2022/06/28/19/59635777-0-image-a-46_1656440320325.jpg"
    }
  ]
}
```
___
## Caching
The application provides cashing RSS feed using `cache.pk1` file in the application directory. The option `--date`  with date in `%Y%m%d` format can be used to read cashed news from the specified date also without Internet connection.
___
## Tests
To run unittests use the following command:\
`$ python -m unittest discover`
___
