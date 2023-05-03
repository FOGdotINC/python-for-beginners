import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine
from scipy.stats import pearsonr

def movie_recommendation(ratings, user):
    # Create a pandas dataframe from the ratings dictionary
    df = pd.DataFrame.from_dict(ratings).transpose()
    
    # Calculate the pearson correlation between all users
    corr = df.corr(method='pearson')
    
    # Get the similarity scores for the given user
    sim_scores = corr[user].drop(user)
    
    # Recommend movies based on the highest similarity scores
    recommended_movies = df.columns[np.argsort(-sim_scores.values)][:5]
    
    return recommended_movies

ratings = {
    "user1": {
        "movie1": 4.0,
        "movie2": 3.5,
        "movie3": 2.0,
        "movie4": 3.5,
        "movie5": 3.0,
    },
    "user2": {
        "movie1": 4.5,
        "movie2": 3.0,
        "movie3": 2.5,
        "movie4": 4.0,
        "movie5": 3.5,
    },
    "user3": {
        "movie1": 4.0,
        "movie2": 5.0,
        "movie3": 2.0,
        "movie4": 4.5,
        "movie5": 4.0,
    },
}

user = "user1"

recommended_movies = movie_recommendation(ratings, user)

print("Recommended movies for", user, ":", recommended_movies)
