# -*- coding: utf-8 -*-
"""Task database class
"""
import sqlite3
import logging
import datetime

from .TableItem import *


class Database():
    """Task database class

    Args:
        db_name (str): data base file name

    """

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks ( task_id INTEGER PRIMARY KEY, active BOOLEAN NOT NULL, title TEXT NOT NULL UNIQUE, importance INTEGER DEFAULT 2, urgency INTEGER DEFAULT 2, detail TEXT, memo TEXT, man_hour FLOAT, create_date TIMESTAMP);")

        # check if tasks_fts table exists
        table_found = self.cur.execute(
            "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tasks_fts'").fetchall()[0]

        # if the count is 1, then table exists
        if not table_found:
            # create and copy from tasks table
            self.cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS tasks_fts USING fts4(task_id INTEGER PRIMARY KEY, active BOOLEAN NOT NULL, title TEXT NOT NULL UNIQUE, importance INTEGER DEFAULT 2, urgency INTEGER DEFAULT 2, detail TEXT, memo TEXT, man_hour FLOAT, create_date TIMESTAMP);")
            self.cur.execute("INSERT INTO tasks_fts SELECT * FROM tasks;")

        # Add trigers
        self.cur.execute("CREATE TRIGGER IF NOT EXISTS on_task_add AFTER INSERT ON tasks BEGIN INSERT INTO tasks_fts (task_id, active, title, importance, urgency, detail, memo, man_hour, create_data) VALUES (new.task_id, new.active, new.title, new.importance, new.urgency, new.detail, new.memo, new.man_hour, new.create_data); END;")
        self.cur.execute("CREATE TRIGGER IF NOT EXISTS on_task_delete AFTER DELETE ON tasks BEGIN INSERT INTO tasks_fts (task_id, active, title, importance, urgency, detail, memo, man_hour, create_data) VALUES ('delete', old.task_id, old.active, old.title, old.importance, old.urgency, old.detail, old.memo, old.man_hour, old.create_data); END;")
        self.cur.execute("CREATE TRIGGER IF NOT EXISTS on_task_update AFTER UPDATE ON tasks BEGIN INSERT INTO tasks_fts (task_id, active, title, importance, urgency, detail, memo, man_hour, create_data) VALUES ('delete', old.task_id, old.active, old.title, old.importance, old.urgency, old.detail, old.memo, old.man_hour, old.create_data); INSERT INTO tasks_fts (task_id, active, title, importance, urgency, detail, memo, man_hour, create_data) VALUES (new.task_id, new.active, new.title, new.importance, new.urgency, new.detail, new.memo, new.man_hour, new.create_data); END;")

        # updte db
        self.conn.commit()

    def fetch(self, task_id):
        """Get task from database

        Args:
            task_id (Int): task id

        """
        rows = self.cur.execute(
            "SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchall()
        return [
            TableItem(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]) for row in rows]

    def fetch_all(self, only_active=False):
        """Get all task from database

        """
        rows = self.cur.execute("SELECT * FROM tasks WHERE active = 1;").fetchall(
        ) if only_active else self.cur.execute("SELECT * FROM tasks;").fetchall()
        return [
            TableItem(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]) for row in rows]

    def create(self, item):
        """Create task on database

        Args:
            item (TableItem): task data to be created

        """
        self.cur.execute(
            "INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?, ?, ?, 0.0, ?)",
            (item.active,
             item.title.rstrip(),
             item.importance,
             item.urgency,
             item.detail.rstrip(),
             item.memo.rstrip(),
             item.create_time))
        self.conn.commit()

    def update(self, item):
        """Update task on database

        Args:
            item (TableItem): task data to be updated

        """
        self.cur.execute(
            "UPDATE tasks SET active = ?, title = ?, importance = ?, urgency = ?, detail = ?, memo = ?, man_hour = ? WHERE task_id = ?",
            (item.active,
             item.title.rstrip(),
             item.importance,
             item.urgency,
             item.detail.rstrip(),
             item.memo.rstrip(),
             item.man_hour,
             item.task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        """Deactivate task on database

        Args:
            task_id (Int): task id

        """
        self.cur.execute(
            "UPDATE tasks SET active = 0 WHERE task_id = ?", (task_id,))
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
