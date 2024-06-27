# database.py
import sqlite3
from contextlib import closing

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def setup(self):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            self.connection.commit()

    def add_item(self, username, email, password):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("INSERT INTO employee (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            self.connection.commit()

    def get_item(self):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM employee")
            return cursor.fetchall()
