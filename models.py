class Book:
    def __init__(self, title, author, pages, current_page=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page

    def progress(self):
        if self.pages > 0:
            return (self.current_page / self.pages) * 100
        return 0
