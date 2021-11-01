#Recommendation System for choosing the movies that only applied for two UserId

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',15)

#Read files
rating=pd.read_csv('E:/file/ratings.csv')
meta=pd.read_csv('E:/file/movies_metadata.csv')
print(rating.head(2))

#choose the columns
rating = rating.loc[:,['userId','rating','movieId']]
meta = meta.loc[:,['id','vote_average','title','popularity','vote_count']]

#merged dataframes based on the same column
merged = meta.merge(rating, left_on='id', right_on='movieId')
print(merged.head(1))

#find the shape of the merged dataframe
print(merged.shape)

#compare user with ID:817 with user ID:1893
u817 = merged.loc[merged['userId']== 817 , ['movieId','rating']]
u1893 = merged.loc[merged['userId']== 7199 , ['movieId','rating']]

#Find the movies that both of the user ID:817 and user ID:1893 watch and gave rating fot it
mm = u817.merge(u1893, left_on='movieId', right_on='movieId')
print(mm)

#Find the correlation of the user  with ID:817 and user ID:1893
c = mm['rating_x'].corr(mm['rating_y'])
print(c)
