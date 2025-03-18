##Personal Library Manager
Description
The Personal Library Manager is a Python-based command-line application designed to help users manage their book collection. Users can add, remove, search, and display books, as well as view statistics about their library. Additionally, the library is saved to a JSON file for persistence between program runs.

Features
Add a Book: Add a new book to the library by entering details like title, author, publication year, genre, and read status.

Remove a Book: Remove a book from the library using its title.

Search for a Book: Search for books by either title or author.

Display All Books: View all books in the library with their details.

Library Statistics: Get insights about the total number of books and the percentage of books that have been read.

File Handling: Automatically saves the library to library.txt on exit and loads it on startup.

How to Use
Clone or download this project.

Make sure Python 3.x is installed on your machine.

Save the provided Python script as library_manager.py in a folder.

Create a file named library.txt in the same folder (optional; the program will create it if it doesn’t exist).

Run the program using the following command:

bash
python library_manager.py
Follow the on-screen menu to interact with your library.

Menu Options
1. Add Book: Prompts the user to input book details.

2. Remove Book: Asks for the title of the book to be removed.

3. Search: Enables searching by title or author.

4. Display All Books: Lists all books in the library.

5. Stats: Displays the total count of books and read percentage.

6. Exit: Saves the library and exits the program.

File Structure
library_manager.py: Main program file.

library.txt: JSON file where library data is saved.

Example Interaction
Adding a Book
Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read it? (yes/no): yes
Book added successfully!
Displaying All Books
The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
Statistics
Total books: 1
Percentage read: 100.00%
Dependencies
No additional Python libraries are required. This project uses only Python's built-in json module.