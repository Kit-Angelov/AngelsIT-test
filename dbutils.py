import sqlite3
from config import *


class SqliteDB:

    def __init__(self):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table_messages(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS messages(
                                                                        message_id INTEGER PRIMARY KEY,
                                                                        text TEXT
                                                                        )""")

    def add_message(self, message):
        with self.connection:
            self.cursor.execute("""INSERT INTO messages (text) VALUES('%s')""" % message)

    def get_messages(self):
        with self.connection:
            self.cursor.execute("""SELECT text FROM messages""")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()