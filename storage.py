import json
import os

STORAGE_FILE = "books.json"

def load_books():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**book) for book in data]
    return []

def save_books(books):
    data = [
        {
            "title": book.title,
            "author": book.author,
            "pages": book.pages,
            "current_page": book.current_page
        }
        for book in books
    ]
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
