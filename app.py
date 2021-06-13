# Import libraries
import os
import collections
from flask import (Flask, render_template, jsonify, request, redirect)
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


#################################################
# Database Setup
#################################################

# Define database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/dest_airports.sqlite" 

db = SQLAlchemy(app)

# Define database table attributes
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



#################################################
# App Routes
#################################################

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

    # results = db.session.query(Destinations.primary_id, Destinations.DEST, Destinations.DISTANCE, Destinations.airport_name, Destinations.dest_longitude, Destinations.dest_latitude).all()

    # To render results on HTML GUI
    # form_values = [float(x) for x in request.form.values()]
    # form_values = [x for x in request.form.values()]

    form_values = request.form['user-input']
    # test = request.args
    print(form_values)

    # if form_values


    # values_to_model = [np.array(form_values)]
    # prediction = model.predict(form_values)
    # output = prediction[0] 

    ################################################# UPDATE THIS LATER
    # return render_template('index.html', prediction_text='Delay Prediction: {}'.format(output))
    return render_template('index.html', prediction_text={form_values})

if __name__ == "__main__":
    app.run()
