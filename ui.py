import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from os.path import exists
from lyrics_similarity_api import Method1 as LyricsSimilarityModel
from user_similarity_api import UserSimilarityModel

def show_image(path):
    img = Image.open(path)
    st.image(img)

lsm = LyricsSimilarityModel()

sim_users = pickle.load(open('pickled_files/user_user_similar.pkl', 'rb'))
user_to_idx = pickle.load(open('pickled_files/user_to_idx.pkl', 'rb'))
idx_to_user = pickle.load(open('pickled_files/idx_to_user.pkl', 'rb'))

users = list(user_to_idx.keys())
songs = lsm.track_lyrics_df['Title'].unique()

st.set_page_config(page_title="Song Recommendation", layout="wide")
title = "Song Recommendation Engine"
st.title(title)
st.write("Created by Amanbeer, Ram, and Shubhangi")

tab1, tab2 = st.tabs(["Lyric-Based Similarity", "User-Based Similarity"])

with tab1:
    song = st.selectbox('Select a song to see similar songs', songs)
    st.write('You have selected song ', song)
    
    if st.button('Show similar songs'):
        lsm.RecommendSongs(song)
        print(song)
        # lsm.LyricCloud(song)
        st.write('The top 5 similar songs to ', song, ' are:')
        st.write(lsm.temp[['Title','Artist name']].values)
        st.markdown('---')
        # st.write('Here\'s a word cloud of the lyrics of the similar songs:')
        # show_image('images/temp_wordcloud.jpg' if not exists('images/wordcloud.png') else 'images/temp_wordcloud.png')

with tab2:
    number = st.number_input('Selected the index of the user you want to recommend songs to', min_value=0, max_value=len(users)-1, value=0)
    st.write('You have selected user ', number)
    st.write('The anonymised name of this user is ', idx_to_user[number], ' but let\'s call them John Doe for now.')
    st.markdown('---')
    st.write('The top 5 songs that John Doe has listened to are:', idx_to_user[number])
    st.markdown('---')
    st.write('Here\'s a word cloud of the lyrics of the songs that John Doe has listened to:')
    show_image('images/temp_wordcloud.jpg')