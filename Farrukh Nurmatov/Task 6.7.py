"""Implement a Pagination class helpful to arrange text on pages and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols will be
allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out
and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index.
Page is missing". If you're familiar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0."""


class Pagination:
    def __init__(self, text, symbol_num):
        self.text = text
        self.symbol_num = symbol_num
        self.pages = [text[x:x+5] for x in range(0, len(text), 5)]

    def page_count(self):
        return len(self.pages)

    def item_count(self):
        return len(self.text)

    def count_items_on_page(self, page_num):
        try:
            return len(self.pages[page_num])
        except IndexError:
            return "Exception: Invalid index. Page is missing."

    def searching(self, symbol):
        searched = [page for page in self.pages if symbol in page]
        return searched

    def display_page(self, num):
        try:
            return self.pages[num]
        except IndexError:
            return "Exception: Invalid index. Page is missing."


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count())
    print(pages.item_count())
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    print(pages.count_items_on_page(4))
    print(pages.searching("a"))
    print(pages.display_page(0))
