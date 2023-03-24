from flask import Flask, render_template, request
import sqlite3
import random

@app.route("/project4/", methods=["GET", "POST"])

def booking_info():

    if request.method == "POST"
        booking_id = request.form["booking_id"]

        conn = sqlite3.connect("data.db")
        c = conn.cursor()

        c.execute("SELECT Passagennummer, Passagiernummer, Buchungsdatum, Klasse FROM Buchung WHERE Buchungsnummer = ?",
                  (booking_id))
        bookings = c.fetchone()

        conn.close()

        return render_template("buchungsinfo.html", bookings=bookings)


    return render_template("buchungsinfo.html")


def create_booking():
    if request.method == 'POST':
        # Get form data
        travel_class = request.form['travel_class']
        # Generate random passage number, passenger number, and booking number
        passage_num = random.randint(100, 999)
        passenger_num = random.randint(10000, 99999)
        booking_num = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Insert booking data into database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Buchung (passenger_num, passage_num, booking_num, travel_class) VALUES (?, ?, ?, ?)', (Passagiernummer, Passagennummer, Buchungsnummer, Klasse))
        conn.commit()
        # Get the ID of the newly inserted row
        booking_id = c.lastrowid
        conn.close()
        # Return a success message with the newly generated booking number
        return render_template('erfolg.html', booking_num=booking_num)
    # If request method is GET, show the form
    return render_template('buchung_erstellen.html')