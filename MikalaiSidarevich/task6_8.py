# Task 6.8

# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.

# Example:
# ```python
# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19
# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# ```
# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

# Example:
# ```python
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
# ```

class Pagination:
    """Class helpful to arrange text on pages and list content on given page."""

    def __init__(self, data, page_size):
        """
        Initialize paginator with `data` and set `page_size`.
        """
        self._data = data
        self._data_size = len(data)
        self._page_size = page_size
        self._page_count = (self._data_size + page_size) // page_size
        self._paginate()    

    def _paginate(self):
        """
        Split source data into the storage.
        """
        self._pages = []

        for i in range(self._page_count):
            page = self._data[i*self._page_size:(i+1)*self._page_size]
            self._pages.append(page)

    @property
    def page_count(self):
        """Get page size."""
        return self._page_count

    @property
    def item_count(self):
        """Get total data size."""
        return self._data_size

    def count_items_on_page(self, page_number):
        """
        Get page size - all items quantity on the `page_number`.
        """
        try:
            items_count = len(self._pages[page_number])
        except IndexError as e:
            return f"Exception: Invalid index. Page is missing."
        else:
            return items_count

    def display_page(self, page_number):
        """
        Get `page_number` content.
        """
        try:
            page_content = self._pages[page_number]
        except IndexError as e:
            return f"Exception: Invalid index. Page is missing."
        else:
            return f"'{page_content}'"

    def find_page(self, token):
        """
        Get page numbers where `token` was found.
        """
        pages = []
        start_index = 0
        while start_index < self._data_size:
            # Look up through the data
            found_index = self._data.find(token, start_index)

            if found_index == -1:
                # Already found at least one
                if start_index:
                    return pages
                else:
                    # Token not found
                    raise Exception(f"'{token}' is missing on the pages")
            else:
                # End index of the token found
                last_index = found_index + len(token) - 1

                # New start index for search
                start_index = last_index + 1

                # Pages boundaries
                found_page = found_index // self._page_size
                last_page = last_index // self._page_size

                # Add found page into result list
                token_pages = []
                for p in range(found_page, last_page + 1):
                    token_pages.append(p)
                pages.extend(token_pages)


def main():
    """
    Entry point function.
    """
    pages = Pagination('Your beautiful text', 5)
    # pages = Pagination('Your e beautiful text text', 5)
    print(pages.page_count)
    print(pages.item_count)
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    print(pages.count_items_on_page(4))

    print(pages.find_page('Your'))
    print(pages.find_page('e'))
    print(pages.find_page('beautiful'))
    try:
        print(pages.find_page('great'))
    except Exception as e:
        print(f"Exception: {e}")
    print(pages.display_page(0))


if __name__ == '__main__':
    main()
