from flask import Flask, render_template, request
import sqlite3

@app.route("/project4/", methods=["GET", "POST"])

def project4():

    if request.method == "POST"
        booking_id = request.form["booking_id"]

        conn = sqlite3.connect("project4.sql")
        c = conn.cursor()

        c.execute("SELECT Passagennummer, Passagiernummer, Buchungsdatum, Klasse FROM Buchung WHERE Buchungsnummer = ?",
                  (booking_id))
        bookings = c.fetchone()

        conn.close()



        return render_template("project4.html", bookings=bookings)


    return render_template("project4.html")
