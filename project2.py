import sqlite3
from flask import Flask, render_template, request
import werkzeug
import flask_sqlalchemy
import flask

#wie heisst unsere db und wo ist sie? bzw wie kann ich sie importieren wie er es gemavjt hat mit:
# from flask_auu.db import get_db
#from flask_project_01-master.db import get_db


#con=sqlite3.connect("testdata.sql")
#cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")
#res=cur.execute("SELECT name FROM sqlite_master")




app = flask(__name__, template_folder='templates')

@app.route('/Projekte/Projekt2/search', methods=('GET', 'POST')) #wie 
@app.route('/Projekte/Projekt2', methods=('GET', 'POST'))





#Seemeilen
def search():


    con=sqlite3.connect("testdata.sql")
    cur = con.cursor()


    if request.method == "POST": 
        Seemeilen = request.form['Seemeilen']
        Inventarnummer = request.form['Inventarnummer']

        if  (not Seemeilen) and (not Inventarnummer):
            print('input is required.')

    
        else:


            Seemeilen = cur.execute(
                
                "select Seemeilen, Inventarnummer from Schiff").fetchall()
    


            return render_template('project2/search.html', Seemeilen=Seemeilen, Inventarnummer=Inventarnummer)
    else:
          return render_template('project2/search.html')
    


#TODO:

#def update_seemeilen():
   # if request.method == "GET":


