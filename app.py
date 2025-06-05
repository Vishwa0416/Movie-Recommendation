import streamlit as st
from recommendation_engine import recommend

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎥 Movie Recommendation System")
st.write("Enter your favorite movie and get 5 similar movie suggestions!")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        recommendations = recommend(movie_name)
        if recommendations:
            st.subheader("📽️ Recommended Movies:")
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")
        else:
            st.error("Movie not found in dataset.")
