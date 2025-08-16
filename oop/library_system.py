class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size) -> None:
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count) -> None:
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")
            if isinstance(book, EBook):
                print(f"File Size: {book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"Page Count: {book.page_count}")
            print()
