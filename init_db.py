import sqlite3
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User, Person, Passagier, Gehaltskonto, Schiff, Schifftyp, Angestellter, Kapitaen, Logbuch, Telefonnummer, Bank, Hersteller, Techniker, KapitaenPassage, Passage, Anschlusspassage, Buchung
from app import app

# vorher alle Tables löschen weil SQLAlchemy das in Metadaen speichert
db.drop_all()

# create all tables
db.create_all()







#--- das untere hab ich vorher ghabt:
#connection = sqlite3.connect('data.db')

#with open ('tools/schema.sql') as f:
#    connection.executescript(f.read())

#cur = connection.cursor()

# Beispiel für ein befülln von Datenbank Tabelle
#cur.execute("INSERT INTO user (username, email, password, date_created) VALUES (?, ?, ?, ?)",
#            ('test', 'test@gmail.com', '1q2w3', '2023-03-18 12:11:32.660910')
##)
#cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#           ('First Post', 'Content for the first post')
#            )

#connection.commit()
#connection.close()