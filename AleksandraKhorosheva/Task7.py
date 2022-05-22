### Task 4.7

'''Implement a Pagination class helpful to arrange text on pages and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
(take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that
accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.
'''

import math


class Pagination():

    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.item_count = len(text)
        self.page_count = math.ceil(self.item_count / self.num)

    def get_items_count(self):
        return self.item_count

    def get_page_count(self):
        return self.page_count

    def text_on_page(self, page_num):
        return self.text[page_num * self.num:(page_num + 1) * self.num]

    def count_items_on_page(self, page_num):
        if 0 <= page_num <= self.num:
            return len(self.text_on_page(page_num))
        else:
            return "Invalid index.Page is missing"

    def find_symbols(self, symbol):
        return [i for i in range(self.page_count) if symbol in self.text_on_page(i)]


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
print(pages.count_items_on_page(9))
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(4))
print(pages.find_symbols("te"))
