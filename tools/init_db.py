import sqlite3

connection = sqlite3.connect('data.db')

with open ('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Beispiel für ein befülln von Datenbank Tabelle

#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#           ('First Post', 'Content for the first post')
#            )

connection.commit()
connection.close()