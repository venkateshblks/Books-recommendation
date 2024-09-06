import streamlit as st
import pandas as pd
from recommend import load_data, create_user_item_matrix, calculate_user_similarity, recommend_books


# @st.experimental_singleton
def initialize_data():
    data = load_data('data.csv')
    user_item_matrix = create_user_item_matrix(data)
    user_similarity_df = calculate_user_similarity(user_item_matrix)
    user_ids = sorted(user_item_matrix.index.tolist())
    return data, user_item_matrix, user_similarity_df, user_ids

data, user_item_matrix, user_similarity_df, user_ids = initialize_data()
# data = load_data('data.csv')
# user_item_matrix = create_user_item_matrix(data)
# user_similarity_df = calculate_user_similarity(user_item_matrix)
# user_ids = sorted(user_item_matrix.index.tolist())
st.title('Book Recommendation System')
user_id = st.selectbox(
    'Select your User ID:',
    options=user_ids,
    
)
if st.button('Get Recommendations'):
    recommendations = recommend_books(user_id, user_item_matrix, user_similarity_df)
    if not recommendations.empty:
            st.write('Recommended Books:')            
            cols = st.columns(3)  
            for i, book in enumerate(recommendations.index):
                book_details = data[data['Book-Title'] == book].iloc[0]
                col_index = i % 3
                with cols[col_index]:
                    st.image(book_details['Image-URL-L'], caption=book_details['Book-Title'], width=150)
                    st.write(f"**Title:** {book_details['Book-Title']}")
                    st.write(f"**Author:** {book_details['Book-Author']}")
                    st.write(f"**Publisher:** {book_details['Publisher']}")
                    st.write(f"**Year:** {book_details['Year-Of-Publication']}")
    else:
        st.write('No recommendations available.')
