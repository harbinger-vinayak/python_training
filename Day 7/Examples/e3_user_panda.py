"""
Find out top 5 movie name which have user input genre
"""
import pandas as pd
import re

# print raw_input("Enter a movie genre: ")
rating = pd.read_csv('ml-1m/ratings.dat', names=['userId', 'movieId', 'rating', 'time'], sep='::', engine='python')
movies = pd.read_csv('ml-1m/movies.dat', names=['movieId', 'movieName', 'genre'], sep='::', engine='python')

rating_movies = pd.merge(rating, movies, on='movieId')
dataset = rating_movies['rating'].str.contains('comedy', key=False)
print dataset
# print rating_movies[rating_movies['rating'] == 5][['movieName', 'rating']].groupby('movieName').size()\
    # .sort_values(ascending=False).head()


'''
def split_it(genre):
    return re.findall('comedy', genre, re.I)
# movies['genre'].apply(lambda x: split_it(x)

movies = pd.read_csv('ml-1m/movies.dat', names=['movieId', 'movieName', 'genre'], sep='::', engine='python')
# print movies['genre'].apply(lambda x: split_it(x))
print movies[movies['genre'] == (lambda x: split_it(x))].head()
# print movies[movies['genre'] == (lambda x: split_it(x))][['movieName', 'genre']].groupby('genre').size().sort_values(ascending=False).head()
# print movies[['movieName', 'genre']].apply(lambda x: split_it(x))
'''