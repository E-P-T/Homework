# Task 6.8
# Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each
# page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method
# that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.
#
# Example:
# ```python
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
# ```
# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted
# in two return an array of all the occurences.
#
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