import sqlite3

class BookInventoryManager:
    def __init__(self, database_name="book_inventory.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.initialize_database()

    def initialize_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                quantity INTEGER
            )
        ''')
        self.connection.commit()

    def add_book(self, title, author, quantity):
        query = "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)"
        self.cursor.execute(query, (title, author, quantity))
        self.connection.commit()

    def update_book(self, book_id, title=None, author=None, quantity=None):
        update_query = "UPDATE books SET "
        update_params = []

        if title:
            update_query += "title = ?, "
            update_params.append(title)
        if author:
            update_query += "author = ?, "
            update_params.append(author)
        if quantity is not None:
            update_query += "quantity = ?, "
            update_params.append(quantity)

        update_query = update_query.rstrip(", ")
        update_query += " WHERE id = ?"
        update_params.append(book_id)

        self.cursor.execute(update_query, update_params)
        self.connection.commit()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.connection.commit()

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if not books:
            print("No books in the inventory.")
        else:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

    def search_book(self, keyword):
        query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?"
        self.cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        found_books = self.cursor.fetchall()

        if not found_books:
            print(f"No books found containing '{keyword}'.")
        else:
            for book in found_books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

    def close_connection(self):
        self.connection.close()

def run_book_inventory_manager():
    book_manager = BookInventoryManager()

    book_manager.add_book("The Martian", "Andy Weir", 8)
    book_manager.add_book("Dune", "Frank Herbert", 12)

    print("\n-- All Books --")
    book_manager.view_books()

    try:
        book_manager.update_book(1, quantity=10)
        book_manager.delete_book(2)

        print("\n-- Updated Books --")
        book_manager.view_books()

        search_keyword = input("\nEnter a keyword to search: ")
        book_manager.search_book(search_keyword)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        book_manager.close_connection()

if __name__ == "__main__":
    run_book_inventory_manager()
