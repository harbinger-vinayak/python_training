"""
Find out top 5 movie name which have highest rating count from two csv files
The head() returns top 5 records by ascending
The tail() returns top 5 records by descending
"""
import pandas as pd

rating = pd.read_csv('ml-1m/ratings.dat', names=['userId', 'movieId', 'rating', 'time'], sep='::', engine='python')

movies = pd.read_csv('ml-1m/movies.dat', names=['movieId', 'movieName', 'genre'], sep='::', engine='python')

rating_movies = pd.merge(rating, movies, on='movieId')
print rating_movies[rating_movies['rating'] == 5][['movieName', 'rating']].groupby('movieName').size()\
    .sort_values(ascending=False).head()
