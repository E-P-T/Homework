from io import StringIO
from html.parser import HTMLParser

# html parser for clean data


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()

# cleaning tag and return clean data


def clean_desc(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


"""Testing html parse"""
# print(strip_tags("""<p><a href="https://auto.onliner.by/2022/06/06/na-dorestajlovyj-bmw-g11-postavili-22-dyujmovye-diski-kak-vam"><img src="https://content.onliner.by/news/thumbnail/c88eeb7d3c60993f7498f924ca86952d.jpeg" alt="" /></a></p><p>Сейчас внимание автомобильной общественности приковано к BMW 7-Series нового поколения. Но на рынке по-прежнему находится предшественник в старом кузове. Тюнинг-ателье тоже все еще не стесняются дорабатывать G11. Даже дорестайл. </p><p><a href="https://auto.onliner.by/2022/06/06/na-dorestajlovyj-bmw-g11-postavili-22-dyujmovye-diski-kak-vam">Читать далее…</a></p>"""))
