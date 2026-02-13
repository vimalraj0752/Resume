import sqlite3

conn = sqlite3.connect("resume.db")
cur = conn.cursor()

name = input("Name: ")
email = input("Email: ")
file = input("Resume filename: ")

cur.execute("INSERT INTO candidates (name,email,filename) VALUES (?,?,?)",
            (name,email,file))

conn.commit()
conn.close()

print("Added!")

