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




    def update_book(self, book_id, title=None, author=None, quantity=None):
