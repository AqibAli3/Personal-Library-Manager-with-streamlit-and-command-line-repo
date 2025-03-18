import streamlit as st
import requests
import json
import os  

# Page configuration
st.set_page_config(
    page_title="Personal Library Manager by Aqib Ali",  
    page_icon="📚",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# Initialize library as a list of dictionaries
library = []

# Load library from files (library.json or library.txt)
def load_library_from_file():
    global library
    try:
        # First attempt to load from library.json
        with open("library.json", "r") as json_file:
            library.extend(json.load(json_file))
    except FileNotFoundError:
        # If JSON file doesn't exist, attempt to load from library.txt
        if os.path.exists("library.txt"):
            with open("library.txt", "r") as txt_file:
                for line in txt_file:
                    # Parse each line to convert it into a dictionary
                    parts = line.strip().split(", ")
                    book = {
                        "Title": parts[0].split(": ")[1],
                        "Author": parts[1].split(": ")[1],
                        "Year": int(parts[2].split(": ")[1]),
                        "Genre": parts[3].split(": ")[1],
                        "Read": parts[4].split(": ")[1] == "True"
                    }
                    library.append(book)
    except Exception as e:
        st.error(f"Error loading library: {e}")

# Save library to both library.json and library.txt
def save_library_to_file():
    try:
        # Save to library.json
        with open("library.json", "w") as json_file:
            json.dump(library, json_file)
        # Save to library.txt
        with open("library.txt", "w") as txt_file:
            for book in library:
                txt_file.write(
                    f"Title: {book['Title']}, Author: {book['Author']}, "
                    f"Year: {book['Year']}, Genre: {book['Genre']}, Read: {book['Read']}\n"
                )
    except Exception as e:
        st.error(f"Error saving library: {e}")

# Search books using Google Books API
def search_books_google(query):
    api_key = "AIzaSyBSX9sO--XWL7n1-7rtJUQwCcifBC3OpOM"  
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        st.error("Double click please.")
        return []

# Load custom CSS
def load_custom_css():
    custom_css = """
   <style>
    /* General Background */
    body {
        background: linear-gradient(135deg, #f0f5f9, #c9dff0);
        font-family: 'Arial', sans-serif;
    }

    /* App Title */
    h1 {
        color: #1c3f60;
        text-shadow: 2px 2px 6px #a0a0a0;
        font-size: 2.5rem;
    }

    /* Subheader Styling */
    h2, h3 {
        color: #4a4a4a;
        border-bottom: 2px solid #007acc;
        padding-bottom: 5px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: #4a90e2;
        color: #ffffff;
        padding: 15px;
        border-right: 3px solid #003d66;
    }
    section[data-testid="stSidebar"] .css-1d391kg {
        color: #ffffff !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #007acc;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
        transition: 0.3s all;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    div.stButton > button:hover {
        background-color: #28a745; /* Updated hover color to green */
        transform: scale(1.05);
    }

    /* Footer */
    footer {
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #4a4a4a;
        border-top: 2px solid #d3d3d3;
        margin-top: 20px;
    }
</style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
# Streamlit app starts here
def main():
    st.title("📚 Personal Library Manager")  

    # Load library on startup
    load_library_from_file()

# Contact details footer
def display_footer():
    st.markdown(
        """
        <footer>
        Built with ❤ by Syed Aqib Ali | 
        <a href="https://github.com/" target="_blank" style="color: #007acc;">GitHub</a> | 
        <a href="https://linkedin.com/" target="_blank" style="color: #007acc;">LinkedIn</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Streamlit app starts here
def main():
    load_custom_css()  
    st.title("📚 Personal Library Manager")  

    # Load library on startup
    load_library_from_file()

    # Sidebar menu options
    menu = [
        "Add a Book",
        "Remove a Book",
        "Search for a Book",
        "Search Online Books",
        "Display All Books",
        "Display Statistics",
        "Download Books (coming soon)",
        "Upload Books (coming soon)",
        "Contact Me",
    ]
    choice = st.sidebar.selectbox("Menu", menu)

    # Add a book
    if choice == "Add a Book":
        st.subheader("Add a New Book")
        title = st.text_input("Enter the book title:")
        author = st.text_input("Enter the author:")
        year = st.number_input("Enter the publication year:", min_value=0, step=1)
        genre = st.text_input("Enter the genre:")
        read_status = st.radio("Have you read this book?", ("Yes", "No"))
        if st.button("Add Book"):
            read = True if read_status == "Yes" else False
            book = {"Title": title, "Author": author, "Year": int(year), "Genre": genre, "Read": read}
            library.append(book)
            st.success(f"Book '{title}' added successfully!")
            save_library_to_file()
        display_footer()

    # Remove a book
    elif choice == "Remove a Book":
        st.subheader("Remove a Book")
        titles = [book["Title"] for book in library]
        book_to_remove = st.selectbox("Select the book to remove:", titles)
        if st.button("Remove Book"):
            library[:] = [book for book in library if book["Title"] != book_to_remove]
            st.success(f"'{book_to_remove}' removed successfully!")
            save_library_to_file()
        display_footer()

    # Search for a book
    elif choice == "Search for a Book":
        st.subheader("Search for a Book")
        search_by = st.radio("Search by:", ("Title", "Author"))
        query = st.text_input("Enter your search query:")
        if st.button("Search"):
            results = [book for book in library if query.lower() in book[search_by].lower()]
            if results:
                st.write("### Matching Books:")
                for book in results:
                    st.write(f"- **{book['Title']}** by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            else:
                st.warning("No matching books found.")
        display_footer()

    # Search online books
    elif choice == "Search Online Books":
        st.subheader("Search Online Books")
        query = st.text_input("Enter a book title or author:")
        if st.button("Search Online"):
            results = search_books_google(query)
            if results:
                st.write("### Online Search Results:")
                for book in results[:10]:  
                    volume_info = book.get("volumeInfo", {})
                    title = volume_info.get("title", "N/A")
                    authors = ", ".join(volume_info.get("authors", ["Unknown"]))
                    year = volume_info.get("publishedDate", "Unknown")
                    cover_url = volume_info.get("imageLinks", {}).get("thumbnail")
                    info_link = volume_info.get("infoLink", "#")
                    if cover_url:
                        st.image(cover_url, width=150)
                    st.write(f"**{title}** by {authors} ({year})")
                    st.write(f"[More Details]({info_link})")
                    st.write("---")
            else:
                st.warning("No results found.")
        display_footer()

    # Display all books
    elif choice == "Display All Books":
        st.subheader("Your Library")
        if library:
            for idx, book in enumerate(library, 1):
                st.write(f"{idx}. **{book['Title']}** by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
            # Add the download button for all books here
            library_data = "\n\n".join(
                [
                    f"Title: {book['Title']}\nAuthor: {book['Author']}\nYear: {book['Year']}\n"
                    f"Genre: {book['Genre']}\nRead: {'Yes' if book['Read'] else 'No'}"
                    for book in library
                ]
            )
            st.download_button(
                label="📥 Download All Books Info",
                data=library_data,
                file_name="library_books.txt",
                mime="text/plain"
            )
        else:
            st.info("Your library is empty.")
        display_footer()

       # Display statistics
    elif choice == "Display Statistics":
        st.subheader("Library Statistics")
        total_books = len(library)
        read_books = len([book for book in library if book["Read"]])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        st.write(f"Total books: **{total_books}**")
        st.write(f"Books read: **{read_books}**")
        st.write(f"Percentage read: **{percentage_read:.2f}%**")
        display_footer()

    # Contact details page
    elif choice == "Contact Me":
        st.subheader("Contact Details")
        st.markdown(
            """
            ---
            <div class="contact-details" style="text-align: center; margin-top: 20px;">
                <p><b>Feel free to reach out!</b></p>
                <a href="https://www.linkedin.com/in/syed-aqib-ali/" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width: 40px; height: 40px; margin: 5px;">
                </a>
                <a href="https://github.com/AqibAli3" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width: 40px; height: 40px; margin: 5px;">
                </a>
                <a href="https://wa.me/+923158796106" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" style="width: 40px; height: 40px; margin: 5px;">
                </a>
                <a href="mailto:shaali254@gmail.com">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Mail_%28iOS%29.svg" alt="Email" style="width: 40px; height: 40px; margin: 5px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    save_library_to_file()

if __name__ == "__main__":
    main()
