import math
class Pagination:

    def __init__(self, text="", symb=5):
        self.text = text
        if type(symb) == int and symb > 0:
            self.symb = symb
        else:
            raise TypeError("'Number of symbols' must be int and > 0")
        self.num_of_pages = self.page_count()
        self.pages = []

    def item_count(self):
        return len(self.text)


    def page_count(self):
        if len(self.text) % self.symb == 0:
            return int(len(self.text)/self.symb)
        else:
            return math.ceil(len(self.text) / self.symb)

    def count_items_on_page(self, num_of_page):
        if num_of_page >= self.num_of_pages or num_of_page < 0:
            raise IndexError("Invalid index. Page is missing.")
        elif num_of_page == self.num_of_pages - 1 and len(self.text) % self.symb != 0:
            return len(self.text) % self.symb
        else:
            return self.symb


    def display_page(self, num):
        if num >= self.num_of_pages or num < 0:
            raise IndexError("Invalid index. Page is missing.")
        else:
            self.pages = []
            index = 1
            s = self.text
            while index <= self.num_of_pages:
                s = s[0:self.symb]
                self.pages.append(s)
                s = self.text[index * self.symb:]
                index += 1
            return(self.pages[num])

    def find_page(self, text):
        arr = []
        for elem in self.pages:
            word = elem.replace(" ", "")
            if text in word:
                arr.append(self.pages.index(elem))
            else:
                if word in text:
                    arr.append(self.pages.index(elem))
        if len(arr) != 0:
            return(arr)
        else:
            raise Exception(f"'{text}' is missing on the pages")




pages = Pagination('Your beautiful text', 5)
print(pages.display_page(3))
print(pages.pages)
print(pages.find_page("great"))
