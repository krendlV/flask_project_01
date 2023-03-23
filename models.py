#from app import db  # importiere die Datenbank aus app.py
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from app import db # import the 'db' object from the models file

# Create a user model

# iwie hab ich seit stunden Zirkuläre imports und es ist keine Zeit mehr, ich kopier das jetzt einfach ins app.py und lass das hier für Dokumentation, ist aber nicht mehr benutzt.

class User(UserMixin, db.Model):
  __tablename__ = 'User'
  __table_args__ = {'extend_existing': True} # damit ich die Tabelle erweitern kann, ohne sie neu zu erstellen
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique = True, index = True)
  password_hash = db.Column(db.String(150))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)
  Sozialversicherungsnummer = db.Column(db.Integer, db.ForeignKey('Person.Sozialversicherungsnummer'), unique=True)

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self,password):
      return check_password_hash(self.password_hash,password)
  
# Create a Pseron Model

class Person(db.Model):
    __tablename__ = 'Person'
    Sozialversicherungsnummer = db.Column(db.Integer, primary_key=True)
    Vorname = db.Column(db.String(50))
    Nachname = db.Column(db.String(50))
    Postleitzahl = db.Column(db.Integer)
    Ort = db.Column(db.String(50))
    Straße = db.Column(db.String(50))
    Hausnummer = db.Column(db.Integer)
    Telefonnummer = db.Column(db.Integer)

    users = db.relationship('User', backref='person', uselist=False) # I <3 SQLAlchemy, mit der backref kann ich Person objects von User aus ansprechen

# Create a Passagier Model

class Passagier(db.Model):
    __tablename__ = 'Passagier'
    Passagiernummer = db.Column(db.Integer, primary_key=True)
    Sozialversicherungsnummer = db.Column(db.Integer, db.ForeignKey('Person.Sozialversicherungsnummer'), nullable=False)

    # Define a relationship to the Person table
    Person = db.relationship('Person', backref=db.backref('passagiere', lazy=True))

    def __repr__(self): # so kann ich die Passagiernummer als String ausgeben lassen. auch nützllich für Debugging & logging
        return f'<Passagier {self.Passagiernummer}>'
    
# Angestellter Model

class Angestellter(db.Model):
    __tablename__ = 'Angestellter'
    Angestelltennummer = db.Column(db.Integer, primary_key=True)
    Sozialversicherungsnummer = db.Column(db.Integer, db.ForeignKey('Person.Sozialversicherungsnummer'), nullable=False)
    
    def __repr__(self):
        return f"<Angestellter {self.Angestelltennummer}>"
    
# Gehaltskonto Model

class Gehaltskonto(db.Model):
    __tablename__ = 'Gehaltskonto'
    Kontonummer = db.Column(db.Integer, primary_key=True)
    Bankleitzahl = db.Column(db.Integer, db.ForeignKey('Bank.Bankleitzahl'), nullable=False)
    Konstostand = db.Column(db.Integer)
    Bankname = db.Column(db.Text)
    Angestelltennummer = db.Column(db.Integer, db.ForeignKey('Angestellter.Angestelltennummer'), unique=True)

    def __repr__(self):
        return f'<Gehaltskonto {self.Kontonummer}>'

# Passage Model

class Passage(db.Model):
    __tablename__ = 'Passage'
    Passagennummer = db.Column(db.Integer, primary_key=True)
    Abfahrtshafen = db.Column(db.String(50))
    Zielhafen = db.Column(db.String(50))
    Abfahrtszeit = db.Column(db.Time)
    Ankunftszeit = db.Column(db.Time)

# Anschlusspassage Model
# bei dem bin ich mir ned sicher...

class Anschlusspassage(db.Model):
    __tablename__ = 'Anschlusspassage'
    passagennummer_1 = db.Column(db.Integer, db.ForeignKey('Passage.Passagennummer'), primary_key=True)
    passagennummer_2 = db.Column(db.Integer, db.ForeignKey('Passage.Passagennummer'), primary_key=True)
    passage_1 = db.relationship('Passage', foreign_keys=[passagennummer_1])
    passage_2 = db.relationship('Passage', foreign_keys=[passagennummer_2])

# Schifftyp Model

class Schifftyp(db.Model):
    __tablename__ = 'Schifftyp'
    Typennummer = db.Column(db.Integer, primary_key=True)
    Bruttoregistertonnen = db.Column(db.Numeric)
    Besatzungsstaerke = db.Column(db.Integer) # changed bc. possible ASCII error (ä is not ASCII)
    Typenbezeichnung = db.Column(db.String(50))
    Name = db.Column(db.String(50), db.ForeignKey('Hersteller.Name')) # now referenced with Hersteller Table
    hersteller = db.relationship('Hersteller', backref='schifftypen')

# Buchung Model

class Buchung(db.Model):
    __tablename__ = 'Buchung'
    Buchungsnummer = db.Column(db.Integer, primary_key=True)
    Passagennummer = db.Column(db.Integer, db.ForeignKey('Passage.Passagennummer'))
    Passagiernummer = db.Column(db.Integer, db.ForeignKey('Passagier.Passagiernummer'), nullable=False)
    Buchungsdatum = db.Column(db.Date)
    Klasse = db.Column(db.Text)
    passagier = db.relationship('Passagier', backref='buchungen')
    passage = db.relationship('Passage', backref='buchungen')

# Schiff Model

class Schiff(db.Model):
    __tablename__ = 'Schiff'
    Inventarnummer = db.Column(db.Integer, primary_key=True)
    Typennummer = db.Column(db.Integer, db.ForeignKey('Schifftyp.Typennummer'), nullable=False)
    Jahr_der_Fertigung = db.Column(db.Integer)
    Seemeilen = db.Column(db.Numeric)
    
    schifftyp = db.relationship('Schifftyp', backref=db.backref('schiffe', lazy=True)) # lazy means it is only loaded when accessed.

# captn model

class Kapitaen(db.Model): # changed Umlaut to ae
    __tablename__ = 'Kapitaen'
    Kapitaenspatentnummer = db.Column(db.Integer, primary_key=True) # changed umlaut to ae
    Angestelltennummer = db.Column(db.Integer, db.ForeignKey('Angestellter.Angestelltennummer'), nullable=False)
    Seemeilen = db.Column(db.Numeric)
    
    def __repr__(self):
        return f"Kapitän {self.Kapitänspatentnummer}"

# Logbuch Model

class Logbuch(db.Model):
    __tablename__ = 'Logbuch'
    Code = db.Column(db.Integer, primary_key=True)
    Inventarnummer = db.Column(db.Integer, unique=True)
    Angestelltennummer = db.Column(db.Integer)
    Inventarnummer_fk = db.ForeignKey('Schiff.Inventarnummer')
    Angestelltennummer_fk = db.ForeignKey('Angestellter.Angestelltennummer')

# telefonnummer model

class Telefonnummer(db.Model):
    __tablename__ = 'Telefonnummer'
    Telefonnummer = db.Column(db.Integer, primary_key=True)
    Sozialversicherungsnummer = db.Column(db.Integer, db.ForeignKey('Person.Sozialversicherungsnummer'))

# Bank Model

class Bank(db.Model):
    __tablename__ = "Bank"
    Bankleitzahl = db.Column(db.Integer, primary_key=True)
    Bankname = db.Column(db.String(50))

# Hersteller Model

class Hersteller(db.Model):
    __tablename__ = 'Hersteller'
    Name = db.Column(db.String(50), primary_key=True)

# techniker model

class Techniker(db.Model):
    __tablename__ = 'Techniker'
    Lizenznummer = db.Column(db.Integer, primary_key=True)
    Angestelltennummer = db.Column(db.Integer, db.ForeignKey('Angestellter.Angestelltennummer'), primary_key=True)
    Grad_der_Ausbildung = db.Column(db.String(50)) # changed the spaces so it is a proper python Variable
    Typennummer = db.Column(db.Integer, db.ForeignKey('Schifftyp.Typennummer'))

    def __repr__(self):
        return f'<Techniker {self.Lizenznummer}>'

# captn Passage Model

class KapitaenPassage(db.Model): # Umlaut entfernt
    __tablename__ = 'KapitaenPassage'

    Kapitaenspatentnummer = db.Column(db.Integer, db.ForeignKey('Kapitaen.Kapitaenspatentnummer'), primary_key=True)
    Passagennummer = db.Column(db.Integer, db.ForeignKey('Passage.Passagennummer'), primary_key=True)
    Typennummer = db.Column(db.Integer, db.ForeignKey('Schiff.Typennummer'))

    kapitaen = db.relationship('Kapitaen', backref='passagen')
    passage = db.relationship('Passage', backref='kapitaene')
    schiff = db.relationship('Schiff', backref='kapitaene') # keine Ahnung ob das mim Plural wirklich automatisch erkannt wird...
