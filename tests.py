import unittest
from unittest.mock import patch
from rss_reader.rss_reader import *


class MyTest(unittest.TestCase):
    def test_is_xml(self):
        r = requests.get("https://news.yahoo.com/rss/")
        xml_content = r.content
        self.assertFalse(is_xml(xml_content))
        self.assertTrue(is_xml(xml_content))

    def test_is_xml_2(self):
        s = requests.get("https://mail.ru")
        c = s.content
        self.assertTrue(is_xml(c))
        self.assertFalse(is_xml(c))

    def test_get_content(self):
        r = requests.get("https://news.yahoo.com/rss/")
        xml_content = r.content
        root = etree.fromstring(xml_content)
        self.assertEqual(type(get_content("https://news.yahoo.com/rss/")), type(root[0]))

    @patch('rss_reader.get_content')
    def test_for_get_content(self, mock_is_xml):
        mock_is_xml.return_value = False
        with self.assertRaises(Exception):
            get_content("https://news.yahoo.com/rss/")
            mock_is_xml.assert_called_once()

    def test_link_handler(self):
        link_xml = "<link>https://news.yahoo.com/gop-commission-refuses-certify-mexico-004011875.html</link>"
        root = etree.fromstring(link_xml)
        link = "https://news.yahoo.com/gop-commission-refuses-certify-mexico-004011875.html"
        self.assertEqual(link_handler(None), "Link field doesn't provided!")
        self.assertEqual(link_handler(root), link)

    def test_description_handler(self):
        description = '<description><![CDATA[ <p><a ><img src="https://content.onliner.by/news/thumbnail/47cd48d89466d7ec81d09848ecb32fdc.jpeg" alt="" />' \
                      '</a></p><p>В <a href="https://mchs.gov.by/glavnoe/391537/" target="_blank">МЧС</a> рассказали об аварии, которая произошла 14 июня ' \
                      'около 17:30 на трассе М1 (Брест — Минск — граница России), вблизи деревни Рябиновка Дзержинского района. Mazda 626 столкнулась с микроавтобусом Mercedes Sprinter.' \
                      '</p><p><a href="https://auto.onliner.by/2022/06/15/mazda-stolknulas-s-mikroavtobusom">Читать далее…</a></p> ]]></description>'
        root = etree.fromstring(description)
        clear_descr = " В МЧС рассказали об аварии, которая произошла 14 июня около 17:30 на трассе М1 (Брест — Минск — граница России), " \
                      "вблизи деревни Рябиновка Дзержинского района. Mazda 626 столкнулась с микроавтобусом Mercedes Sprinter.Читать далее… "
        self.assertEqual(description_handler(root), clear_descr)
        self.assertEqual(description_handler(None), "There is no description!")
        description_2 = "<description>Graphic footage of the attack in China set off a heated debate that showed both " \
                        "the growing awareness of women’s rights and how divisive feminism still remains.</description>"
        clear_descr_2 = "Graphic footage of the attack in China set off a heated debate that showed both " \
                        "the growing awareness of women’s rights and how divisive feminism still remains."
        root_2 = etree.fromstring(description_2)
        self.assertEqual(description_handler(root_2), clear_descr_2)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)