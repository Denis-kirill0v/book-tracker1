from models import Book
from storage import load_books, save_books
from stats import calculate_total_pages, calculate_read_pages, average_progress

books = load_books()

def display_menu():
    print("\n=== Трекер прочитанных книг ===")
    print("1. Добавить книгу")
    print("2. Отметить прочитанные страницы")
    print("3. Показать статистику")
    print("4. Показать список книг")
    print("5. Выход")

def add_book():
    title = input("Название книги: ")
    author = input("Автор: ")
    pages = int(input("Всего страниц: "))
    book = Book(title, author, pages)
    books.append(book)
    save_books(books)
    print(f"Книга '{title}' добавлена!")

def update_progress():
    for i, book in enumerate(books):
        print(f"{i+1}. {book.title} - {book.current_page}/{book.pages}")
    choice = int(input("Выберите книгу: ")) - 1
    if 0 <= choice < len(books):
        pages = int(input("Сколько страниц прочитали сегодня? "))
        books[choice].current_page += pages
        save_books(books)
        print("Прогресс обновлён!")

def show_stats():
    total = calculate_total_pages(books)
    read = calculate_read_pages(books)
    avg_progress = average_progress(books)
    print(f"\nСтатистика:")
    print(f"Всего страниц во всех книгах: {total}")
    print(f"Прочитано страниц: {read}")
    print(f"Средний прогресс: {avg_progress:.1f}%")

def show_books():
    print("\nСписок книг:")
    for book in books:
        progress = book.progress()
        print(f"- {book.title} ({book.author}): {book.current_page}/{book.pages} ({progress:.1f}%)")

while True:
    display_menu()
    choice = input("Выберите действие: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_progress()
    elif choice == "3":
        show_stats()
    elif choice == "4":
        show_books()
    elif choice == "5":
        break
    else:
        print("Неверный выбор, попробуйте снова.")
