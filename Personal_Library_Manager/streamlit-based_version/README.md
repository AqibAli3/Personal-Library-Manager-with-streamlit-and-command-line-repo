Deployed at: ([https://smart-unit-converter-by-aqib-ali.streamlit.app/])

# Personal Library Manager (Streamlit App)
Overview
The Personal Library Manager is an interactive Streamlit web app designed to help users manage their personal book collections effortlessly. This application allows you to add, remove, search, and display books from your library. It integrates with the Google Books API to search for books online and provides advanced features like downloads and customizable CSS styling for an enhanced user experience.

Features
Add a Book: Add a new book to your personal library by entering its details such as title, author, year, genre, and read status.

Remove a Book: Easily delete a book from the collection by selecting it from the list.

Search for Books:

By Title or Author: Search for books in your library based on title or author.

Online Search: Look up books using the Google Books API and retrieve additional information such as cover images, authors, and publication years.

Display All Books: View all books in your library in a formatted and downloadable list.

Display Statistics: Get an overview of your library, including the total number of books and the percentage of books read.

Contact and Links: Access links to contact the developer or visit their GitHub/LinkedIn profiles.

Custom Styling: Features a visually appealing interface with enhanced custom CSS.

How to Use
Setup Instructions
Clone the Repository:

bash
git clone https://github.comAqibAli3/Personal-Library-Manager-with-streamlit-and-command-line-repo.git
cd personal-library-manager
Install Dependencies:

bash
pip install streamlit requests
Run the Application:

bash
streamlit run library_manager.py
Using the App:

Choose options from the left-hand sidebar to interact with your library.

Follow on-screen prompts for adding, removing, searching, or displaying books.

File Structure
library_manager.py: Main Python script that runs the Streamlit app.

library.json: Primary JSON file for storing library data (created automatically if missing).

library.txt: Secondary, human-readable file for library data (created automatically).

Features in Detail
Add a Book
Enter book details:

Title

Author

Publication Year

Genre

Read Status (Yes/No)

Click "Add Book" to save the book to your library.

Remove a Book
Select a book from the dropdown list.

Click "Remove Book" to delete the selected book.

Search for Books
In Library: Search by title or author to view matching results.

Online Search: Enter a query to fetch books using the Google Books API, displaying titles, authors, covers, and publication years.

Display All Books
View your entire collection with book details displayed in a formatted list.

Option to download your entire book list as a plain text file.

Display Statistics
View metrics such as the total number of books and the percentage of books you’ve marked as read.

Customizable Features
Beautiful custom CSS for styling.

Download and upload features for library data (to be added in future updates).

Example Screenshots
Add a Book:

Title: The Hobbit
Author: J.R.R. Tolkien
Year: 1937
Genre: Fantasy
Read: Yes
Search Results:

Matching Books:
- The Hobbit by J.R.R. Tolkien (1937) - Fantasy - Read
Library Statistics:

Total Books: 10
Percentage Read: 70.00%
API Usage
The app integrates with the Google Books API for online book searches:

API Endpoint: https://www.googleapis.com/books/v1/volumes

Note: Replace the placeholder API key in the search_books_google function with your own from Google Cloud Console.

Dependencies
Python 3.x

Streamlit: For building the web app interface.

Requests: For making HTTP requests to the Google Books API.

Future Improvements
Add functionality for uploading books from external sources.

Enable editing of existing book details.

Enhance the statistics section with additional metrics.

Improve the UI to be mobile-friendly.

Include bookmarking or tagging options for books.

Provide the option to upload/download entire libraries as .json or .csv files.
