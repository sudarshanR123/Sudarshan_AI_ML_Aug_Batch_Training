def add_book(catalog, book_id, title, author, year):
    # Store book details as a tuple
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    # Check if the book exists
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist.")
        return

    # Check if the book is already borrowed
    if book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
        return

    # Add the book ID to the borrowed books list
    borrowed_books.append(book_id)
    print(f"Book ID {book_id} borrowed successfully.")


def return_book(borrowed_books, book_id):
    # Check if the book is currently borrowed
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


def register_member(members, member_id):
    # Set automatically ignores duplicate values
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    # Display books that are not currently borrowed
    for book_id, book_details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = book_details
            print(
                f"ID: {book_id}, "
                f"Title: {title}, "
                f"Author: {author}, "
                f"Year: {year}"
            )


def main():
    # Dictionary for library catalog
    catalog = {}

    # List for currently borrowed books
    borrowed_books = []

    # Set for unique members
    members = set()

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2022)
    add_book(catalog, 102, "Data Science", "Alice Brown", 2023)
    add_book(catalog, 103, "Machine Learning", "David Lee", 2021)
    add_book(catalog, 104, "Web Development", "Robert King", 2024)

    # Register 3 members
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)

    # Try registering a duplicate member
    register_member(members, 1001)

    print("Registered Members:", sorted(members))

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("Borrowed Books:", borrowed_books)

    # Return 1 book
    return_book(borrowed_books, 101)

    print("Borrowed Books after return:", borrowed_books)

    # Display available books
    show_available(catalog, borrowed_books)


# Run the program
if __name__ == "__main__":
    main()