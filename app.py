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

login_manager = LoginManager()


app = Flask(__name__, template_folder='templates')

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'#_3y2L_"F4Q8z\n\xec]/'

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

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
@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('/'))
    return render_template("login.html")

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