import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset (you should replace this with your data)
movies_data = [
    {"Title": "Iron man", "Genre": ["Action", "Adventure"]},
    {"Title": "Captain America", "Genre": ["Comedy", "Romance"]},
    {"Title": "Transformer", "Genre": ["Action", "Sci-Fi"]},
    {"Title": "Movie 4", "Genre": ["Drama"]},
    {"Title": "Sholay", "Genre": ["Comedy", "Adventure"]},
]

# Create a DataFrame from the dataset
movies_df = pd.DataFrame(movies_data)

# Create a TF-IDF vectorizer to convert genre information into numerical form
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'].apply(lambda x: ' '.join(x)))

# Calculate the cosine similarity between movies based on their genres
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations for a given movie
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies_df.index[movies_df['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Exclude the movie itself (top similarity score)
    movie_indices = [i[0] for i in sim_scores]
    return movies_df[['Title', 'Genre']].iloc[movie_indices]

# Example usage
movie_title = 'Movie 4'  # Replace with the movie you want to find recommendations for

recommendations = get_recommendations(movie_title)

print(f"Top 10 movie recommendations for '{movie_title}':")
print(recommendations)
