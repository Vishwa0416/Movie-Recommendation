import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess the dataset
movies = pd.read_csv("tmdb_5000_movies.csv")

# Keep only the required columns
movies = movies[['title', 'genres', 'keywords', 'overview']]
movies.dropna(inplace=True)

# Combine relevant text fields
movies['tags'] = movies['overview'].astype(str) + " " + movies['genres'].astype(str) + " " + movies['keywords'].astype(str)

# Create feature vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Store titles separately for the UI
movie_titles = movies['title'].values

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return []
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]
