"""
Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols
will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages
that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index.
Page is missing". If you're familliar with using of Excpetions in Python display the error
message in this way.
Pages indexing starts with 0.
"""

class Pagination:

    def __init__ (self, text, num):
        self.text = text
        self.num = num
        self.item_count = len(text)
        self.page_count = self.item_count // self.num if self.item_count % self.num == 0 else self.item_count // self.num +1

    def count_items_on_page(self, page_num):
        try:
            if page_num == self.page_count-1:
                s = len(self.text[self.num * page_num:])
            elif page_num < self.page_count-1:
                s = self.num
            else:
                raise ValueError
            return s
        except ValueError:
            return  "Invalid index. Page is missing"

    def display_page (self, page_num):
        try:
            if page_num == self.page_count-1:
                s = self.text[self.num * page_num:]
            elif page_num < self.page_count-1:
                s = self.text[self.num * page_num:self.num * (page_num+1)]
            else:
                raise ValueError
            return s
        except ValueError:
            return  "Invalid index. Page is missing"

    def find_page (self, my_str):
        try:
            # count apperiances of my_str in the text
            my_count = self.text.count(my_str)
            if my_count == 0:
                raise ValueError
            else:
                page_list = []
                ind = -1
                # iterate by my_count and memorize pages with my_str
                for i in range(my_count):
                    ind = self.text.find(my_str, ind+1)
                    if ind // self.num == (ind + len(my_str)) // self.num:
                        page_list.append(ind // self.num)
                    else: 
                        page_list.append(ind // self.num)
                        page_list.append((ind // self.num) + 1)
                return page_list
        except ValueError:
            return  "Exception: {} is missing on the pages".format(my_str)

pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)

print(pages.count_items_on_page(0))
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(4))

print(pages.display_page(0))
print(pages.display_page(1))
print(pages.display_page(4))

print(pages.find_page('Your'))
print(pages.find_page('e'))
print(pages.find_page('beautiful'))
print(pages.find_page('great'))