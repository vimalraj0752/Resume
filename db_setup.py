import sqlite3

conn = sqlite3.connect("resume.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    rank INTE
    filename TEXT,
    filepath TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER,
    score REAL,
    rank INTEGER
)
""")

conn.commit()
conn.close()

print("✅ Database ready!")
