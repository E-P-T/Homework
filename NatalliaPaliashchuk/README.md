# RSS reader
Pure Python command-line RSS reader.
___
## Installation
### Install all dependencies
`$ pip install -r requirements.txt`
### Install CLI utility
`$ python setup.py install`
### The application can be used also without installation of CLI utility
To run the application use `rss_reader.py` file.\
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
      "item_title": "Sony представила игровые мониторы для PS5 и геймерские наушники. Известны цены",
      "item_pub_date": "2022-06-29 09:44:11+03:00",
      "item_url": "https://tech.onliner.by/2022/06/29/sony-predstavila-igrovye-monitory-dlya-ps5-i-gejmerskie-naushniki-izvestny-ceny",
      "item_desc_text": "[1]Sony официально представила игровой бренд InZone — под ним будут выходить гаджеты для геймеров. Начали с мониторов и наушников, [2 сообщает] engadget.[3 Читать далее…]",
      "item_desc_links": [
        {
          "link_pos": 1,
          "link_url": "https://content.onliner.by/news/thumbnail/625fdac3c028b390f2d80f9c26fe90de.jpeg",
          "link_type": "image"
        },
        {
          "link_pos": 2,
          "link_url": "https://www.engadget.com/sony-inzone-gaming-monitors-headsets-specs-pricing-availability-210056794.html",
          "link_type": "link"
        },
        {
          "link_pos": 3,
          "link_url": "https://tech.onliner.by/2022/06/29/sony-predstavila-igrovye-monitory-dlya-ps5-i-gejmerskie-naushniki-izvestny-ceny",
          "link_type": "link"
        }
      ],
      "item_image_url": "https://content.onliner.by/news/default/625fdac3c028b390f2d80f9c26fe90de.jpeg"
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
