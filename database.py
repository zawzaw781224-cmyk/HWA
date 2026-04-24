import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT,
password TEXT
)
""")

cursor.execute(
"INSERT INTO users (username,password) VALUES (?,?)",
("hwsm","312023")
)

conn.commit()
conn.close()

print("database created")