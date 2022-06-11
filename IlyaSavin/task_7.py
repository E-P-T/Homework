#! /usr/bin/env python
# TODO: Implement a Pagination class helpful to arrange text on pages and list
# content on given page. The class should take in a text and a positive integer
# which indicate how many symbols will be allowed per each page (take spaces
# into account as well). You need to be able to get the amount of whole symbols
# in text, get a number of pages that came out and method that accepts the page
# number and return quantity of symbols on this page. If the provided number of
# the page is missing print the warning message "Invalid index. Page is
# missing". If you're familliar with using of Excpetions in Python display the
# error message in this way. Pages indexing starts with 0.
# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19
# Optional: implement searching/filtering pages by symblos/words and displaying
# pages with all the symbols on it. If you're querying by symbol that appears
# on many pages or if you are querying by the word that is splitted in two
# return an array of all the occurences.


"""
task_7.py: Implemented Pagination class helpful to arrange text on pages and
list content on given page and some test statements.
"""


class Pagination:
    """
    Pagination: class arrange text on pages and list content on given page.
    The class should take in a text and a positive integer which indicate how
    many symbols will be allowed per each page.
    """
    def __init__(self, text, page):
        self.icount = len(text)
        self.pcount = len(text) // page + 1
        self.pages = [text[i * page:(i + 1) * page] for i in range(self.pcount)]

    def count_items_on_page(self, index):
        if 0 <= index < len(self.pages):
            return len(self.pages[index])
        else:
            raise Exception('Invalid index. Page is missing.')

    def find_page(self, target):
        return [i for i, v in enumerate(self.pages)
                if (v.strip() in target or target in v.strip())]

    def display_page(self, index):
        if 0 <= index < len(self.pages):
            return repr(self.pages[index])
        else:
            raise Exception('Invalid index. Page is missing.')


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.pcount)  # Result: 4
    print(pages.icount)  # Result: 19
    print(pages.count_items_on_page(0))  # Result: 5
    print(pages.count_items_on_page(3))  # Result: 4
    # print(pages.count_items_on_page(4))  # Result: Exception: Invalid index. Page is missing.
    print(pages.find_page('Your'))  # Result: [0]
    print(pages.find_page('e'))  # Result: [1, 3]
    print(pages.find_page('beautiful'))  # Result: [1, 2]
    print(pages.find_page('great'))  # Result: []
    print(pages.display_page(0))  # Result: 'Your '
