# Book Recommendation System

## Project Overview

This project builds a Book Recommendation System that provides personalized book recommendations based on user IDs. The system utilizes collaborative filtering techniques to predict user preferences for various books. The project also includes a Streamlit web application that allows users to input their user ID and receive book recommendations through an interactive interface.

## Key Features

- **User-Based Recommendations**: Provides personalized book suggestions based on a user's previous ratings.
- **Streamlit Web Application**: A simple and interactive web interface for users to input their user ID and get recommendations.
- **Data Analysis and Visualization**: Includes exploratory data analysis to understand user behavior and book popularity.

## Datasets

The system uses three datasets:

- `books.csv`: Metadata about the books.
- `users.csv`: Information about users.
- `ratings.csv`: User ratings for various books.



### Combine the Datasets

The Jupyter notebook `books_recomendation.ipynb` will generate a combined CSV file. Ensure that this combined CSV file is also placed in the project directory.

## How to Run the Project


Clone the repository:

```bash
git clone https://github.com/yourusername/book-recommendation-system.git
cd book-recommendation-system
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Run the Streamlit app:
```bash
streamlit run app.py
```
Open the web browser and navigate to the provided local URL to interact with the recommendation system by inputting a user ID.

## Deployment
You can also access the deployed version of the application here [Click here.](https://books-recommendation.streamlit.app/)

## Screenshots
Here is a screenshot of the web application:
<br>
![Screenshot (54)](https://github.com/user-attachments/assets/47c8ebad-4f72-4176-872a-1a15d1ff41b9)
<br><br>
![screenshot_recommendation](https://github.com/user-attachments/assets/964770ab-9321-455e-b06f-f2e6fa81f9fd)



