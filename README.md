# Group 2: Project 4 - Movie Selector
## UNC-CH-DA - Project 4 - Machine Learning
## Contributors:
* Hannah Doby
* Aubrey Leary
* Andrew Bourgeois

## Data Sources:
* https://grouplens.org/datasets/movielens/25m/ 
* the data set consists of: MovieLens 25M movie ratings. Stable benchmark dataset. 25 million ratings and one million tag applications applied to 62,000 movies by 162,000 users. Includes tag genome data with 15 million relevance scores across 1,129 tags. Released 12/2019
The data is broken into multiple CSVs:
* genome-scores.csv
* genome-tags.csv
* links.csv
* movies.csv
* ratings.csv
* tags.csv

## Outline
Our group has decided to create a tool using machine learning which can help with your next movie selection using machine learning. Once our model is trained, new users will be able to have the model predict if they will like a new movie, or possibly suggest a next movie to watch.

# Scope of Work:

## Create GitHub Repository:
* https://github.com/hannahdoby/project-4

## Pull MovieLens data into Pandas: 
* download data and review csvs
* create Pandas dataframes
* merge and clean dataframes

## Clean the data using: Python Pandas
* verify removal of NULL data
* convert datatypes as needed
* Split column data

## Setup front-end interface:
* HTML/CSS/JS

## Create machine learning model:
* Tools: JupyterNotebook, Python, Pandas, SciKit-Learn, Flask, Spark
* Use notebook to pull in the dataset
* Use Pandas to create a DataFrame of the dataset
* Use data to fit two KMeans models to different trend categories
* Comb data for trends in results, verify creation of clusters and accuracy
* Export trained models as .pkl files


## Create web based UI for new predictions
* Tools: Javascript, HTML, CSS, Flask
* User can enter new features
* Model will predict percentage compatibility between user and desired movie
* UI will display results and give prediction
* Extended capability for giving movie recommendations included in [run_model_process.ipynb](Data_Preparation/run_model_process.ipynb) but not yet integrated into UI


## Future goals
* Edit UI as well as back-end to allow users to rate movies, rather than just genres. This will increase accuracy of model 2 application to new users (currently hard-coded to average values, so places all new users in the same cluster)
* Store new-user inputs for improvement of model through refitting 
* Incorporate tag data for increased specificity of model results 
* Host ratings.csv information on SQLite server to allow repository visitors to run full capability of predictive model. At this time, ratings.csv is too large to be hosted on GitHub.