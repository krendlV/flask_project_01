import re
import sqlite3
from datetime import datetime
from flask import Flask
from flask import render_template
import os
from flask_login import LoginManager
from flask import session
from flask import abort, redirect, url_for
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash
from flask import current_app, g
from init_db import get_db
from sqlalchemy import SQLAlchemy
from flask_login import UserMixin



app = Flask(__name__, template_folder='templates')

app.config[‘SQLALCHEMY_DATABASE_URI’] = ‘sqlite:///data.db’
app.config[‘SQLALCHEMY_TRACK_MODIFICATIONS’] = False
db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique = True, index = True)
  password_hash = db.Column(db.String(150))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self,password):
      return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

    

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
@app.route('/register/', methods=('GET', 'POST'))
def register():
    # when user submits form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        #valide usr/pw not empty
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                #inser usr/pw into db
                # generate_password_hash to securely hash pw
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityErrror:
                error = f"User {username} is already registered."
            else:
                # after storing usr/pw-> redirect to login
                return redirect(url_for("login"))

        # in case of error
        flash(error)

    #html rendering
    return render_template('register.html')


@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        #fetchone returns  one row from the query

        if user is None:
            error = 'Incorrect username.'

        #hash submitted password and compare
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            #session is a dict that stores data across request
            # user id stored in session!
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('home'))

        flash(error)

    return render_template('login.html')


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
@app.route("/project5/")
def project5():
    return render_template("project5.html")

random_bytes = os.urandom(22)
print(random_bytes)