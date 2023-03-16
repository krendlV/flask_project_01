import re
import sqlite3
from datetime import datetime
from flask import Flask
from flask import render_template
import os


app = Flask(__name__, template_folder='templates')

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Replace the existing home function with the one below
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
@app.route("/login/")
def login():
    return render_template("login.html")

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