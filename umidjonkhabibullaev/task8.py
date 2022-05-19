class Pagination:
    def __init__(self, text, items_per_page):
        self.text = text
        self.items_per_page = items_per_page

        ### Split the page ###
        self.pages = self.split_text_to_pages()
        self.item_count = len(self.pages)
        self.page_count = len(self.pages)
    
    def split_text_to_pages(self):
        pages = []
        for i in range(0, len(self.text), self.items_per_page):
            page = self.text[i:i+self.items_per_page]
            pages.append(page)
        return pages
    
    def count_items_on_page(self, page_index):
        try:
            return len(self.pages[page_index])
        except IndexError as e:
            return e
    
    def display_page(self, page_index):
        try:
            return self.pages[page_index]
        except IndexError as e:
            return e

    def find_page(self, content):
        searching_pages = []
        for page_number in range(self.page_count):
            if content in self.display_page(page_number):
                searching_pages.append(page_number)
                break
            elif self.display_page(page_number) in content:
                searching_pages.append(page_number)
                content = content.replace(self.display_page(page_number), "")
        
        if searching_pages:
            return searching_pages

        return f"Exception: '{content}' is missing on the pages"

                
if __name__ == "__main__":
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count)
    print(pages.count_items_on_page(4))
    print(pages.display_page(2))
    print(pages.find_page("Your beauti"))
    print(pages.pages)