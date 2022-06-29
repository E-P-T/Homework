import unittest
from rss_reader.converting import feed_to_html, feed_to_json
from .test_feed import test_feed


class TestConverting(unittest.TestCase):
    def test_feed_to_html(self, *args):
        self.maxDiff = None
        html = feed_to_html(test_feed)
        self.assertEqual(html, '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Feed title</title>
</head>
<body>
    <h3>Feed title</h3>
        <p>
        Title: Item title 1<br>
        Date: 2022-06-22 12:12:12+00:00<br>
        Link: <a href="http://example.com/item_1.html">http://example.com/item_1.html</a><br><br>
            <img src="http://example.com/item_1.jpg" style="max-width:150px;width:100%;border:0"><br>
        [1 Image comment]Item description 1[2 Link comment]<br>
            [1]: <a href="http://example.com/files/item_1.jpg">image</a><br>
            [2]: <a href="http://example.com/item_1.html">link</a><br>
        </p>
</body>
</html>''')

    def test_feed_to_json(self, *args):
        json_ = feed_to_json(test_feed)
        self.assertEqual(json_, '''{"feed_title": \
"Feed title", "feed_items": [{"item_title": "Item title 1", \
"item_pub_date": "2022-06-22 12:12:12+00:00", "item_url": \
"http://example.com/item_1.html", "item_desc_text": \
"[1 Image comment]Item description 1[2 Link comment]", "item_desc_links": \
[{"link_pos": 1, "link_url": "http://example.com/files/item_1.jpg", "link_type": \
"image"}, {"link_pos": 2, "link_url": "http://example.com/item_1.html", "link_type": \
"link"}], "item_image_url": "http://example.com/item_1.jpg"}]}''')


if __name__ == '__main__':
    unittest.main()
