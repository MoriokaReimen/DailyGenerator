import sqlite3
import logging
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class TableItem:
    id: int
    active: bool
    title: str
    importance: int
    urgency: int
    detail: str
    memo: str

class Model():

    def __init__(self, control):
        self.db = Database("tasks.db")
        self.daily_gen = DailyGenerator()
        self.control = control

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
        self.cur.execute("INSERT OR REPLACE INTO tasks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (item.active, item.title, item.importance, item.urgency, item.detail, item.memo))
        self.conn.commit()

    def update(self, item):
        self.cur.execute("INSERT OR REPLACE INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?)", (item.id, item.active, item.title, item.importance, item.urgency, item.detail, item.memo))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        logging.info("Database closed successfully.")

class DailyGenerator():
    def __init__(self):
        pass

    def generate(self, rows):
        text = "Dear Someone\n"
        for row in rows:
            if row.active:
                text += \
                    "Title:{title}\n" \
                    "====================================================================================================\n" \
                    "Importance:\t{importance}\n" \
                    "Urgency:\t{urgency}\n" \
                    "Detail:\n{detail}\n\n\n" \
                    .format(**asdict(row))

        text += "Regards"
        return text


    def __del__(self):
        logging.info("Daily file closed successfully.")


if __name__ == '__main__':
    daily = DailyGenerator()
    db = Database("database.db")
    db.insert(TableItem(0, True, "Jiro Ramen", 5, 5, "Eating Jiro Ramen with Hang", "Hang loves vegitables so much."))
    db.insert(TableItem(0, False, "Jiro Ramen2", 5, 5, "Eating Jiro Ramen with Hang", "Hang loves vegitables so much."))
    db.insert(TableItem(0, True, "Jiro Ramen3", 5, 5, "Eating Jiro Ramen with Hang", "Hang loves vegitables so much."))
    rows = db.fetch_all()
    daily.generate(rows)
