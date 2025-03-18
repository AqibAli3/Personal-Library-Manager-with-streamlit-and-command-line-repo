import json

# Initialize library
try:
    with open("library.txt", "r") as file:
        library = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    library = []

def save_library():
    """Save the library to a file."""
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)
    print("Library saved. Goodbye!")

def display_books(books=None):
    """Display books (all or filtered)."""
    books = books or library
    if not books:
        print("No books found!")
    for book in books:
        print(f"{book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}")

def add_book():
    """Add a new book."""
    library.append({
        "Title": input("Enter the book title: "),
        "Author": input("Enter the author: "),
        "Publication Year": int(input("Enter the publication year: ")),
        "Genre": input("Enter the genre: "),
        "Read Status": input("Have you read it? (yes/no): ").lower() == "yes"
    })
    print("Book added successfully!")

def remove_book():
    """Remove a book by title."""
    title = input("Enter the book title to remove: ").lower()
    global library
    library = [book for book in library if book['Title'].lower() != title]
    print("Book removed successfully!")

def search_book():
    """Search by title or author."""
    field = "Title" if input("Search by (1. Title, 2. Author): ") == "1" else "Author"
    term = input("Enter your search term: ").lower()
    matches = [book for book in library if term in book[field].lower()]
    display_books(matches)

def display_statistics():
    """Show library statistics."""
    total = len(library)
    read = sum(book['Read Status'] for book in library)
    print(f"Total books: {total}\nPercentage read: {read / total * 100:.2f}%" if total else "No books to analyze!")

def main():
    """Menu-driven library manager."""
    actions = {
        "1": add_book,
        "2": remove_book,
        "3": search_book,
        "4": lambda: display_books(),
        "5": display_statistics,
        "6": save_library
    }
    while True:
        print("\nWelcome to Personal Library Manager!")
        print("1. Add Book  2. Remove Book  3. Search  4. Display All  5. Stats  6. Exit")
        action = actions.get(input("Enter your choice: "), lambda: print("Invalid choice!"))
        if action == save_library:  # Exit case
            action()
            break
        action()

if __name__ == "__main__":
    main()
