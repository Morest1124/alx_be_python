
class Book:
    def __init__(self, title, author)-> None:
        self.title = title
        self.author = author
        pass
class EBook(Book):
    def __init__(self, file_size) -> None:
        self.file_size  = file_size
        pass

    
class PrintBook(Book):
        def __init__(self,  page_count):
            self.page_count = page_count
        pass
    
class Library:
    def _add_book(self, Book, EBook, PrintBook) -> None:
        self.Book = Book
        self.EBook = EBook
        self.PrintBook = PrintBook
        pass
    def list_book(self):
        pass