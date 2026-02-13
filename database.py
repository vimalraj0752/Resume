import sqlite3

# database create/connect
conn = sqlite3.connect("resume.db")
cur = conn.cursor()

# resumes table
cur.execute("""
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT NOT NULL,
    email TEXT,
    pdf_path TEXT NOT NULL,
    ai_score REAL,
    rank INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# index (fast search for 1000+ resumes)
cur.execute("""
CREATE INDEX IF NOT EXISTS idx_name
ON resumes(candidate_name)
""")

conn.commit()
conn.close()

print("✅ SQL database ready for 1000+ resumes!")
