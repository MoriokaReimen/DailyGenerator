import sqlite3
import logging

from .TableItem import *

class Database():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY, active BOOLEAN NOT NULL, title TEXT NOT NULL UNIQUE, importance INTEGER DEFAULT 2, urgency INTEGER DEFAULT 2, detail TEXT, memo TEXT);")

    def fetch(self, id):
        rows = self.cur.execute("SELECT * FROM tasks WHERE id=?", (id,)).fetchall()
        return [TableItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows ]

    def fetch_all(self):
        rows = self.cur.execute("SELECT * FROM tasks;").fetchall()
        return [TableItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows ]

    def create(self, item):
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (item.active, item.title.rstrip(), item.importance, item.urgency, item.detail.rstrip(), item.memo.rstrip()))
        self.conn.commit()

    def update(self, item):
        self.cur.execute("UPDATE tasks SET active = ?, title = ?, importance = ?, urgency = ?, detail = ?, memo = ? WHERE id = ?", (item.active, item.title.rstrip(), item.importance, item.urgency, item.detail.rstrip(), item.memo.rstrip(), item.id))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        logging.info("Database closed successfully.")
