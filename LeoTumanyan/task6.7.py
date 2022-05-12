# ### Task 6.7

# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
# (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that
# accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're
# familiar with using of Exceptions in Python display the error message in this way.
# Pages indexing starts with 0.

# Example:

# ```python
# >>> pages = Pagination('Your beautiful text', 5)
# >>> TODO: pages.page_count
# 4
# >>> TODO: pages.item_count
# 19

# >>> TODO: pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# ```
import math


class Pagination:
    def __init__(self, text: str, s_per_page: int = 10):
        self.text = text
        self.s_per_page = s_per_page
        if not isinstance(s_per_page, int) and not isinstance(text, str):
            raise TypeError
        self.pages = self.wrap(self.text, self.s_per_page)

    @staticmethod
    def wrap(s, w):
        return [s[i:i + w] for i in range(0, len(s), w)]

    def page_count(self):
        print(math.ceil(len(self.text) / self.s_per_page))

    def item_count(self):
        print(len(self.text))

    def count_items_on_page(self, page_no):
        try:
            print(len(self.pages[page_no]))
        except IndexError:
            print("Exception: Invalid index. Page is missing.")
        except TypeError:
            print("TypeError: Wrong argument")


pages = Pagination('Your beautiful text', 5)
pages.page_count()
pages.item_count()
pages.count_items_on_page("k")
