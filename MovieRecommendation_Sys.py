#Recommendation system for choosing Movie
import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)

#read data
rating = pd.read_csv('E:/file/ratings.csv')
meta = pd.read_csv('E:/file/movies_metadata.csv')
# select the columns that that need
rating = rating.loc[:, ['userId', 'rating', 'movieId']]
meta = meta.loc[:, ['id', 'vote_average', 'title', 'popularity', 'vote_count']]

#merge two dataset based on movieId
merged = meta.merge(rating, left_on='id', right_on='movieId')
print(merged.head(1))
print(merged.shape)
# Compare user ID 1923 with rest of the users
for i in merged['userId']:
    ui = merged.loc[merged['userId'] == i, ['movieId', 'rating']]
    u1923 = merged.loc[merged['userId'] == 1923, ['movieId', 'rating']]
    mm = u1923.merge(ui, left_on='movieId', right_on='movieId')
    column_1 = mm['rating_x']
    column_2 = mm['rating_y']
    #find the correlation of column_1 and column_1
    correlation = column_1.corr(column_2, method='spearman')
    maxi = np.max(correlation, axis=None)
    #find the maximum of correlation of user 1923 with rest of the users
    print(i, maxi)
