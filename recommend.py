import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

# Create user-item matrix
def create_user_item_matrix(data):
    user_item_matrix = data.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating')
    user_item_matrix.fillna(0, inplace=True)
    return user_item_matrix

# Calculate similarity between users
def calculate_user_similarity(user_item_matrix):
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    return user_similarity_df

# Get similar users
def get_similar_users(user_id, user_similarity_df, top_n=5):
    if user_id not in user_similarity_df.index:
        return pd.Series()
    similar_scores = user_similarity_df[user_id]
    similar_users = similar_scores.sort_values(ascending=False).index[1:top_n+1]
    return similar_users

# Recommend books
def recommend_books(user_id, user_item_matrix, user_similarity_df, top_n=6):
    similar_users = get_similar_users(user_id, user_similarity_df, top_n)
    if similar_users.empty:
        return pd.Series()
    
    recommended_books = pd.DataFrame()
    
    for similar_user in similar_users:
        similar_user_books = user_item_matrix.loc[similar_user]
        recommended_books = pd.concat([recommended_books, similar_user_books], axis=1)
    
    recommended_books = recommended_books.mean(axis=1).sort_values(ascending=False)
    return recommended_books.head(top_n)
