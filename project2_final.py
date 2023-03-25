# project 2
@app.route('/project2/', methods=['POST', 'GET'])
def project2():
        if request.method == "POST":
             shipnr = request.form["shipnr"]
             found_ship = db.session.query.filter_by(Inventarnummer=shipnr).first()
             if found_ship:
                  session[shipnr]=found_ship
                  seemeilen=db.session.query(found_ship.Inventarnummer, found_ship.Seemeilen).filter_by(Inventarnummer=shipnr).first()
                  session['seemeilen']=seemeilen
                  if seemeilen:
                      return redirect(url_for("update.html"))
                      
                  else: 
                    return render_template("Schiffnr.html")
             else:
                  return render_template("Schiffnr.html")

        else:
             return render_template("Schiffnr.html")
        

@app.route('/update', method =['POST', 'GET'])
def update():
    if request.method=="POST":
        update= Schiff(shipnr=request.form["shipnr"], Seemeilen=request.form["seemeilen"])
        db.session.add(update)
        db.session.commit()
        return flash("Seemeilen wurden geändert")
    else:
        return render_template("update.html")