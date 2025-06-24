import streamlit as st
import pickle
import pandas as pd

# Load Data
movies= pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))


def recommend(movie_title):
  movie_index = movies[movies["title"]== movie_title].index[0]
  distance = similarity[movie_index]
  movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies = []
  recommended_posters = []

  for i in movie_list:
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_posters.append(movies.iloc[i[0]]["poster_url"])                    #using saved url

  return recommended_movies,recommended_posters

# Streamlit UI
st.title("Movie Recommender System")

option = st.selectbox("What would you like to watch..!?",movies["title"].values)

if st.button("Recommend"):
    names,posters = recommend(option)
    for name,poster in zip(names,posters):
       st.write(name)
       st.image(poster)