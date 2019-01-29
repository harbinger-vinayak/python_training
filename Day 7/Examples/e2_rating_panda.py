"""
Find out top 5 movieId which have highest rating count
The head() returns top 5 records by ascending
The tail() returns top 5 records by descending
"""
import pandas as pd

rating = pd.read_csv('ml-1m/ratings.dat', names=['userID', 'movieId', 'rating', 'time'], sep='::', engine='python')

print rating[['movieId', 'rating']].groupby('movieId').size().sort_values(ascending=False).head()
# print rating[['movieId', 'rating']].groupby('movieId').count()['rating'].sort_values(ascending=False).head(10)
