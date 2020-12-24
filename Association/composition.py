class Book:
    def __init__(self):
        page1 = Page('This is content for page 1')
        page2 = Page('This is content for page 2')
        self.pages = [page1, page2]

    def print_pages(self):
        print(self.pages)
        for page in self.pages:
            print(page.content)


class Page:
    def __init__(self, content):
        self.content = content


book = Book()  # If I destroy this Book instance,
# the Page instances are also destroyed
book.print_pages()
