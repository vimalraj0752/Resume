import sqlite3
import random

conn = sqlite3.connect("resume.db")
cur = conn.cursor()

cur.execute("SELECT id, name FROM candidates")
data = cur.fetchall()

print("\nResume Ranking:\n")

rank = 1
for cid, name in data:
    print(cid,name)
    score = random.randint(60, 95)

    print(f"Rank {rank}: {name} — {score}%")

    cur.execute("""
        UPDATE candidates
        SET rank = ?
        WHERE id = ?
    """, (rank, cid))

    rank += 1

conn.commit()
conn.close()

print("\n✅ Rank updated in database!")
