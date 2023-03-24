from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from app import db 
import config
from models import User, UserMixin



app = Flask(__name__)
app.secret_key= "hello"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Schiff.sqlite3'#user muss noch ausgetauscht werden mit dem table, zu dem referenziert wird
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.init_app(app)


# Schiff Model

class Schiff(db.Model):
    __tablename__ = 'Schiff'
    Inventarnummer = db.Column(db.Integer, primary_key=True)
    Typennummer = db.Column(db.Integer, db.ForeignKey('Schifftyp.Typennummer'), nullable=False)
    Jahr_der_Fertigung = db.Column(db.Integer)
    Seemeilen = db.Column(db.Numeric)

    
    
    schifftyp = db.relationship('Schifftyp', backref=db.backref('schiffe', lazy=True))

@app.route('/')
def home():
    return render_template("index.html")#Valentins homesite



@app.route("/project2", methods = ["POST", "GET"])
@app.route("/project2/view", methods=["POST", "GET"])
def ships():
        if request.method == "POST":
             shipnr = request.form["xy"]
             #session["shipnr"]= shipnr # ----->>>> wohin zeigt die session? was ist in session? like in: in user-funktion(user): if "user" in session: user = session["user"]
             found_ship = session.query.filter_by(Inventarnummer=shipnr).first()
             if found_ship:
                  #return(Schiff.Seemeilen)
                  session[shipnr]=found_ship
                  seemeilen=session.query(found_ship.Inventarnummer, found_ship.Seemeilen).filter_by(Inventarnummer=shipnr).first()
                  return render_template("view.html", values=seemeilen)
             else:
                  return redirect(url_for("shipnr"))#url_for muss noch auf eine andere Funktion mit key:value pair referenzieren
        #    return render_template(inventarnr.html)

        else:
             return render_template("project2.html")
 #found_ship.seemeilen=seemeilen gehört in die nächste Funktion, oder ich muss sie erstnoch kombinieren

#@app.route


@app.route("/shipnr", methods=["POST", "GET"])#die 2.Funktion mit Speichern der Eingabe seemeilen?
def seemeilen_update():
     
     
            #TODO
            return render_template()


  #found_ship.seemeilen=seemeilen
    #if request.method==["POST"]:




if __name__ == "__main__":
    db.create_all() 
    app.run(debug=True)


