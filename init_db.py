import sqlite3
from flask import current_app, g



#--- das untere hab ich vorher ghabt:
connection = sqlite3.connect('data.db')

with open ('tools/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Beispiel für ein befülln von Datenbank Tabelle
cur.execute("INSERT INTO user (username, email, password, date_created) VALUES (?, ?, ?, ?)",
            ('test', 'test@gmail.com', '1q2w3', '2023-03-18 12:11:32.660910')
)
#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#           ('First Post', 'Content for the first post')
#            )

connection.commit()
connection.close()