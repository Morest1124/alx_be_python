
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def get_is_checked_out(self):
        return self._is_checked_out

    def set_is_checked_out(self, value):
        self._is_checked_out = value
    
    def return_book(self):
        return self.return_book 
    
    def set_is_list_available_books(self, value):
        self.list_available_books = value



class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book._is_checked_out:
                book._is_checked_out = True
                print(f"You have checked out '{title}'.")
                return
            elif book.title.lower() == title.lower() and book._is_checked_out:
                print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in library.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book._is_checked_out:
                book._is_checked_out = False
                print(f"You have returned '{title}'.")
                return
            elif book.title.lower() == title.lower() and not book._is_checked_out:
                print(f"'{title}' is already available in library.")
                return
        print(f"'{title}' not found in library.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

