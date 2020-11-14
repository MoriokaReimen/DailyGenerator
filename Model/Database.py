# -*- coding: utf-8 -*-
"""Task database class
"""
import sqlite3
import logging

from .TableItem import *

class Database():
    """Task database class

    Args:
        db_name (str): data base file name

    """
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks ( task_id INTEGER PRIMARY KEY, active BOOLEAN NOT NULL, title TEXT NOT NULL UNIQUE, importance INTEGER DEFAULT 2, urgency INTEGER DEFAULT 2, detail TEXT, memo TEXT);")

    def fetch(self, task_id):
        """Get task from database

        Args:
            task_id (Int): task id

        """
        rows = self.cur.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchall()
        return [TableItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows ]

    def fetch_all(self):
        """Get all task from database

        """
        rows = self.cur.execute("SELECT * FROM tasks;").fetchall()
        return [TableItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows ]

    def create(self, item):
        """Create task on database

        Args:
            item (TableItem): task data to be created

        """
        self.cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (item.active, item.title.rstrip(), item.importance, item.urgency, item.detail.rstrip(), item.memo.rstrip()))
        self.conn.commit()

    def update(self, item):
        """Update task on database

        Args:
            item (TableItem): task data to be updated

        """
        self.cur.execute("UPDATE tasks SET active = ?, title = ?, importance = ?, urgency = ?, detail = ?, memo = ? WHERE task_id = ?", (item.active, item.title.rstrip(), item.importance, item.urgency, item.detail.rstrip(), item.memo.rstrip(), item.task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        """Deactivate task on database

        Args:
            task_id (Int): task id

        """
        self.cur.execute("UPDATE tasks SET active = 0 WHERE task_id = ?", (task_id,))
        self.conn.commit()

    def remove(self, task_id):
        """Delete task on database

        Args:
            task_id (Int): task id

        """
        self.cur.execute("DELETE FROM tasks WHERE task_id=?", (task_id,))
        self.conn.commit()

    def __del__(self):
        """Close database

        """
        self.conn.close()
        logging.info("Database closed successfully.")
