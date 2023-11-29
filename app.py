# Import Flask and dependencies
from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from flask_cors import CORS, cross_origin
import joblib
from sklearn.cluster import KMeans
import pandas as pd
import pickle

### Set up Flask ###
# Create App
app = Flask(__name__)
CORS(app, supports_credentials=True, methods = ["GET", "POST"],allow_headers=["Content-Type", "Authorization"])


inputs1 = {'Action':2, 'Adventure':5,
        'Animation':2, 'Children':2, 'Comedy':3, 'Crime':4, 'Documentary':4, 'Drama':4,
        'Fantasy':1, 'Film-Noir':1, 'Horror':2, 'Musical':0, 'Mystery':5, 'Romance':4,
        'Sci-Fi':2, 'Thriller':1, 'War':5, 'Western':5, '(no genres listed)':1}


inputs2 = {'Action':0.313, 'Adventure':0.255, 'Animation':0.068, 'Children':0.896, 'Comedy':0.347, 'Crime':0.179,
       'Documentary':0.008, 'Drama':0.442, 'Fantasy':0.115, 'Film-Noir':0.008, 'Horror':0.062,
       'Musical':0.039, 'Mystery':0.079, 'Romance':0.188, 'Sci-Fi':0.179, 'Thriller':0.280,
       'War':0.056, 'Western':0.019, '(no genres listed)':0.000}




# Route to the home page
@app.route('/')
@cross_origin(supports_credentials=True)
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# Route to process data and send results to the frontend
@app.route('/predict', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)

def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page first.'
    if request.method == 'POST':
        input_val = request.get_json()


        if input_val:
            action_rating = input_val.get("Action")
            adventure_rating = input_val.get("Adventure")
            anim_rating = input_val.get("Animation")
            children_rating = input_val.get("Children")
            comedy_rating = input_val.get("Comedy")
            crime_rating = input_val.get("Crime")
            doc_rating = input_val.get("Documentary")
            drama_rating = input_val.get("Drama")
            fant_rating = input_val.get("Fantasy")
            noir_rating = input_val.get("Film-Noir")
            horror_rating = input_val.get("Horror")
            music_rating = input_val.get("Musical")
            mystery_rating = input_val.get("Mystery")
            rom_rating = input_val.get("Romance")
            sci_rating = input_val.get("Sci-Fi")
            thrill_rating = input_val.get("Thriller")
            war_rating = input_val.get("War")
            western_rating = input_val.get("Western")
            no_rating = input_val.get("(no genres listed)")
            movie_input = input_val.get("newMovieTitle")

        inputs1 = {'Action':float(action_rating), 'Adventure':float(adventure_rating),
        'Animation':float(anim_rating), 'Children':float(children_rating), 'Comedy':float(comedy_rating), 'Crime':float(crime_rating), 'Documentary':float(doc_rating), 'Drama':float(drama_rating),
        'Fantasy':float(fant_rating), 'Film-Noir':float(noir_rating), 'Horror':float(horror_rating), 'Musical':float(music_rating), 'Mystery':float(mystery_rating), 'Romance':float(rom_rating),
        'Sci-Fi':float(sci_rating), 'Thriller':float(thrill_rating), 'War':float(war_rating), 'Western':float(western_rating), '(no genres listed)':float(no_rating)}

        print(inputs1)
        sum_data = []
        count = 0
        for i in inputs1:
            if inputs1[i] != 0:
                count += 1
                sum_data.append(inputs1[i])
        user_mean = sum(sum_data)/count

        for key in inputs1:
            inputs1[key] = (inputs1[key]-user_mean)/user_mean

        #Load both models and have them make predictions
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
        counts_df = pd.read_csv("Resources/ratings_counts.csv")

        #Retrieve the movieId
        movie_id = movie_df.loc[movie_df["title"]==movie_input].values[0][0]

        #Retrieve the genres
        genre_list = genre_df.loc[genre_df["movieId"]==movie_id].values[0][2:]

        #Collect average ratings by genre per cluster
        means = df.loc[df["clusters"]==cluster].groupby("clusters").mean()
        pre_weights = counts_df.loc[counts_df["clusters"]==cluster].groupby("clusters").mean()

        #Calculate the average rating for the input movie
        means = means.values[0][1:]
        pre_weights = pre_weights.values[0][1:]

        weights_list = []
        for i in range(len(genre_list)):
            weights_list.append(means[i]*genre_list[i])
        output_average = sum(weights_list)/sum(genre_list)*user_mean+user_mean

        #This is our output guess at the odds that the user would like this movie taking into account how this specific user tends to rate
        output_percent = round(output_average/5*100)
        print(movie_input +" is a "+str(round(output_average/5*100))+"% match for you.")

        # Return predicted movie rating
        return jsonify({"percent":output_percent})


if __name__ == '__main__':
    app.run(debug=True)