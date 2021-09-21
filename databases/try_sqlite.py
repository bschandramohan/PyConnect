import sqlite3

db = sqlite3.connect("tags-sqlite.db")

cursor = db.cursor()

# cursor.execute("CREATE TABLE tags (id INTEGER PRIMARY KEY, tag varchar(250) NOT NULL UNIQUE)")
cursor.execute("INSERT INTO tags VALUES (245, 'abcd') ")
db.commit()

db.close()
