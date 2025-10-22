import sys

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = {}

    def __str__(self):
        borrowed_books = ', '.join(f"'{book}'" for book in self.borrowed.values()) or "None"
        return f"{self.name}, Borrowed: {borrowed_books}"

class Library:
    def __init__(self):
        self.books = {}  # Book ID -> Book object
        self.books_by_title = {}  # Title -> Book object
        self.members = {}  # Member name -> Member object
        self.next_book_id = 1

    def add_book(self, title, author):
        book = Book(title, author)
        self.books[self.next_book_id] = book
        self.books_by_title[title.lower()] = book  # Store title in lowercase for case-insensitive lookup
        print(f"Added book: '{title}' by {author}.")
        self.next_book_id += 1

    def register_member(self, name):
        if name in self.members:
            print(f"Member '{name}' is already registered.")
            return
        self.members[name] = Member(name)
        print(f"Member '{name}' registered.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the Library:")
        for id_, book in self.books.items():
            print(f"[{id_}] {book}")

    def list_members(self):
        if not self.members:
            print("No members registered.")
            return
        print("Library Members:")
        for m in self.members.values():
            print(m)

    def issue_book(self, member_name, book_id_or_title):
        member = self.members.get(member_name)
        if not member:
            print("Member not found.")
            return

        book = self.books.get(book_id_or_title) if isinstance(book_id_or_title, int) else self.books_by_title.get(book_id_or_title.lower())
        if not book:
            print("Book not found.")
            return

        if book.is_issued:
            print("Book already issued.")
            return

        if book.title in member.borrowed:
            print(f"'{member_name}' has already borrowed '{book.title}'.")
            return

        book.is_issued = True
        member.borrowed[book_id_or_title] = book.title
        print(f"Issued '{book.title}' to '{member_name}'.")

    def return_book(self, member_name, book_id_or_title):
        member = self.members.get(member_name)
        if not member:
            print("Member not found.")
            return

        book = self.books.get(book_id_or_title) if isinstance(book_id_or_title, int) else self.books_by_title.get(book_id_or_title.lower())
        if not book:
            print("Book not found.")
            return

        if book.title not in member.borrowed.values():
            print(f"'{member_name}' did not borrow '{book.title}'.")
            return

        book.is_issued = False
        # Remove the book from the borrowed dictionary
        for key, title in member.borrowed.items():
            if title == book.title:
                del member.borrowed[key]
                break

        print(f"Returned '{book.title}' from '{member_name}'.")

def main():
    lib = Library()
    while True:
        print("\n1:Add Book 2:Register Member 3:List Books 4:List Members")
        print("5:Issue 6:Return 7:Exit")
        choice = input("> ").strip()
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(title, author)
        elif choice == "2":
            name = input("Member Name: ")
            lib.register_member(name)
        elif choice == "3":
            lib.list_books()
        elif choice == "4":
            lib.list_members()
        elif choice == "5":
            name = input("Member Name: ")
            bid_or_title = input("Book ID or Title: ").strip()
            # Try to convert to integer (if it's a book ID)
            try:
                bid_or_title = int(bid_or_title)
            except ValueError:
                pass
            lib.issue_book(name, bid_or_title)
        elif choice == "6":
            name = input("Member Name: ")
            bid_or_title = input("Book ID or Title: ").strip()
            # Try to convert to integer (if it's a book ID)
            try:
                bid_or_title = int(bid_or_title)
            except ValueError:
                pass
            lib.return_book(name, bid_or_title)
        elif choice == "7":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
