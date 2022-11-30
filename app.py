# we are using virtual enviornment that means that most of the librabry we are using we need to install them first before we start using thempr
import pickle as pkl
import pandas as pd
import streamlit as st
import requests


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2234cda012e52526ee792fda591639f4&language=en-US".format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

st.title("Movie Recommender System")

# we have transfer our data frame from jupyter notebook to here in form of pickle format
with open("C:/Users/rani/Movie_Recommendation_System/my_data.pkl", "rb") as f:
    file = pkl.load(f)
df = pd.DataFrame(file)

with open("C:/Users/rani/Movie_Recommendation_System/similarity.pkl", "rb") as ff:
    similarity = pkl.load(ff)


selected_movie_name = st.selectbox("what do you like ?",df['title'].values)

if st.button("Recommend"):
    name,posters = recommend(selected_movie_name)
    st.title("Here are some recommendation based on your likes : ")
    st.header(name[0])
    st.image(posters[0])
    st.header(name[1])
    st.image(posters[1])
    st.header(name[2])
    st.image(posters[2])
    st.header(name[3])
    st.image(posters[3])
    st.header(name[4])
    st.image(posters[4])


st.header("Enjoy your day !!!")


