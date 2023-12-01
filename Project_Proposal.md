# Group 2: Project 4 - Movie Selector
## UNC-CH-DA - Project 4 - Machine Learning
## Contributors:
* Hannah Doby
* Aubrey Leary
* Andrew Bourgeois

## Data Sources:
* https://grouplens.org/datasets/movielens/25m/ 
* the data set consists of: MovieLens 25M movie ratings. Stable benchmark dataset. 25 million ratings and one million tag applications applied to 62,000 movies by 162,000 users. Includes tag genome data with 15 million relevance scores across 1,129 tags. Released 12/2019
* The data is broken into multiple CSVs:
    * genome-scores.csv
    * genome-tags.csv
    * links.csv
    * movies.csv
    * ratings.csv
    * tags.csv

## Outline
Our group has decided to create a tool using machine learning which can help with your next movie selection using machine learning. ONce our medel is trained, new users will be able to have the model predict if they will like a new movie, or possibly suggest a next movie to watch, (we haven't decided which way to go yet).

Scope of Work:

* Create GitHub Repository:
    * https://github.com/hannahdoby/project-4

* Pull MovieLens data into a SQL database: 
    * download data and review csvs
    * create schema for tables
    * create a SQL Database using schema to create tables and CSVs to populate tables

* Clean the data using: SQL, Python adn notebooks
    * verify removal of NULL data
    * convert datatypes as needed
    * Split column data

* Setup data hosting location:
    * AWS?
    * Google?

* Create machine learning model:
    * Tools (TBD): Notebook, Python, Pandas, SciKit-Learn, Spark, etc.
    * use notebook to pull in the dataset
    * Using SQL, Spark, Pandas to create a dataframe of the dataset
    * Split our dataset into train and test
    * traing the data and test the results

* Create web based UI for new predictions
    * Tools (TBD): Javascript, HTML, CSS, Leaflet, etc.
    * user can enter new features
    * model will predict outcome
    * UI will display results and give statistics on accuracy
