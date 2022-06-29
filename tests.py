import unittest
import rss_reader
import sys


class TestParseArgs(unittest.TestCase):

    def setUp(self):
        self.fake_exit_status = None
        self.orig_sys_exit = sys.exit
        sys.exit = self._fake_sys_exit

    def _fake_sys_exit(self, status=0):
        self.fake_exit_status = status

    def tearDown(self):
        sys.exit = self.orig_sys_exit

    def test_empty(self):
        rss_reader.parse_args([])
        self.assertNotEqual(self.fake_exit_status, None)

    def test_only_url(self):
        args = rss_reader.parse_args(['mockurl'])
        self.assertFalse(args.json)
        self.assertFalse(args.verbose)
        self.assertEqual(args.source, 'mockurl')
        self.assertEqual(args.limit, None)

    def test_version(self):
        rss_reader.parse_args(['--version'])
        self.assertNotEqual(self.fake_exit_status, None)

    def test_json(self):
        args = rss_reader.parse_args(['--json', 'mockurl2'])
        self.assertTrue(args.json)
        self.assertFalse(args.verbose)
        self.assertEqual(args.source, 'mockurl2')
        self.assertEqual(args.limit, None)

    def test_verbose(self):
        args = rss_reader.parse_args(['--verbose', 'mockurl3'])
        self.assertFalse(args.json)
        self.assertTrue(args.verbose)
        self.assertEqual(args.source, 'mockurl3')
        self.assertEqual(args.limit, None)

    def test_limit(self):
        args = rss_reader.parse_args(['--limit', '10', 'mockurl4'])
        self.assertFalse(args.json)
        self.assertFalse(args.verbose)
        self.assertEqual(args.source, 'mockurl4')
        self.assertEqual(args.limit, 10)


class TestParseFeed(unittest.TestCase):

    SAMPLE_2_0 = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
   <channel>
      <title>Liftoff News</title>
      <link>http://liftoff.msfc.nasa.gov/</link>
      <description>Liftoff to Space Exploration.</description>
      <language>en-us</language>
      <pubDate>Tue, 10 Jun 2003 04:00:00 GMT</pubDate>
      <lastBuildDate>Tue, 10 Jun 2003 09:41:01 GMT</lastBuildDate>
      <docs>http://blogs.law.harvard.edu/tech/rss</docs>
      <generator>Weblog Editor 2.0</generator>
      <managingEditor>editor@example.com</managingEditor>
      <webMaster>webmaster@example.com</webMaster>
      <item>
         <title>Star City</title>
         <link>http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp</link>
         <description>&lt;img src="https://example.com/images/logo.png"&gt;How do Americans get ready to work with Russians aboard the International Space Station? They take a crash course in culture, language and protocol at Russia's &lt;a href="http://howe.iki.rssi.ru/GCTC/gctc_e.htm"&gt;Star City&lt;/a&gt;.</description>
         <pubDate>Tue, 03 Jun 2003 09:39:21 GMT</pubDate>
         <guid>http://liftoff.msfc.nasa.gov/2003/06/03.html#item573</guid>
      </item>
      <item>
         <description>Sky watchers in Europe, Asia, and parts of Alaska and Canada will experience a &lt;a href="http://science.nasa.gov/headlines/y2003/30may_solareclipse.htm"&gt;partial eclipse of the Sun&lt;/a&gt; on Saturday, May 31st.</description>
         <pubDate>Fri, 30 May 2003 11:06:42 GMT</pubDate>
         <guid>http://liftoff.msfc.nasa.gov/2003/05/30.html#item572</guid>
      </item>
      <item>
         <title>The Engine That Does More</title>
         <link>http://liftoff.msfc.nasa.gov/news/2003/news-VASIMR.asp</link>
         <description>Before man travels to Mars, NASA hopes to design new engines that will let us fly through the Solar System more quickly.  The proposed VASIMR engine would do that.</description>
         <pubDate>Tue, 27 May 2003 08:37:32 GMT</pubDate>
         <guid>http://liftoff.msfc.nasa.gov/2003/05/27.html#item571</guid>
      </item>
      <item>
         <title>Astronauts' Dirty Laundry</title>
         <link>http://liftoff.msfc.nasa.gov/news/2003/news-laundry.asp</link>
         <description>Compared to earlier spacecraft, the International Space Station has many luxuries, but laundry facilities are not one of them.  Instead, astronauts have other options.</description>
         <pubDate>Tue, 20 May 2003 08:56:02 GMT</pubDate>
         <guid>http://liftoff.msfc.nasa.gov/2003/05/20.html#item570</guid>
      </item>
   </channel>
</rss>"""

    def test_sample20(self):
        content = self.SAMPLE_2_0
        feed = rss_reader.parse_feed(content)
        self.assertEqual(feed['title'], 'Liftoff News')
        self.assertEqual(feed['link'], 'http://liftoff.msfc.nasa.gov/')
        self.assertEqual(feed['description'], 'Liftoff to Space Exploration.')
        self.assertEqual(len(feed['items']), 4)
        self.assertEqual(feed['items'][0]['title'], 'Star City')
        self.assertEqual(feed['items'][0]['link'], 'http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp')
        self.assertEqual(feed['items'][0]['pubDate'], 'Tue, 03 Jun 2003 09:39:21 GMT')
        self.assertEqual(feed['items'][0]['description'], '[image 2]How do Americans get ready to work with Russians aboard the International Space Station? They take a crash course in culture, language and protocol at Russia\'s Star City[3].')
        self.assertEqual(len(feed['items'][0]['links']), 3)
        self.assertEqual(feed['items'][0]['links'][0], ('http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp', 'link'))
        self.assertEqual(feed['items'][0]['links'][1], ('https://example.com/images/logo.png', 'image'))
        self.assertEqual(feed['items'][0]['links'][2], ('http://howe.iki.rssi.ru/GCTC/gctc_e.htm', 'link'))

    def test_illformed(self):
        with self.assertRaises(ValueError):
            content = "Invalid RSS"
            rss_reader.parse_feed(content)

    def test_limit(self):
        content = self.SAMPLE_2_0
        feed = rss_reader.parse_feed(content)
        rss_reader.limit_feed(feed, 1)
        self.assertEqual(len(feed['items']), 1)

    def test_overlimit(self):
        content = self.SAMPLE_2_0
        feed = rss_reader.parse_feed(content)
        rss_reader.limit_feed(feed, 5)
        self.assertEqual(len(feed['items']), 4)

    def test_text(self):
        content = self.SAMPLE_2_0
        feed = rss_reader.parse_feed(content)
        rss_reader.limit_feed(feed, 1)
        text = rss_reader.format_text(feed)
        self.assertEqual(text,
                         "Feed: Liftoff News\n\nTitle: Star City\n"
                         "Date: Tue, 03 Jun 2003 09:39:21 GMT\n"
                         "Link: http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp\n\n"
                         "[image 2]How do Americans get ready to work with Russians aboard the International Space Station? They take a crash course in culture, language and protocol at Russia\'s Star City[3].\n\n"
                         "Links:\n[1]: http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp (link)\n"
                         "[2]: https://example.com/images/logo.png (image)\n"
                         "[3]: http://howe.iki.rssi.ru/GCTC/gctc_e.htm (link)\n")

    def test_json(self):
        content = self.SAMPLE_2_0
        feed = rss_reader.parse_feed(content)
        rss_reader.limit_feed(feed, 1)
        json = rss_reader.format_json(feed)
        self.maxDiff = None
        self.assertEqual(json,
                         '{\n "title": "Liftoff News",\n "link": "http://liftoff.msfc.nasa.gov/",\n'
                         ' "description": "Liftoff to Space Exploration.",\n "items": [\n'
                         '  {\n   "title": "Star City",\n   "pubDate": "Tue, 03 Jun 2003 09:39:21 GMT",\n'
                         '   "link": "http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp",\n'
                         '   "description": "[image 2]How do Americans get ready to work with Russians aboard the International Space Station? They take a crash course in culture, language and protocol at Russia\'s Star City[3].",\n'
                         '   "links": [\n'
                         '    [\n     "http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp",\n     "link"\n    ],\n'
                         '    [\n     "https://example.com/images/logo.png",\n     "image"\n    ],\n'
                         '    [\n     "http://howe.iki.rssi.ru/GCTC/gctc_e.htm",\n     "link"\n    ]\n'
                         '   ]\n  }\n ]\n}')
