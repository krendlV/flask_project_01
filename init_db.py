import sqlite3
from flask import current_app, g
import click

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

def close_db(e=None):
    db = g.pop('db', None)

    # if connection exists -> closed
    if db is not None:
        db.close()

def init_db():
    #return database connection
    db = get_db()
    # flush needed as stdout is BUFFERED
    print('init_db(): get_db()...', flush=True)

    #open_resource opens file relative to flask_auu package
    #create tables etc
    with current_app.open_resource('tools/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        print('init_db(): schema successfully created...', flush=True)

    #open_resource opens file relative to flask_auu package
    #insert data
    with current_app.open_resource('tools/db_insertdata.sql') as f:
        db.executescript(f.read().decode('utf8'))
        print('init_db(): data successfully inserted...', flush=True)

#defines command line command init-db that calls init_db function
#   and shows success message to the user
# DO: flask --app flask_auu init-db BEFORE db is used
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    print('init_db_command(): init_db() done...', flush=True)

#register close_db and init_db_command with app instance
# due to using a factory function, the instance is not available when writing the functions
# solution: function that takes an app and does registration
def init_app(app):
        # Flask will call function when cleaning up
        app.teardown_appcontext(close_db)
        # new command, can be called with flask
        app.cli.add_command(init_db_command)







#--- das untere hab ich vorher ghabt:
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