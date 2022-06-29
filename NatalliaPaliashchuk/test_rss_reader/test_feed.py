import datetime
from dateutil.tz import tzutc

test_feed = {'feed_title': 'Feed title', 'feed_items': [
    {'item_title': 'Item title 1',
     'item_pub_date': datetime.datetime(2022, 6, 22, 12, 12, 12, tzinfo=tzutc()),
     'item_url': 'http://example.com/item_1.html',
                 'item_desc_text': '[1 Image comment]Item description 1[2 Link comment]',
                 'item_desc_links': [
                     {'link_pos': 1,
                      'link_url': 'http://example.com/files/item_1.jpg',
                      'link_type': 'image'},
         {'link_pos': 2,
                         'link_url': 'http://example.com/item_1.html',
                         'link_type': 'link'}],
     'item_image_url': 'http://example.com/item_1.jpg'}]}
