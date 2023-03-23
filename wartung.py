import sqlite3

def get_technicians(ship_type):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    # Execute the SQL query to retrieve the technicians who can service the specified ship type
    query = "SELECT Name FROM Techniker WHERE ship_type_id = (SELECT ship_type_id FROM ShipTypes WHERE ship_type = ?)"
    cursor.execute(query, (ship_type,))
    
    # Fetch the results and store them in a list
    results = []
    for row in cursor:
        results.append(row[0])
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()
    
    # Return the list of technicians who can service the specified ship type
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input from the HTML form
        ship_type = request.form['ship_type']
        
        # Call the get_technicians function to retrieve the technicians who can service the specified ship type
        technicians = get_technicians(ship_type)
        
        # Render the results in an HTML template and return it
        return render_template('results.html', technicians=technicians, ship_type=ship_type)
    
    # If no user input has been submitted yet, just render the HTML form
    return render_template('formform.html')