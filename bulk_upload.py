import sqlite3
import os

UPLOAD_FOLDER = "static/uploads"

conn = sqlite3.connect("resume.db")
cur = conn.cursor()

files = os.listdir(UPLOAD_FOLDER)

for file in files:
    name = file.split(".")[0]
    email = name + "@mail.com"
    path = UPLOAD_FOLDER + "/" + file

    cur.execute("""
    INSERT INTO candidates (name, email, filename, filepath)
    VALUES (?, ?, ?, ?)
    """, (name, email, file, path))

    print("Uploaded:", file)

conn.commit()
conn.close()

print("\n✅ Bulk upload completed!")
