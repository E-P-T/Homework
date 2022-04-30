import math


class Pagination:
    def __init__(self, text, symbolsCount):
        self.text = text
        self.symbolsCount = symbolsCount
        self.itemCount = len(text)
        self.pageCount = math.ceil(len(text) / symbolsCount)

    def countItemsOnPage(self, pageNumber):
        if pageNumber + 1 > self.pageCount:
            print("Invalid index. Page is missing")
        else:
            currentPageIndex = self.symbolsCount * pageNumber
            nextPageIndex = self.symbolsCount * (pageNumber + 1)
            return len(self.text[currentPageIndex:nextPageIndex])

    # Optional hatvacy taski

    def findPage(self, word):
        p = set()
        found = True
        startIndex = 0

        while found:
            a = self.text.find(word, startIndex)
            if a != -1:
                p.add(a // self.symbolsCount)
                p.add((a + len(word)) // self.symbolsCount)
                startIndex = a + 1
            else:
                found = False

        if len(p) > 0:
            return p
        else:
            print("'{0}' is missing on the pages".format(word))

    def displayPage(self, pageNum):
        return self.text[pageNum * self.symbolsCount:(pageNum + 1) * self.symbolsCount]


pages = Pagination('Saminaxadasutyune', 5)

print(pages.findPage("Sa"))
