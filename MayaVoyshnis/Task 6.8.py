import math


class Pagination:
    def __init__(self, text, volume):
        self.text = text
        self.volume = volume
        self._pages = self._separation()

    def _separation(self):
        lst = [self.text[i:i + self.volume] for i in range(0, len(self.text), self.volume)]
        dick = {x: lst[x] for x in range(self.page_count())}
        return dick

    def page_count(self):
        return math.ceil(len(self.text) / self.volume)

    def count_items_on_page(self, page):
        if page <= self.page_count():
            return len(self._pages[page])
        raise ValueError()

    def display_page(self, page):
        if page <= self.page_count():
            return self._pages[page]
        raise ValueError()


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count())
    print(pages.count_items_on_page(0))
    print(pages.display_page(0))
