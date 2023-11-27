# Import Flask and dependencies
from flask import Flask, render_template, request, jsonify
import json
from flask_cors import CORS
import joblib
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import pickle


### Set up Flask ###
# Create App
app = Flask(__name__)
CORS(app)

# Load K-means model
def load_kmeans_model():
    loaded_kmeans = joblib.load('kmeans_model.pkl')
    return loaded_kmeans

# Load movie data from csv
file_path = ("resources/movies_modified.csv")
def load_csv_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process data and send results to the frontend
@app.route('/process_data', methods=['POST'])
def process_data():
    # Get data from the request
    data = request.get_json()

    # Load the K-means model
    kmeans_model = load_kmeans_model()

    # Predict clusters using the K-means model
    cluster_label = kmeans_model.predict(data)[0]

    # Return the result as JSON
    result = {'cluster_label': cluster_label}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)