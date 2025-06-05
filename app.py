import streamlit as st
from recommendation_engine import recommend, movie_titles

st.title('🎬 Movie Recommendation System')

st.markdown("""
### 📌 How to Use:
1. Start typing a movie name in the search box.
2. Select a movie from the suggestions.
3. Click **"Show Recommendations"** to see movies similar to the selected one.

💡 Make sure you enter a valid movie from the list.
""")

# Use selectbox for auto-suggestion
selected_movie = st.selectbox("Search for a movie", movie_titles)

if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write(f"🎥 {movie}")
    else:
        st.warning("No recommendations found.")
