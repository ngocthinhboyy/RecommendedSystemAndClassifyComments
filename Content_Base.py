import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset.csv")

features = ['keywords','cast','genres','director']

def combine_features(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
    
thanh="meo"

print(thanh)

print(df)







