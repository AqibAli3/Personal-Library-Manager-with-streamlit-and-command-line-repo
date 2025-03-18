## Personal Library Manager
Overview
The Personal Library Manager repository contains two versions of an app designed to help users organize and manage their book collections. Each version offers a unique approach, catering to different needs and preferences:

Command-Line Version: A lightweight and beginner-friendly command-line interface (CLI) app for managing books.

Streamlit-Based Version: An interactive and visually appealing web app built using Streamlit for a richer user experience.

Repository Structure
This repository is divided into two folders:

commandline_version/:

Contains the Python CLI implementation.

Provides all essential features for managing a personal library through the terminal.

streamlit_version/:

Contains the fully-featured Streamlit web application.

Integrates with the Google Books API for online book searches and offers enhanced functionality with a modern UI.

Features Comparison
Feature	Command-Line Version	Streamlit Version
Add Books	✅ Add book details via terminal input.	✅ Add books using a user-friendly form.
Remove Books	✅ Remove books by entering their title.	✅ Remove books with a dropdown list.
Search for Books	✅ Search by title or author.	✅ Search library and Google Books API.
Display All Books	✅ View all books in plain text.	✅ View a formatted list and download it.
Statistics	✅ View total and read percentage.	✅ View enhanced statistics visually.
File Storage	✅ Library saved in JSON (library.txt).	✅ Library saved in JSON (library.json) and plain text.
User Interface	❌ Text-based (command-line).	✅ Interactive web interface (Streamlit).
How to Use
Command-Line Version
Navigate to the commandline_version/ folder:

bash
cd commandline_version
Run the program:

bash
python library_manager.py
Use the on-screen menu to manage your library.

Streamlit Version
Navigate to the streamlit_version/ folder:

bash
cd streamlit_version
Install dependencies (if not already installed):

bash
pip install streamlit requests
Run the Streamlit app:

bash
streamlit run library_manager.py
Use the sidebar menu to interact with the app and manage your library.

Prerequisites
Python 3.x is required to run both versions of the app.

Install additional dependencies for the Streamlit version:

bash
pip install -r requirements.txt
(The requirements.txt file is located in the streamlit_version folder.)

Google Books API (Streamlit Version Only)
The Streamlit version integrates with the Google Books API to provide online book search functionality. Make sure to add your API key in the search_books_google function in library_manager.py:

python
api_key = "your-google-books-api-key"
Contributions
If you'd like to contribute:

Fork the repository.

Make your changes.

Submit a pull request with a detailed description of the update.
