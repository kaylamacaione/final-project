# Import libraries
import os
import collections
from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pickle

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#################################################
# Database Setup
#################################################

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
def dest_airports():
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

    return jsonify(airport_data)

# Flask route to use predict button in app
@app.route('/predict',methods=['POST'])
def predict():

    # To render results on HTML GUI
    int_features = [float(x) for x in request.form.values()]

    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 

    ################################################## UPDATE THIS LATER
    return render_template('index.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))

if __name__ == "__main__":
    app.run()
