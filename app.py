# Import Flask and dependencies
from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from flask_cors import CORS
import joblib
from sklearn.cluster import KMeans
import pandas as pd
import pickle


inputs1 = {'Action':2, 'Adventure':5,
        'Animation':2, 'Comedy':3, 'Crime':4, 'Documentary':4, 'Drama':4,
        'Fantasy':1, 'Film-Noir':1, 'Horror':2, 'Musical':0, 'Mystery':5, 'Romance':4,
        'Sci-Fi':2, 'Thriller':1, 'War':5, 'Western':5, '(no genres listed)':1}

inputs2 = {'Action':5/19, 'Adventure':5/19, 'Animation':5/19, 'Comedy':5/19, 'Crime':5/19,
        'Documentary':5/19, 'Drama':5/19, 'Fantasy':5/19, 'Film-Noir':5/19, 'Horror':5/19,
        'Musical':5/19, 'Mystery':5/19, 'Romance':5/19, 'Sci-Fi':5/19, 'Thriller':5/19,
        'War':5/19, 'Western':5/19, '(no genres listed)':5/19}

### Set up Flask ###
# Create App
app = Flask(__name__)
CORS(app)

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process data and send results to the frontend
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page first.'
    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = {}
            for key, value in input_val.items():
                vals[key] = value

        # Load both models and have them make predictions
        model1 = joblib.load("Models/weights_model.pkl")
        model2 = joblib.load("Models/counts_model.pkl")

        prediction1 = model1.predict(pd.DataFrame(inputs1, index=[0]))
        prediction2 = model2.predict(pd.DataFrame(inputs2, index=[0]))

        # This combines the predictions to make an overall cluster
        cluster = int(str(prediction1[0]) + str(prediction2[0]))

        # Read in the csvs
        movie_df = pd.read_csv("Resources/movies.csv")
        genre_df = pd.read_csv("Resources/movies_modified.csv")
        df = pd.read_csv("Resources/average_ratings.csv")

        # Retrieve the movieId
        movie_id = movie_df.loc[movie_df["title"] == "Jumanji (1995)"].values[0][0]

        # Retrieve the genres
        genre_list = genre_df.loc[genre_df["movieId"] == movie_id].values[0][2:]

        # Collect average ratings by genre per cluster
        means = df.loc[df["clusters"] == cluster].groupby("clusters").mean()

        # Calculate the average rating for the input movie
        means = means.values[0][2:]

        # Find the average rating by the cluster of a movie with each of these genres
        weights_list = []
        for i in range(len(genre_list)):
            weights_list.append(means[i] * genre_list[i])
        output_average = sum(weights_list) / sum(genre_list)

        # This is our output guess at how they would rate the movie
        output_average

        # Return predicted movie rating
        return render_template('predict.html', result=output_average)
        model1 = joblib.load("Models/weights_model.pkl")
        model2 = joblib.load("Models/counts_model.pkl")

        prediction1 = model1.predict(pd.DataFrame(inputs1, index = [0]))
        prediction2 = model2.predict(pd.DataFrame(inputs2, index = [0]))

        #This combines the predictions to make an overall cluster
        cluster = int(str(prediction1[0])+str(prediction2[0]))

        #Read in the csvs
        movie_df = pd.read_csv("Resources/movies.csv")
        genre_df = pd.read_csv("Resources/movies_modified.csv")
        df = pd.read_csv("Resources/average_ratings.csv")

        #Retrieve the movieId
        movie_id = movie_df.loc[movie_df["title"]=="Jumanji (1995)"].values[0][0]

        #Retrieve the genres
        genre_list = genre_df.loc[genre_df["movieId"]==movie_id].values[0][2:]

        #Collect average ratings by genre per cluster
        means = df.loc[df["clusters"]==cluster].groupby("clusters").mean()

        #Calculate the average rating for the input movie
        means = means.values[0][2:]

        #Find the average rating by the cluster of a movie with each of these genres
        weights_list = []
        for i in range(len(genre_list)):
            weights_list.append(means[i]*genre_list[i])
        output_average = sum(weights_list)/sum(genre_list)

        #This is our output guess at how they would rate the movie
        output_average

#return predicted movie rating         
    return render_template(
        'predict.html', result = output_average
    )

    
    
# # Load K-means model
# def load_kmeans_model():
    #loaded_kmeans = joblib.load('kmeans_model.pkl')
    #return loaded_kmeans

# # Load movie data from csv
# file_path = ("resources/movies_modified.csv")
# def load_csv_data(file_path):
#     data = pd.read_csv(file_path)
#     return data   

# # Route to the home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route to process data and send results to the frontend
# @app.route('/process_data', methods=['POST'])
# def process_data():      
# # Get data from the request
# data = request.get_json()

# # Load the K-means model
# kmeans_model = load_kmeans_model()

# # Predict clusters using the K-means model
# cluster_label = kmeans_model.predict(data)[0]

# # Return the result as JSON
# result = {'cluster_label': cluster_label}
# return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)