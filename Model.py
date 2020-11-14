import sqlite3
import logging
from dataclasses import dataclass

@dataclass
class TableItem:
    id: int
    title: str
    importance: int
    urgency: int
    detail: str
    memo: str

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY, title TEXT NOT NULL UNIQUE, importance INTEGER DEFAULT 2, urgency INTEGER DEFAULT 2, detail TEXT, memo TEXT);")

    def fetch(self, query):
        rows = self.cur.execute(query).fetchall()
        return rows

    def fetch_all(self):
        rows = self.cur.execute("SELECT * FROM tasks;").fetchall()
        return rows

    def insert(self, item):
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?, ?)", (item.title, item.importance, item.urgency, item.detail, item.memo))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        logging.info("Database closed successfully.")

if __name__ == '__main__':
    db = Database("database.db")
    db.insert(TableItem(0, "Jiro Ramen", 5, 5, "Eating Jiro Ramen with Hang", "Hang loves vegitables so much."))
    rows = db.fetch_all()
    print(rows)
