import sqlite3
from flask import current_app, g

def get_db():
        print('get_db(): before db is accessed...', flush=True)

        # connection stored and reused if not created
        if 'db' not in g:
            # establish a connection to db file
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            # connection returns row
            g.db.row_factory = sqlite3.Row

        return g.db

connection = sqlite3.connect('data.db')

with open ('tools/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Beispiel für ein befülln von Datenbank Tabelle

#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#           ('First Post', 'Content for the first post')
#            )

connection.commit()
connection.close()