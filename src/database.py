import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent

        self.db_folder = self.root / "database"
        self.db_folder.mkdir(exist_ok=True)

        self.db_file = self.db_folder / "rcis.db"

        self.conn = sqlite3.connect(self.db_file)

        self.create_tables()

    def create_tables(self):

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS recordings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            filepath TEXT UNIQUE,
            filesize INTEGER,
            language TEXT,
            duration REAL,
            status TEXT DEFAULT 'Pending',
            transcript TEXT,
            english TEXT,
            summary TEXT,
            error TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
        )
        """)

        self.conn.commit()

    def register(self, filepath):

        p = Path(filepath)

        cur = self.conn.cursor()

        cur.execute(
            "SELECT id FROM recordings WHERE filepath=?",
            (str(p),)
        )

        if cur.fetchone():
            return False

        self.conn.execute("""
            INSERT INTO recordings(
                filename,
                filepath,
                filesize
            )
            VALUES(?,?,?)
        """,
        (
            p.name,
            str(p),
            p.stat().st_size
        ))

        self.conn.commit()

        return True

    def pending(self):

        cur = self.conn.cursor()

        cur.execute("""
            SELECT filepath
            FROM recordings
            WHERE status='Pending'
            ORDER BY id
        """)

        return [r[0] for r in cur.fetchall()]

    def update(
            self,
            filepath,
            status,
            transcript="",
            language="",
            error=""
    ):

        self.conn.execute("""
        UPDATE recordings
        SET
            status=?,
            transcript=?,
            language=?,
            error=?,
            updated_at=CURRENT_TIMESTAMP
        WHERE filepath=?
        """,
        (
            status,
            transcript,
            language,
            error,
            filepath
        ))

        self.conn.commit()

    def close(self):
        self.conn.close()