def calculate_total_pages(books):
    return sum(book.pages for book in books)

def calculate_read_pages(books):
    return sum(book.current_page for book in books)

def average_progress(books):
    if not books:
        return 0
    total_progress = sum(book.progress() for book in books)
    return total_progress / len(books)
