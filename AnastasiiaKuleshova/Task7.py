# Task 4.8
# Implement a Pagination class helpful to arrange text on pages and list
# content on given page. The class should take in a text and a positive integer
# which indicate how many symbols will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that
# came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index.
# Page is missing". If you're familliar with using of Excpetions in Python display the error
# message in this way. Pages indexing starts with 0.
#
# Example:
#
# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19
#
# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# Optional: implement searching/filtering pages by symblos/words and displaying
# pages with all the symbols on it. If you're querying by symbol that appears on many
# pages or if you are querying by the word that is splitted in two return an array of all the occurences.
#
# Example:
#
# >>> pages.find_page('Your')
# [0]
# >>> pages.find_page('e')
# [1, 3]
# >>> pages.find_page('beautiful')
# [1, 2]
# >>> pages.find_page('great')
# Exception: 'great' is missing on the pages
# >>> pages.display_page(0)
# 'Your '

class Pagination:
    _text_on_page = {}

    def __init__(self, text: str, number_of_symbols_on_page: int):

        if isinstance(number_of_symbols_on_page, int) and isinstance(text, str):
            self.number_of_symbols_on_page = number_of_symbols_on_page
            self.text = text
        else:
            raise Exception("wrong data type")

    def text_split_to_pages(self):

        _number_of_pages = 0
        for i in range(0, len(self.text), self.number_of_symbols_on_page):
            if i < len(self.text):
                _number_of_pages += 1
                self._text_on_page[_number_of_pages] = self.text[i:i + self.number_of_symbols_on_page]
            else:
                _number_of_pages += 1
                self._text_on_page[_number_of_pages] = self.text[i - 1:len(self.text) + 1]

    def page_count(self):
        self.text_split_to_pages()
        print(len(self._text_on_page))

    def item_count(self):
        print(len(self.text))

    def count_items_on_page(self, page_number):
        self.text_split_to_pages()
        try:
            if int(page_number) < len(self._text_on_page) and page_number > 0:
                print(len(self._text_on_page[page_number]))
            else:
                raise Exception("wrong page number")
        except ValueError:
            print("wrong number of pages")

    def find_page(self, line: str):
        self.text_split_to_pages()
        page_numbers_of_found_line = []
        try:
            for page in range(1, len(self._text_on_page) + 1):
                if line in self._text_on_page[page]:
                    page_numbers_of_found_line.append(page)
        except ValueError:
            print("wrong data")
        print(page_numbers_of_found_line)

    def display_page(self, page):
        self.text_split_to_pages()
        try:
            print(self._text_on_page[page])
        except (ValueError, KeyError):
            print("wrong page number")


a = Pagination("dsldk", 2)

a.page_count()
a.item_count()
a.count_items_on_page(2)
a.page_count()
a.count_items_on_page(2)
a.find_page('k')
a.display_page(3)
