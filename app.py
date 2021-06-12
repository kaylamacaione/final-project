# Import libraries
import os
import collections
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

# Define database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dest_airports.sqlite"

db = SQLAlchemy(app)

# Define database table and column attributes
class Destinations(db.Model):
    __tablename__ = 'dest_airports'

    primary_id = db.Column(db.Integer, primary_key=True)
    DEST = db.Column(db.String(10))
    DISTANCE = db.Column(db.Float)
    airport_name = db.Column(db.String(50))
    dest_longitude = db.Column(db.Float)
    dest_latitude = db.Column(db.Float)

    def __repr__(self):
        return '<Destinations %r>' % (self.name)

# Flask route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Flask route to query data from SQLite database and output in json format
@app.route("/api/dest_airports")
def olympics():
    results = db.session.query(Destinations.primary_id, Destinations.DEST, Destinations.DISTANCE, Destinations.airport_name, Destinations.dest_longitude, Destinations.dest_latitude).all()

    airport_data = []

    # Loop through query results and assign key value pairs for each row
    for result in results:
        dict = collections.OrderedDict()
        dict["primary_id"] = result[0]
        dict["DEST"] = result[1]
        dict["DISTANCE"] = result[2]
        dict["airport_name"] = result[3]
        dict["dest_longitude"] = result[4]
        dict["dest_latitude"] = result[5]
        airport_data.append(dict)

    # Loop through query results and assign variables to each series
    # primary_id = [result[0] for result in results]
    # NOC = [result[1] for result in results]
    # Region = [result[2] for result in results]
    # Medal = [result[3] for result in results]
    # Year = [result[4] for result in results]

    # Assign key value pairs to data series
    # olympics_data = [{
    #     "primary_id": primary_id,
    #     "NOC": NOC,
    #     "Region": Region,
    #     "Medal": Medal,
    #     "Year": Year
    # }]
    
    return jsonify(airport_data)


if __name__ == "__main__":
    app.run()
