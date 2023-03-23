import re
import sqlite3
from datetime import datetime
from flask import Flask
from flask import render_template
import os
from flask import session
from flask import abort, redirect, url_for
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
#from models import User, Person, Passagier, Gehaltskonto, Schiff, Schifftyp, Angestellter, Kapitaen, Logbuch, Telefonnummer, Bank, Hersteller, Techniker, KapitaenPassage, Passage, Anschlusspassage, Buchung
#i load it later in the create_db function
#from models import db # import the 'db' object from the models file
from config import config



app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app) # derweil auskommentiert weil ich die db aus models.py importiere

# here i create all the models with which the tables are created.
# create User Model
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






def create_db():
    db.drop_all()
    db.create_all()

#create_db()
# Auskommentieren nachdem die DB erstellt wurde...

login_manager = LoginManager()
login_manager.init_app(app)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) # es gehört .query dazu, das is in der Flask Doku falsch!!!



class RegistrationForm(FlaskForm):
    username = StringField('username', validators =[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password1')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me',validators= [DataRequired()])
    submit = SubmitField('Login')


# Home sweet Home
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/team/")
def team():
    return render_template("team.html")

@app.route("/work/")
def work():
    return render_template("work.html")

# Projects
# project 1
@app.route('/register/', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('home'))
        flash('Invalid email address or Password.')    
    return render_template('login.html', form=form)


@app.route("/logout/")
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('/'))

# project 2
@app.route("/project2/")
def project2():
    return render_template("project2.html")

# project 3
@app.route("/project3/")
def project3():
    return render_template("project3.html")

# project 4
@app.route("/project4/")
def project4():
    return render_template("project4.html")

# project 5
@app.route("/project5/", methods=['GET', 'POST'])
def project5():
    #i dont know how to conect to the database to execute my sql query 
    data = sqlite3.connect('data.db')
    logbuchliste = data.execute(
        "SELECT Code, Inventarnummer,Angestelltennummer"
        "FROM Logbuch"
    ).fetchall()
    return render_template("project5.html",logbuchliste=logbuchliste)


