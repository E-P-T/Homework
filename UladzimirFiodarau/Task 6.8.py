# Task 6.8
# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
# (take spaces into account as well). You need to be able to get the amount of whole symbols in text, get a number of
# pages that came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way. Pages indexing starts
# with 0.
# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in
# two return an array of all the occurences.

class Pagination(object):

    def __init__(self, text: str, split: int):
        self._text = text
        self._split = split
        self._pages = Pagination.pagify(text, split)

    @staticmethod
    def pagify(text: str, split: int):
        result = []
        while text:
            result.append(text[:split])
            text = text[split:]
        return result

    def page_count(self):
        return len(self._pages)

    def item_count(self):
        return len(self._text)

    def count_items_on_page(self, index: int):
        try:
            return len(self._pages[index])
        except IndexError:
            return "Exception: Invalid index. Page is missing."

    def find_page(self, seq: str):
        result = []
        i = 0
        while True:
            try:
                search_index = self._text.index(seq, i)
                if (search_index + len(seq) - 1) // self._split == search_index // self._split:
                    result.append(search_index // self._split)
                else:
                    result.extend(range(search_index//self._split, (search_index + len(seq)) // self._split + 1))
                i = search_index + len(seq)
            except ValueError:
                if result:
                    return result
                else:
                    return f"Exception: '{seq}' is missing on the pages"

    def display_page(self, index):
        return self._pages[index]

pages = Pagination('Your beautiful text', 5)
print(pages.page_count())
# 4
print(pages.item_count())
# 19
print(pages.count_items_on_page(0))
# 5
print(pages.count_items_on_page(3))
# 4
print(pages.count_items_on_page(4))
# Exception: Invalid index. Page is missing.

print(pages.find_page('Your'))
# [0]
print(pages.find_page('e'))
# [1, 3]
print(pages.find_page('beautiful'))
# [1, 2]
print(pages.find_page('great'))
# Exception: 'great' is missing on the pages
print(pages.display_page(0))
# 'Your '
